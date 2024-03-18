# -*- coding: utf-8 -*-
"""LVADSUSR125-Swathi M-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QHcPU_RvgEqnIGB9QxektSXgafK8IaIq
"""

#1
import numpy as np
rgb_image=np.array([[[255,0,0],[0,255,0],[0,0,255]],[[255,255,0],[255,0,255],[0,255,255]],[[127,127,127],[200,200,200],[50,50,50]]])
print(rgb_image)
def rgb_to_grayscale(rgb_image):

    coefficients = np.array([0.2989, 0.5870, 0.1140])

    grayscale_image = np.dot(rgb_image, coefficients)

    return grayscale_image
rgb_image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                      [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                      [[127, 127, 127], [200, 200, 200], [50, 50, 50]]])
grayscale_image = rgb_to_grayscale(rgb_image)
print(grayscale_image)

#2
a=np.array([[1,2,3],[3,4,5],[4,5,6]])
def normalize(a):
    b = np.zeros(9).reshape(3,3)
    for i in range(len(a)):
        for j in range(len(a[i])):
           b[i][j] = (a[i][j] - a[i].mean())/(a[i].std())
    return b
normalize(a)

#3
data = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])
flattened_data = np.array([sensor.flatten() for sensor in data])
concatenated_data = np.concatenate(flattened_data)
num_sensors = data.shape[0]
num_elements_per_sensor = data.shape[1] * data.shape[2]
reshaped_data = concatenated_data.reshape(num_sensors, num_elements_per_sensor)

print("Original data:")
print(data)
print("\nReorganized data:")
print(reshaped_data)

#4
scores = np.array([
    [80, 85, 90, 95],
    [70, 75, 80, 85],
    [90, 85, 80, 75]
])

firstgame_scores = scores[:, 0]
lastgame_scores = scores[:, -1]
improve = lastgame_scores - firstgame_scores
for i, imp in enumerate(improve):
    print(f"Athlete {i+1} improvement: {imp}")

#5
scores = np.array([
    [85, 90, 92, 88, -1],
    [75, 80, 85, -1, 78],
    [90, 85, -1, 88, 82],
    [70, -1, 75, 80, 72]
])

last_three_subjects_indices = slice(-3, None)
selected_subjects = scores[:, last_three_subjects_indices]
valid_scores = selected_subjects[selected_subjects != -1]
average_scores = np.mean(valid_scores.reshape(-1, 3), axis=1)
for i, avg_score in enumerate(average_scores):
    print(f"Student {i+1} average score in the last three subjects: {avg_score:.2f}")

#6
def apply_adjustment_factors(city_temperatures, adjustment_factors):

    adjusted_factors = adjustment_factors.reshape(1, -1)
    adjusted_temperatures = city_temperatures * adjusted_factors

    return adjusted_temperatures
city_temperatures = np.array([
    [20, 25, 30, 28],
    [15, 18, 22, 20],
    [10, 12, 14, 16]
])
adjustment_factors = np.array([0.95, 0.98, 1.05, 1.02])

adjusted_temperatures = apply_adjustment_factors(city_temperatures, adjustment_factors)

print("Original temperatures:")
print(city_temperatures)
print("\nAdjusted temperatures:")
print(adjusted_temperatures)

#7
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, 35, 40, 45, 50, 55],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']
}
final = [(data['Name'][i], data['City'][i]) for i in range(len(data['Name']))
                 if data['Age'][i] < 45 and data['Department'][i] != 'HR']
for name, city in final:
    print(f"Name: {name}, City: {city}")

#8
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
df = pd.DataFrame(data)
fruit_df = df[df['Category'] == 'Fruit']
average_price = fruit_df['Price'].mean()
above_average_df = fruit_df[fruit_df['Price'] > average_price]
potential_candidates = above_average_df[above_average_df['Promotion'] == False]
print("Potential candidates for promotions among 'Fruit' category products:")
print(potential_candidates)

#9
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}
employee_df = pd.DataFrame(employee_data)
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}
project_df = pd.DataFrame(project_data)
merged_df = pd.merge(project_df, employee_df, on='Employee', how='left')
merged_df['Manager'].fillna('Unassigned', inplace=True)
department_overview = merged_df.groupby(['Department', 'Manager']).agg({'Project': list}).reset_index()
print("Department Overview:")
print(department_overview)

#10
data = {
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales': [70000, 50000, 30000, 40000, 60000]
}
df = pd.DataFrame(data)
avg_sales_per_salesperson = df.groupby(['Department', 'Salesperson'])['Sales'].mean().reset_index()
avg_sales_per_department = avg_sales_per_salesperson.groupby('Department')['Sales'].mean().reset_index()
ranked_departments = avg_sales_per_department.sort_values(by='Sales', ascending=False)
print("Average sales per salesperson in each department:")
print(avg_sales_per_salesperson)
print("\nAverage sales per department:")
print(avg_sales_per_department)
print("\nRanked departments based on average sales:")
print(ranked_departments)
