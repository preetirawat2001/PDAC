import argparse
from pathlib import Path

import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from model import get_stacked_ensemble_model
from preprocessing import load_and_preprocess_discovery_data


def train(data_path, model_path, metrics_path):
    X, y, feature_cols, scaler = load_and_preprocess_discovery_data(data_path)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = get_stacked_ensemble_model()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {"model": model, "scaler": scaler, "feature_cols": feature_cols},
        model_path,
    )

    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(
        "metric,value\n"
        f"mse,{mean_squared_error(y_test, predictions):.6f}\n"
        f"r2,{r2_score(y_test, predictions):.6f}\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description="Train PDAC drug response model.")
    parser.add_argument("--data", default="data/raw/pan_data.csv")
    parser.add_argument("--model", default="models/best_model.pkl")
    parser.add_argument("--metrics", default="results/tables/train_metrics.csv")
    args = parser.parse_args()

    train(Path(args.data), Path(args.model), Path(args.metrics))


if __name__ == "__main__":
    main()
