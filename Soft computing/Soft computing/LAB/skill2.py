import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
df = pd.read_csv('customer_data.csv')
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary')
plt.show()
df.dropna(inplace=True)  # Drop rows with missing values
# Or, fill missing values with mean
df.fillna(df.mean(), inplace=True)
label_encoder = LabelEncoder()
df['Country_Encoded'] = label_encoder.fit_transform(df['Country'])
# Or, use One-Hot Encoding for nominal data
df = pd.get_dummies(df, columns=['Country'], drop_first=True)
X = df.drop('Purchase', axis=1)  # Features
y = df['Purchase']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
