import pandas as pd
from joblib import load
import os

MODEL_PATH = "artifacts/nids_model.joblib"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Train the model first.")
    return load(MODEL_PATH)

def predict_sample(sample_dict):
    """
    sample_dict: Python dict with feature_name: value
    Example (keys must match your training CSV columns):
    {
        "duration": 0,
        "protocol_type": "tcp",
        "service": "http",
        "flag": "SF",
        "src_bytes": 181,
        "dst_bytes": 5450,
        ...
    }
    """
    model = load_model()
    df = pd.DataFrame([sample_dict])
    pred = model.predict(df)[0]
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)[0]
    return pred, proba

if __name__ == "__main__":
    # Example dummy sample; replace keys/values according to your dataset columns
    example_sample = {
        "duration": 0,
        "protocol_type": "tcp",
        "service": "http",
        "flag": "SF",
        "src_bytes": 181,
        "dst_bytes": 5450,
    }

    label, proba = predict_sample(example_sample)
    print("Predicted label:", label)
    if proba is not None:
        print("Class probabilities:", proba)
