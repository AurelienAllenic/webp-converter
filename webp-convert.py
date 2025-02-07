import os
import sys
import requests
from PIL import Image
from io import BytesIO

# 📌 Définition du dossier de sortie
OUTPUT_FOLDER = "converted-images"

def convert_to_webp(input_path, output_folder, quality=80):
    # 📌 Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        if input_path.startswith("http"):  # 📌 Télécharger si c'est une URL
            response = requests.get(input_path, stream=True)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            file_name = os.path.basename(input_path).split("?")[0]  # Récupère le nom du fichier
        else:  # 📌 Gestion d'un fichier local
            image = Image.open(input_path)
            file_name = os.path.basename(input_path)

        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".webp")

        # ✅ Convertit et sauvegarde en WebP
        image.save(output_path, "WEBP", quality=quality)
        print(f"✅ Conversion réussie : {output_path}")

    except Exception as e:
        print(f"❌ Erreur lors de la conversion : {e}")

# 📌 Vérifie si une URL a été passée en argument
if len(sys.argv) > 1:
    input_path = sys.argv[1]
else:
    input_path = input("🔹 Entrez l'URL de l'image ou le chemin du fichier local : ").strip()

# 📌 Lancer la conversion
convert_to_webp(input_path, OUTPUT_FOLDER)
