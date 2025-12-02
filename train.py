# train.py
import pandas as pd
import json

def calculate_error(theta0: float, 
                    theta1: float, 
                    kms: list[float], 
                    prices: list[float]) -> float:
    """
    Calcule l'erreur moyenne entre les prédictions et les prix réels.
    """
    errors = []

    for km, price in zip(kms, prices):
        prediction = theta0 + theta1 * km
        error = abs(prediction - price)
        errors.append(error)

    return sum(errors) / len(errors)

def iterate_gradient_descent(kms: list[float], 
                             prices: list[float], 
                             theta0: float, 
                             theta1: float, 
                             step: float,
                             iterations: int) -> tuple[float, float]:
    """
    Descente de gradient simple
    """
    for _ in range(iterations):
        error = calculate_error(theta0, theta1, kms, prices)
        
        # Teste les 4 directions
        error_up_0 = calculate_error(theta0 + step, theta1, kms, prices)
        error_down_0 = calculate_error(theta0 - step, theta1, kms, prices)
        error_up_1 = calculate_error(theta0, theta1 + step * 0.0001, kms, prices)
        error_down_1 = calculate_error(theta0, theta1 - step * 0.0001, kms, prices)
        
        # Bouge vers la meilleure direction
        best = min(error, error_up_0, error_down_0, error_up_1, error_down_1)
        
        if best == error_up_0:
            theta0 += step
        elif best == error_down_0:
            theta0 -= step
        elif best == error_up_1:
            theta1 += step * 0.0001
        elif best == error_down_1:
            theta1 -= step * 0.0001
        else:
            step *= 0.95
        
        if step < 0.01:
            break
    
    return theta0, theta1

# Charger les données
df = pd.read_csv("data.csv")
kms = df['km'].values
prices = df['price'].values

# Entraîner
theta0, theta1 = iterate_gradient_descent(kms, prices, 8000, -0.02, 100, 1000)

print(f"Entraînement terminé !")
print(f"theta0 = {theta0:.2f}")
print(f"theta1 = {theta1:.6f}")

# Sauvegarder les theta
with open('theta.json', 'w') as f:
    json.dump({'theta0': theta0, 'theta1': theta1}, f)

print("Thetas sauvegardés dans theta.json")