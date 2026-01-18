# Network Intrusion Detection System (ML)

Machine Learning based Network Intrusion Detection System using the NSL-KDD dataset.  
Includes data preprocessing, model training, evaluation metrics, and a prediction script for new network traffic samples.

## Features
- Loads NSL-KDD train/test CSV files and applies basic preprocessing (label mapping, encoding, scaling).
- Trains a Random Forest classifier to detect normal vs attack traffic.
- Evaluates the model using accuracy, precision, recall, and F1-score.
- Saves the trained model and scaler for later use.
- Provides a simple prediction script to classify new samples.

## How to run

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
  
   pip install -r requirements.txt
   Download NSL-KDD CSV files (e.g., KDDTrain+.csv, KDDTest+.csv) and place them in the data/ folder.

Train and evaluate the model:

python nids_train.py
Run a test prediction:
python nids_predict.py
