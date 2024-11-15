import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./datasets/cleaned_data.csv', skipinitialspace=True)

# Converting 'education-num' to numeric and ensuring it is sorted numerically
df['education-num'] = pd.to_numeric(df['education-num'], errors='coerce')
df.sort_values('education-num', inplace=True)
print(f"Number of rows used for analysis: {len(df)}")

# Grouping
education_sex_income = df.groupby(['education-num', 'sex', 'income']).size().unstack(fill_value=0)

# Calculating the total counts and percentage of '>50K' for each group
education_sex_income['Total'] = education_sex_income['<=50K'] + education_sex_income['>50K']
education_sex_income['>50K%'] = (education_sex_income['>50K'] / education_sex_income['Total']) * 100

education_sex_income = education_sex_income.reset_index()

# Pivot to maek 'sex' as columns
pivot_df = education_sex_income.pivot(index='education-num', columns='sex', values='>50K%')

# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(data=pivot_df)
plt.title('Percentage of Individuals Earning >50K by Education Level and Sex')
plt.xlabel('Education Number')
plt.ylabel('Percentage of >50K Income')
plt.xticks(pivot_df.index) 
plt.grid(True)
plt.legend(title='Sex')
plt.savefig('education_gender_income_combined.png')
plt.show()

genders = pivot_df.columns.tolist()

# Iterating over each gender to create separate plots
for gender in genders:
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        x=pivot_df.index, 
        y=pivot_df[gender], 
        marker='o', 
        label=gender, 
        color='skyblue' if gender == 'Male' else 'salmon'
    )
    plt.title(f'Percentage of Individuals Earning >50K by Education Level for {gender}')
    plt.xlabel('Education Number')
    plt.ylabel('Percentage of >50K Income')
    plt.xticks(pivot_df.index)
    plt.ylim(0, pivot_df[gender].max() + 5) 
    plt.grid(True)
    plt.legend(title='Sex')
    plt.tight_layout()
  
    plt.savefig(f'education_income_{gender.lower()}.png')
    plt.show()