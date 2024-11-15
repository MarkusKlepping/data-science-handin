import pandas as pd
import numpy as np

column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

df = pd.read_csv('./datasets/adult.data', names=column_names, header=None, skipinitialspace=True)

# Checking for null values
print(df.isnull().sum())

# Checking for and handling duplicates
print("Number of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
#making sure that thea actually got removed
print("Number of duplicate rows after removal:", df.duplicated().sum())

print("Unique workclass values:", df['workclass'].unique())

# Check whether there are any missing values in the the columns 
print("Missing 'income' placeholders:", (df['income'] == '?').sum())
print("Missing 'sex' placeholders:", (df['sex'] == '?').sum())
print("Missing 'education-num' placeholders:", (df['education-num'] == '?').sum())
print("Missing 'marital-status' placeholders:", (df['marital-status'] == '?').sum())

# Replace '?' with NaN
df['native-country'] = df['native-country'].replace('?', np.nan)
df['occupation'] = df['occupation'].replace('?', np.nan)

# Save the cleaned data to a new CSV file 
df.to_csv('cleaned_data.csv', index=False)

numerical_cols = ['age', 'education-num', 'hours-per-week', 'capital-gain', 'capital-loss']


# -------------------- Descriptive Statistics to get an overview of the Dataset -------------------- #

# Compute descriptive statistics
numerical_stats = df[numerical_cols].describe().transpose()
numerical_stats['mode'] = df[numerical_cols].mode().iloc[0]
print("Overview for Numerical Columns:")
print(numerical_stats)

# Selecting categorical columns that are important for me
categorical_cols = ['sex', 'marital-status', 'income', "education-num"]

# Compute frequency distribution
for col in categorical_cols:
    freq = df[col].value_counts(dropna=False)
    percentage = df[col].value_counts(normalize=True, dropna=False) * 100
    freq_df = pd.DataFrame({'Count': freq, 'Percentage': percentage.round(2)})
    print(f"\nOverviwe for Column: {col}")
    print(freq_df)
