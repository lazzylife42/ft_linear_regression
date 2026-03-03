import sys
import json
import pandas as pd
from typing import Tuple


def train_model(df: pd.DataFrame,
                learning_rate: float,
                iterations: int) -> Tuple[float, float]:
    """Learn from training data and return theta0, theta1"""
    mileages = df['km'].values.astype(float)
    prices = df['price'].values.astype(float)

    mileages_mean, mileages_std = mileages.mean(), mileages.std()
    prices_mean, prices_std = prices.mean(), prices.std()

    mileages_norm = (mileages - mileages_mean) / mileages_std
    prices_norm = (prices - prices_mean) / prices_std

    theta0, theta1 = 0.0, 0.0
    m = len(df)

    for _ in range(iterations):
        predictions = theta0 + theta1 * mileages_norm
        errors = predictions - prices_norm

        tmp_theta0 = learning_rate * (1 / m) * errors.sum()
        tmp_theta1 = learning_rate * (1 / m) * (errors * mileages_norm).sum()

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    theta1_real = theta1 * (prices_std / mileages_std)
    theta0_real = prices_mean + prices_std * theta0 - theta1_real * mileages_mean

    return theta0_real, theta1_real


def main():
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("Error: data.csv not found")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: data.csv is corrupted or malformed")
        sys.exit(1)

    if 'km' not in df.columns or 'price' not in df.columns:
        print("Error: CSV must contain 'km' and 'price' columns")
        sys.exit(1)

    if df[['km', 'price']].isnull().any().any():
        print("Error: CSV contains null values in 'km' or 'price'")
        sys.exit(1)

    theta0, theta1 = train_model(df, learning_rate=0.001, iterations=1000)

    with open('theta.json', 'w') as f:
        json.dump({'theta0': theta0, 'theta1': theta1}, f)

    print(f"Training complete — theta0: {theta0:.4f}, theta1: {theta1:.4f}")


if __name__ == "__main__":
    main()