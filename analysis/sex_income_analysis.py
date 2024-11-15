import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_csv('./datasets/cleaned_data.csv', skipinitialspace=True)

# Group data by sex and income and count occurrences
income_by_gender = df.groupby(['sex', 'income']).size().unstack()

# Calculating proportions of income categories witini each gender
income_proportions = income_by_gender.div(income_by_gender.sum(axis=1), axis=0)

print(income_proportions)

# Plotting the pie charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

for i, (gender, data) in enumerate(income_proportions.iterrows()):
    axs[i].pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    axs[i].set_title(f'Income Distribution for {gender}')

plt.suptitle('Income Distribution by Gender')
plt.savefig("sex_income_analysis.png")
plt.show(block=False)


# Preparing contingency table for the chi-squared test
contingency_table = income_by_gender.fillna(0).values

chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f'Chi-squared statistic: {chi2}')
print(f'p-value: {p}')

#using a significance level of 0.05,since this is a common threshold
if p < 0.05:
    print("here is a statistically significant association between gender and income level.")
else:
    print("No evidence of a statistically significant association between gender and income level.")
