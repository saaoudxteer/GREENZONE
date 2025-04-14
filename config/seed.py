import os
import sys
from django.core.files import File

# Assure que le chemin de base du projet est dans le PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from accommodations.models import Accommodation
from django.contrib.auth.models import User

# Récupère un utilisateur (le premier trouvé)
user = User.objects.first()
if not user:
    raise Exception("❌ Aucun utilisateur trouvé. Crée un superuser d'abord avec : python manage.py createsuperuser")


# Insertion en base de données
logements_verts = [

    ("Tiny House en forêt", "Maison en bois au cœur de la nature", "Lyon", 55.0, 2, "tiny_house_marseille.jpg"),
    ("Maison solaire autonome", "A modern eco-house with solar panels on the roof, located in a sunny suburb of Toulouse. Surrounded by green garden beds, this house is completely energy independent.", "Toulouse", 80.0, 4, "maison_solaire_toulouse.jpg"),
    ("Maison autonome en Provence", "Une maison autonome nichée dans la campagne provençale, entourée de champs de lavande et de collines. Conçue pour être 100% indépendante en énergie grâce à des panneaux solaires, un système de récupération d’eau de pluie et des matériaux écologiques.", "Aix-en-Provence", 90.0, 3, "maison_autonome_provence.jpg"),
    ("Maison bioclimatique", "A bioclimatic eco-house in Montpellier with a green roof, solar panels, and Mediterranean plants.", "Montpellier", 90.0, 3, "maison_bioclimatique_montpellier.jpg"),
    ("Villa écologique à Nice", "Villa moderne avec toiture végétalisée et panneaux solaires, située sur les hauteurs de Nice avec vue sur la mer. Matériaux écologiques et autonomie énergétique.", "Nice", 95.0, 4, "villa_eco_nice.jpg")

]

for title, desc, city, price, cap, img_name in logements_verts:
    image_path = os.path.join('media', 'accommodations', img_name)
    if not os.path.exists(image_path):
        print(f"⚠️ Image non trouvée : {image_path} — logement '{title}' non créé.")
        continue

    with open(image_path, 'rb') as img_file:
        Accommodation.objects.create(
            title=title,
            description=desc,
            address="Adresse écolo",
            city=city,
            price_per_night=price,
            capacity=cap,
            owner=user,
            is_green=True,
            image=File(img_file)
        )

