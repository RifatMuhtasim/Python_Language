print("Hello World") 
print("Khandokar Rifat Muhtasim, Chief Technical Officer at WASITAV LIMITED")


# Install Pandas on Linux - sudo apt-get install python3-pandas
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28]
       }
df = pd.DataFrame(data)
print(df.head())
print(df['Name'])  # Access the 'Name' column


# Python Indentation
if 5 > 2:
        print("Number 5 is Greater then the 2")

