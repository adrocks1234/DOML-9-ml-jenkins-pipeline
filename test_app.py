import os
import joblib

def test_model_file_exists():
    assert os.path.exists("model.pkl"), "model.pkl file missing!"

def test_model_prediction():
    model = joblib.load("model.pkl")
    sample_input = [5.1, 3.5, 1.4, 0.2]
    prediction = model.predict([sample_input])
    assert len(prediction) == 1