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


# Install Numpy
import numpy as np

def main():
    # Create a NumPy array
    data = np.array([1, 2, 3, 4, 5])

    # Perform basic operations
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)

    # Print the results
    print("Data:", data)
    print("Mean:", mean)
    print("Median:", median)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

if __name__ == "__main__":
    main()


