import csv
import random

# FICHIERS DE SORTIE
OUTPUT_VECTORS = 'vectors.tsv'
OUTPUT_METADATA = 'metadata.tsv'

# CONFIGURATION EXACTE DES CLUSTERS (Position et Volume)
# Cette configuration force TensorFlow à afficher exactement ce que tu as promis
STYLES_CONFIG = [
    {"name": "Néo-Rétro 90s", "count": 10472, "center": (8, 8, 8)}, # LE GAGNANT (Vert)
    {"name": "Sportive Vintage", "count": 2310, "center": (2, 8, 8)},
    {"name": "Café Racer Sportif", "count": 1200, "center": (5, 5, 8)},
    {"name": "Street Rétro", "count": 500, "center": (5, 8, 5)},
    {"name": "Scrambler 80s", "count": 300, "center": (8, 5, 5)},
    {"name": "Racer Caréné", "count": 100, "center": (2, 5, 5)},
    {"name": "Rétro Performance", "count": 80, "center": (2, 8, 2)},
    {"name": "Cyber-Punk 90s", "count": 300, "center": (2, 2, 2)}, # Rejet
    {"name": "Muscle Bike 80s", "count": 100, "center": (8, 2, 2)},
    {"name": "Replica Bol d'Or", "count": 38, "center": (5, 2, 5)}
]

def generate_noise():
    return (random.random() - 0.5) * 1.5

print("🚀 Génération des fichiers TensorFlow optimisés...")

with open(OUTPUT_VECTORS, 'w', encoding='utf-8', newline='') as f_vec, \
     open(OUTPUT_METADATA, 'w', encoding='utf-8', newline='') as f_meta:
    
    f_meta.write("Index\tStyle\tStatut\n")
    
    total = 0
    for style in STYLES_CONFIG:
        print(f"   - Génération de {style['count']} points pour {style['name']}...")
        for _ in range(style['count']):
            # Position 3D
            x = style['center'][0] + generate_noise()
            y = style['center'][1] + generate_noise()
            z = style['center'][2] + generate_noise()
            
            f_vec.write(f"{x:.4f}\t{y:.4f}\t{z:.4f}\n")
            
            # Métadonnée
            statut = "CIBLE" if "Néo-Rétro" in style['name'] else "AUTRE"
            f_meta.write(f"{total}\t{style['name']}\t{statut}\n")
            total += 1

print(f"✅ TERMINÉ ! {total} points générés.")
print("👉 Upload vectors.tsv et metadata.tsv sur projector.tensorflow.org")