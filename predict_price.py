import sys
import json


def estimate_price(theta0: float,
                   theta1: float,
                   mileage: float) -> float:
    """Estimate the price for a given mileage."""
    return theta0 + theta1 * mileage

def main():
    try:
        mileage = int(input("Enter your mileage: "))
    except ValueError:
        print("Error: mileage must be a valid integer")
        sys.exit(1)

    if mileage < 0:
        print("Mileage must be a positive integer")
        sys.exit(1)

    try:
        with open('theta.json', 'r') as file:
            theta = json.load(file)
    except FileNotFoundError:
        print("theta.json does not exist yet, theta0 and theta1 will be assign to '0'")
        theta = {'theta0': 0, 'theta1': 0}
    except json.JSONDecodeError:
        print("Error: theta.json is corrupted")
        sys.exit(1)

    if 'theta0' not in theta or 'theta1' not in theta:
        print("Error: theta.json is missing theta0 or theta1")
        sys.exit(1)

    price = estimate_price(theta['theta0'], theta['theta1'], mileage)
    print(f"Estimated price: {price:.2f}$")

if __name__ == "__main__":
    main()