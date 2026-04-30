#!/usr/bin/env python3
import json
import os
from pathlib import Path

def rebuild_glossary_index():
    """Rebuild glossary index for this country."""
    glossary_dir = Path('glossary')
    if not glossary_dir.exists():
        print("No glossary directory found.")
        return
    
    terms = []
    for html_file in sorted(glossary_dir.glob('*.html')):
        slug = html_file.stem
        terms.append({
            'slug': slug,
            'file': f'glossary/{slug}.html'
        })
    
    index_data = {
        'total_terms': len(terms),
        'last_updated': '2026-04-30',
        'terms': terms
    }
    
    with open('glossary-index.json', 'w') as f:
        json.dump(index_data, f, indent=2)
    
    print(f"Glossary index rebuilt: {len(terms)} terms indexed")

if __name__ == '__main__':
    rebuild_glossary_index()
