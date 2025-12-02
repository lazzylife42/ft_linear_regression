# predict.py
import json

# Lire les theta sauvegardés
with open('theta.json', 'r') as f:
    data = json.load(f)
    theta0 = data['theta0']
    theta1 = data['theta1']

# Demander le kilométrage
km = float(input("Entrez un kilométrage : "))

# Prédire
price = theta0 + theta1 * km
print(f"Prix estimé : {price:.2f}€")