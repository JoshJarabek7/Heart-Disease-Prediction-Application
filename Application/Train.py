import pickle

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('Data/heart_disease.csv')

t = df['BMI']
cond = [(t.between(0, 18.5)), (t.between(18.5, 24.9)), (t.between(24.9, 29.9)), (t.between(29.9, 34.9)),
        (t.between(34.9, 100))]

labels = ['Underweight', 'Normal', 'Overweight', 'Obese', 'Extremely obese']

df['BMI_cat'] = np.select(cond, labels)

st = df['SleepTime']
cond = [(st.between(0, 6)), (st.between(6, 9)), (st.between(9, 24))]

labels = ['Low', 'Normal', 'High']
df['SleepTime_cat'] = np.select(cond, labels)

AgeCategory_mean = {'18-24': 21, '25-29': 27, '30-34': 32, '35-39': 37, '40-44': 42, '45-49': 47, '50-54': 52,
                    '55-59': 57, '60-64': 62, '65-69': 67, '70-74': 72, '75-79': 77, '80 or older': 80}

df['Mean_Age'] = df['AgeCategory'].apply(lambda x: AgeCategory_mean[x])

df.drop(columns=['AlcoholDrinking', 'MentalHealth', 'BMI', 'SleepTime', 'AgeCategory'], inplace=True)

# Label Encoding

encoded_df = df.copy()
le = LabelEncoder()
cols = ['HeartDisease', 'Smoking', 'Stroke', 'DiffWalking', 'Sex', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer']

for i in cols:
    encoded_df[i] = le.fit_transform(encoded_df[i])

le_1 = le.fit(encoded_df['GenHealth'])
le_1.classes_ = np.array(['Poor', 'Fair', 'Good', 'Very good', 'Excellent'])
encoded_df['GenHealth'] = le_1.transform(encoded_df['GenHealth'])

# One Hot Encoding

encoded_df = pd.concat([encoded_df, pd.get_dummies(encoded_df['Race'], prefix='Race', drop_first=False)], axis=1)
encoded_df = pd.concat([encoded_df, pd.get_dummies(encoded_df['Diabetic'], prefix='Diabetic', drop_first=False)], axis=1)
encoded_df = pd.concat([encoded_df, pd.get_dummies(encoded_df['BMI_cat'], prefix='BMI', drop_first=False)], axis=1)
encoded_df = pd.concat([encoded_df, pd.get_dummies(encoded_df['SleepTime_cat'], prefix='SleepTime', drop_first=False)], axis=1)

encoded_df.drop(columns=['Race', 'Diabetic', 'BMI_cat', 'SleepTime_cat'], axis=1, inplace=True)

X = encoded_df.drop(columns=['HeartDisease'], axis=1)
Y = encoded_df['HeartDisease']

col = X.columns

sc = StandardScaler()

scaler = sc.fit(X)
X_scaled = scaler.transform(X)

X_train = pd.DataFrame(X_scaled, columns=col)

joblib.dump(scaler, 'Application/scaler.pkl')

model_rf = RandomForestClassifier(random_state=42)

model_rf.n_estimators = 500
model_rf.class_weight = "balanced"
model_rf.max_depth = 30
model_rf.min_samples_split = 30
model_rf.min_samples_leaf = 24

model_rf.fit(X_train, Y)

joblib.dump(model_rf, 'Application/model_rf.pkl')