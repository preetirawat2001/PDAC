import argparse
from pathlib import Path

import joblib
from sklearn.metrics import mean_squared_error, r2_score

from preprocessing import load_and_preprocess_discovery_data


def evaluate(data_path, model_path, output_path):
    artifact = joblib.load(model_path)
    model = artifact["model"]

    X, y, _, _ = load_and_preprocess_discovery_data(data_path)
    predictions = model.predict(X)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "metric,value\n"
        f"mse,{mean_squared_error(y, predictions):.6f}\n"
        f"r2,{r2_score(y, predictions):.6f}\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description="Evaluate PDAC drug response model.")
    parser.add_argument("--data", default="data/raw/pan_data.csv")
    parser.add_argument("--model", default="models/best_model.pkl")
    parser.add_argument("--output", default="results/tables/evaluation_metrics.csv")
    args = parser.parse_args()

    evaluate(Path(args.data), Path(args.model), Path(args.output))


if __name__ == "__main__":
    main()
