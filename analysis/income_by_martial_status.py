import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./datasets/cleaned_data.csv', skipinitialspace=True)

# Encoding the income variable to be numeric
df['income_num'] = df['income'].apply(lambda x: 1 if x == '>50K' else 0)

# Calculating the proportion of individuals earning >50K for each martial status category
income_by_marital_status = df.groupby('marital-status')['income_num'].mean().reset_index()

# Renameing for clarity
income_by_marital_status.columns = ['Marital Status', 'Proportion Earning >50K']

print(income_by_marital_status)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=income_by_marital_status,
    x='Marital Status',
    y='Proportion Earning >50K',
    palette='viridis'
)
plt.title('Proportion of Individuals Earning >50K by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Proportion Earning >50K')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("income_by_martial_status.png")
plt.show()

