#!/usr/bin/env python3
"""
Conversor de KML para formato MyFarm.

Uso:
    python convert_kml.py <arquivo_entrada.kml> <diretorio_saida>

Converte um arquivo KML (exportado do Google Earth, MyMaps, etc.)
para o formato aceito pelo MyFarm ERP. Gera um arquivo por talhão.

Dependências:
    pip install shapely --break-system-packages
"""

import sys
import uuid
import os
from xml.etree import ElementTree as ET

try:
    from shapely.geometry import Polygon
    HAS_SHAPELY = True
except ImportError:
    HAS_SHAPELY = False


def is_clockwise_manual(coords):
    """Verifica sentido horário usando Shoelace formula."""
    total = 0
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        total += (x2 - x1) * (y2 + y1)
    return total > 0


def is_clockwise(coords):
    """Verifica se polígono está em sentido horário (CW)."""
    if HAS_SHAPELY:
        poly = Polygon(coords)
        return not poly.exterior.is_ccw
    return is_clockwise_manual(coords)


def parse_coordinates(coords_text):
    """
    Extrai coordenadas limpas de uma string KML.
    Remove altitude, arredonda para 7 decimais, remove artefatos float.
    """
    pairs = coords_text.strip().split()
    coords = []
    for p in pairs:
        parts = p.split(',')
        if len(parts) >= 2:
            lon = round(float(parts[0]), 7)
            lat = round(float(parts[1]), 7)
            coords.append((lon, lat))
    return coords


def ensure_clockwise(coords):
    """Garante que o polígono está em sentido horário (CW)."""
    if not is_clockwise(coords):
        coords = list(reversed(coords))
    return coords


def ensure_closed(coords):
    """Garante que o polígono está fechado."""
    if coords[0] != coords[-1]:
        coords.append(coords[0])
    return coords


def sanitize_name(name, max_length=50):
    """
    Valida e ajusta o nome do talhão.
    Retorna (nome_ajustado, foi_truncado).
    """
    if not name or name.strip() == '' or 'sem titulo' in name.lower() or 'sem título' in name.lower():
        return None, False
    name = name.strip()
    if len(name) <= max_length:
        return name, False
    return name[:max_length], True


def safe_filename(name):
    """Gera nome de arquivo seguro a partir do nome do talhão."""
    safe = name.replace(' ', '_')
    for char in '()./\\:*?"<>|':
        safe = safe.replace(char, '')
    return safe


def generate_myfarm_kml(name, coords):
    """Gera string KML no formato aceito pelo MyFarm."""
    pm_id = str(uuid.uuid4())
    coords_str = ' '.join(f"{c[0]},{c[1]}" for c in coords)

    return (
        f'<?xml version="1.0" encoding="UTF-8"?>'
        f'<kml><Document id="featureCollection">'
        f'<Placemark id="{pm_id}">'
        f'<name>{name}</name>'
        f'<MultiGeometry><Polygon><outerBoundaryIs><LinearRing>'
        f'<coordinates>{coords_str}</coordinates>'
        f'</LinearRing></outerBoundaryIs></Polygon></MultiGeometry>'
        f'</Placemark></Document></kml>'
    )


def extract_placemarks(kml_path):
    """
    Extrai todos os Placemarks com polígonos de um KML.
    Retorna lista de dicts: {'name': str, 'coords': [(lon,lat), ...], 'source': str}
    """
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    tree = ET.parse(kml_path)
    root = tree.getroot()

    # Tentar com e sem namespace
    doc = root.find('kml:Document', ns)
    if doc is None:
        doc = root.find('Document')
    if doc is None:
        doc = root  # KML sem Document wrapper

    placemarks = []

    def extract_from_element(element, source_label):
        pms = element.findall('kml:Placemark', ns)
        if not pms:
            pms = element.findall('Placemark')
        for pm in pms:
            name_el = pm.find('kml:name', ns)
            if name_el is None:
                name_el = pm.find('name')
            name = name_el.text.strip() if name_el is not None and name_el.text else None

            coords_el = pm.find('.//kml:coordinates', ns)
            if coords_el is None:
                coords_el = pm.find('.//coordinates')
            if coords_el is not None and coords_el.text:
                coords = parse_coordinates(coords_el.text)
                if len(coords) >= 3:
                    placemarks.append({
                        'name': name,
                        'coords': coords,
                        'source': source_label
                    })

    # Extrair de Folders
    folders = doc.findall('kml:Folder', ns)
    if not folders:
        folders = doc.findall('Folder')
    for folder in folders:
        folder_name_el = folder.find('kml:name', ns)
        if folder_name_el is None:
            folder_name_el = folder.find('name')
        folder_name = folder_name_el.text.strip() if folder_name_el is not None and folder_name_el.text else 'Folder'
        extract_from_element(folder, f'folder:{folder_name}')

    # Extrair soltos no Document
    extract_from_element(doc, 'document')

    return placemarks


def deduplicate(placemarks):
    """
    Remove Placemarks duplicados (mesmo conjunto de coordenadas).
    Prioriza os que vieram de Folders.
    """
    seen = {}
    for pm in placemarks:
        key = frozenset(pm['coords'])
        if key not in seen:
            seen[key] = pm
        elif pm['source'].startswith('folder:') and not seen[key]['source'].startswith('folder:'):
            seen[key] = pm  # Priorizar o da folder
    return list(seen.values())


def convert_kml(input_path, output_dir):
    """
    Converte um KML para o formato MyFarm.
    Retorna relatório da conversão.
    """
    os.makedirs(output_dir, exist_ok=True)

    placemarks = extract_placemarks(input_path)
    original_count = len(placemarks)

    placemarks = deduplicate(placemarks)
    dedup_removed = original_count - len(placemarks)

    report = {
        'input': input_path,
        'total_found': original_count,
        'duplicates_removed': dedup_removed,
        'converted': [],
        'errors': [],
        'name_adjustments': []
    }

    tl_counter = 1

    for pm in placemarks:
        try:
            # Nome
            name, was_truncated = sanitize_name(pm['name'])
            if name is None:
                name = f"TL{tl_counter:02d}"
                tl_counter += 1
                report['name_adjustments'].append(
                    f"Placemark sem nome válido: atribuído '{name}'"
                )
            elif was_truncated:
                report['name_adjustments'].append(
                    f"Nome truncado: '{pm['name']}' -> '{name}'"
                )

            # Coordenadas
            coords = pm['coords']
            coords = ensure_clockwise(coords)
            coords = ensure_closed(coords)

            # Gerar KML
            kml_content = generate_myfarm_kml(name, coords)

            # Salvar
            filename = f"{safe_filename(name)}.kml"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(kml_content)

            report['converted'].append({
                'name': name,
                'file': filepath,
                'points': len(coords)
            })

        except Exception as e:
            report['errors'].append({
                'name': pm.get('name', 'desconhecido'),
                'error': str(e)
            })

    return report


def print_report(report):
    """Imprime relatório legível da conversão."""
    print(f"\n{'='*50}")
    print(f"Conversão KML para MyFarm")
    print(f"{'='*50}")
    print(f"Arquivo: {report['input']}")
    print(f"Talhões encontrados: {report['total_found']}")
    print(f"Duplicados removidos: {report['duplicates_removed']}")
    print(f"Convertidos: {len(report['converted'])}")
    print(f"Erros: {len(report['errors'])}")

    if report['name_adjustments']:
        print(f"\nAjustes de nome:")
        for adj in report['name_adjustments']:
            print(f"  - {adj}")

    if report['converted']:
        print(f"\nArquivos gerados:")
        for c in report['converted']:
            print(f"  - {c['file']} ({c['name']}, {c['points']} pontos)")

    if report['errors']:
        print(f"\nErros:")
        for e in report['errors']:
            print(f"  - {e['name']}: {e['error']}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python convert_kml.py <arquivo.kml> <diretorio_saida>")
        sys.exit(1)

    report = convert_kml(sys.argv[1], sys.argv[2])
    print_report(report)
