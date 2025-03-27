#######################################################################################################################################################
# 
# Name:Uruz Ahmad
# SID:750003673
# Exam Date:27/03/2025
# Module:programming for business analytics
# Github link for this assignment:https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-UruzAhmad  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []
#solution1
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Allocated keys based on SID: First digit (7) and last digit (3)
allocated_keys = [7, 3]

# Given customer feedback text
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."""

# Initialize an empty list to store (start, end) positions
my_list = []

# Loop through allocated keys to find their corresponding words
for key in allocated_keys:
    word = key_comments.get(key)  # Get the word for the key
    if word:
        start_pos = customer_feedback.find(word)  # Find the start position
        if start_pos != -1:
            end_pos = start_pos + len(word)  # Calculate the end position
            my_list.append((start_pos, end_pos))  # Append tuple to list

# Output the result
print(my_list)
#outout:[(129, 136), (88, 94)]
##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
#solution2
# Define function to calculate Operating Profit Margin
def operating_profit_margin(revenue, operating_income):
    if revenue == 0:
        return 0  # Avoid division by zero
    return (operating_income / revenue) * 100

# Define function to calculate Revenue per Customer
def calculate_revenue_per_customer(total_revenue, total_customers):
    if total_customers == 0:
        return 0  # Avoid division by zero
    return total_revenue / total_customers

# Define function to calculate Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    if total_customers == 0:
        return 0  # Avoid division by zero
    return (lost_customers / total_customers) * 100

# Define function to calculate Average Order Value
def average_order_value(total_revenue, total_orders):
    if total_orders == 0:
        return 0  # Avoid division by zero
    return total_revenue / total_orders

# Given values based on ID
first_two_digits = 75
last_two_digits = 73

total_revenue = first_two_digits * 1000  # Example assumption: Revenue in thousands
operating_income = last_two_digits * 500  # Example assumption: Income in hundreds
lost_customers = last_two_digits  # Example assumption for churned customers
total_customers = first_two_digits * 10  # Example assumption for total customers
total_orders = first_two_digits + last_two_digits  # Example assumption for total orders

# Call functions and print results
operation_profit_margin = operating_profit_margin(total_revenue, operating_income)
revenue_per_customer = calculate_revenue_per_customer(total_revenue, total_customers)
customer_churn_rate_value = customer_churn_rate(lost_customers, total_customers)
average_order_value_result = average_order_value(total_revenue, total_orders)

print("Operating Profit Margin:", operation_profit_margin, "%")
print("Revenue per Customer:", revenue_per_customer)
print("Customer Churn Rate:", customer_churn_rate_value, "%")
print("Average Order Value:", average_order_value_result)

#Output:perating Profit Margin: 48.66666666666667 %
#Revenue per Customer: 100.0
#Customer Churn Rate: 9.733333333333333 %
#Average Order Value: 506.7567567567568
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

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
#output Predicted Demand at £52: 158.17272727272726
Optimal Price for Maximum Revenue: £45

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
#solution4
# Importing necessary libraries
import random
import matplotlib.pyplot as plt

# Asking the user to enter their student ID as the maximum value
max_value = int(input("Enter your Student ID: "))

# Generate 100 random numbers between 1 and the student ID number
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the random numbers using matplotlib to visualize data clearly
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

# Adding title and labels to make the plot understandable
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")

# Adding a legend to describe the plotted data
plt.legend()

# Adding gridlines for better readability of the plot
plt.grid(True)

# Displaying the final plotted chart
plt.show()



