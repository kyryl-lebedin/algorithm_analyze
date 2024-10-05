import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import time
from io import BytesIO
from IPython.display import display
import os
from datetime import datetime
from PIL import Image
import shutil
import string
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler, normalize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
from sklearn.ensemble import RandomForestClassifier



file = 'model/features3.csv'
df = pd.read_csv(file, header=None)
X = df.iloc[:, :-2].values  
y = df.iloc[:, -1].values 

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_normalized, y_encoded, test_size=0.2)

random_forest_model = RandomForestClassifier(n_estimators=500)

# Train the model
random_forest_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = random_forest_model.predict(X_test)

# Output probabilities for each class (optional)
y_pred_proba = random_forest_model.predict_proba(X_test)

joblib.dump(random_forest_model, 'algorithms/model/random_forest_model.pkl')


# Save the label encoder to decode predicted labels later
joblib.dump(label_encoder, 'algorithms/model/label_encoder.pkl')

joblib.dump(scaler, 'algorithms/model/scaler.pkl')