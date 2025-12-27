import pandas as pd
import os

# create a sample Dataframe with column names.
data = {"Name":["Bob", "Alice", "John Doe"], 
        "Age":[12,32,45], 
        "City":["New York", "Delhi", "Luxemberg"]}

df = pd.DataFrame(data)

# # adding new row to df for d2
new_row1 = {"Name": "d2", "Age" : 20, "City" : "city1"}
df.loc[len(df.index)] = new_row1

# # adding new row to df for d3
new_row2 = {"Name": "d3", "Age" : 50, "City" : "city2"}
df.loc[len(df.index)] = new_row2

# Ensure the data directory exisits at root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Define the file path
file_path = os.path.join(data_dir, "Sample data csv")

# Save dataframe to a csv file, including column names
df.to_csv(file_path, index = False)

print (f"CSV file saved to {file_path}")
