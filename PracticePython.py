import pandas as pd
#create dataframe
data = { 
    'Name': ['Aishwarya', 'Aayusha', 'Gaurav', 'Radha','chintu'],
    'Age': [22, 23, 20, 16],
    'Salary': [90000, 700000, 650000, 100000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df, "\n")

#Print its shape and column names
print("Shape of DataFrame:", df.shape)
print("Column Names:", df.columns.tolist(), "\n")

#Print the first 3 rows
print("First 3 Rows:")
print(df.head(3), "\n")

#DataFrame info
print("DataFrame Info:")
df.info()
print()

#Statistical summary
print("Statistical Summary:")
print(df.describe(), "\n")

#Print only 'Age' column
print("Age Column:")
print(df['Age'], "\n")

#Print the first row using iloc
print("First Row (iloc):")
print(df.iloc[0], "\n")

#Print specific row using loc
print("Row for Index 2 (loc):")
print(df.loc[2], "\n")

#Add a missing value (None) in Age column 
df.loc[1, 'Age'] = None
print("After Adding Missing Value:")
print(df, "\n")

#Detect missing values using isnull()
print("Missing Values Detected: ")
print(df.isnull(), "\n")

#Fill missing values with mean of the column
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
print("After Filling Missing Value with Mean:")
print(df, "\n")

#Drop rows with missing values 
df_dropped = df.dropna()
print("After Dropping Rows with Missing Value:")
print(df_dropped, "\n")

#Sort the DataFrame by 'Salary' in descending order
df_sorted = df.sort_values(by='Salary', ascending=False)
print("Sorted by Salary (Descending):")
print(df_sorted, "\n")

#Filter rows where Age > 30
print("Rows where Age > 30:")
print(df[df['Age'] > 30], "\n")


#Filter rows where Salary < 60000
print("Rows where Salary < 60000:")
print(df[df['Salary'] < 60000], "\n")

#Compute mean Age and mean Salary
print("Mean Age and Mean Salary:")
print("Mean Age:", df['Age'].mean())
print("Mean Salary:", df['Salary'].mean(), "\n")

#Count how many times each Age appears using value_counts()
print("Age Value Counts:")
print(df['Age'].value_counts(), "\n")

#Group by Age and compute mean Salary for each group
print("Mean Salary by Age:")
print(df.groupby('Age')['Salary'].mean())







