
"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
#solution3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Create a linear regression model
model = LinearRegression()
model.fit(price, demand)

# Get the regression coefficients
slope = model.coef_[0]
intercept = model.intercept_

# Revenue function: Revenue = Price * Demand
# Demand = slope * Price + intercept
# Revenue = Price * (slope * Price + intercept)

# Find the price that maximizes revenue
optimal_price = -intercept / (2 * slope)

# Predict demand at price = 52
price_52 = np.array([[52]])
demand_52 = model.predict(price_52)[0]

print(optimal_price, demand_52)
