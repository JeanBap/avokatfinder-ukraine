#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

def update_sitemap():
    """Update sitemap with new glossary entries."""
    glossary_dir = Path('glossary')
    if not glossary_dir.exists():
        print("No glossary directory found.")
        return
    
    # Create/update sitemap.xml
    root = ET.Element('urlset')
    root.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Add homepage
    url_elem = ET.SubElement(root, 'url')
    loc = ET.SubElement(url_elem, 'loc')
    loc.text = f'https://avokatfinder-{country}.local/'
    lastmod = ET.SubElement(url_elem, 'lastmod')
    lastmod.text = datetime.now().strftime('%Y-%m-%d')
    
    # Add glossary terms
    for html_file in sorted(glossary_dir.glob('*.html')):
        slug = html_file.stem
        url_elem = ET.SubElement(root, 'url')
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = f'https://avokatfinder-{country}.local/glossary/{slug}/'
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = '0.8'
    
    # Write sitemap
    tree = ET.ElementTree(root)
    tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
    
    glossary_count = len(list(glossary_dir.glob('*.html')))
    print(f"Sitemap updated: {glossary_count} glossary entries indexed")

if __name__ == '__main__':
    update_sitemap()
