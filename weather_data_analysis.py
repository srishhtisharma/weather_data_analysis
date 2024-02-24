# -*- coding: utf-8 -*-
"""weather_data_analysis.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qfc8621Y0uhmTZBnfnP0ikCotHat-_or
"""

#Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Loading the dataset
df= pd.read_csv('/weather.csv')
print(df)

#Shows the first N rows in the data, default N=5
df.head()
#df[:366]

"""**1. Data exploration** is the initial step in the data analysis process, where you examine and understand the structure, content, and basic statistics of the dataset.

In Python, the **pandas** library provides useful functions for data exploration.
"""

# Data Exploration(Displaying the information about the dataset)
print("Data Exploration:")
print(df.info())

"""**2. Data visualization** is a crucial aspect of data analysis, helping to uncover patterns, trends, and relationships within the dataset. Pair plots are a type of visualization that displays scatterplots. They are especially useful for identifying potential correlations and understanding the distribution of data.

In Python, the **seaborn** library provides a convenient function for creating pair plots.
"""

# Data Visualization
print("\nData Visualization:")
sns.pairplot(df)
plt.show()

"""**3. Feature engineering** is the process of creating new informative features from existing ones.
So, we are creating a new feature 'rainy_day' based on the 'Rainfall' column

If 'Rainfall' > 0, it's a rainy day (1), otherwise not (0)
"""

# Feature Engineering
print("\nFeature Engineering")
df['rainy_day'] = np.where(df['Rainfall'] > 0, 1, 0)

"""**4. Data analysis** involves examining and interpreting data to uncover patterns, trends, and insights. It includes calculating statistics, identifying relationships between variables, and drawing meaningful conclusions from the data.

Here, it focuses on calculating the **mean** and **standard deviation** of the 'Rainfall' column.
"""

# Data Analysis
mean_rainfall = df['Rainfall'].mean()
std_rainfall = df['Rainfall'].std()

print("\nData Analysis:")
print(f"Mean Rainfall: {mean_rainfall}")
print(f"Standard Deviation of Rainfall: {std_rainfall}")

"""
**5. Data visualization
(Part 2)** is the graphical representation of data to reveal patterns, trends, and insights. It involves creating visual elements such as charts, graphs, and plots to make complex data more understandable and accessible.

Here, we are visualizing the distribution of 'MaxTemp' and 'MinTemp'"""

# Data Visualization

print("\nData Visualization:")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='MaxTemp', bins=20, kde=True, color='blue', label='MaxTemp')
sns.histplot(data=df, x='MinTemp', bins=20, kde=True, color='red', label='MinTemp')
plt.title('Distribution of MaxTemp and MinTemp')
plt.legend()
plt.show()

"""**6. Advanced analysis** involves more sophisticated and complex techniques applied to understand patterns, relationships, or make predictions in the data.

Here, **linear regression** is used for predicting rainfall based on the minimum temperature (MinTemp).
"""

# Advanced Analysis
#Rainfall prediction using Linear Regression
# Using 'MinTemp' as the predictor variable
X = df[['MinTemp']]
y = df['Rainfall']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)

print("\nAdvanced Analysis:")
print(f"Linear Regression Mean Squared Error: {mse}")

"""**7. Conclusions and Insights:** We are determining the correlation between 'MaxTemp' and 'Rainfall'

"""

correlation_maxtemp_rainfall = df['MaxTemp'].corr(df['Rainfall'])

print("\nConclusions and Insights:")
print(f"Correlation between MaxTemp and Rainfall: {correlation_maxtemp_rainfall}")