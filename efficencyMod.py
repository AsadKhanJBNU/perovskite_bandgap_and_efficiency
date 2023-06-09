import os
import joblib


os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="5"

bandgap_model = joblib.load('Saved_Models/CatBoostRegressorEfficiency.sav')