# Data Science Basics Handin

## Overview

This project aims to analyze a Dataset about [Adult Incomes in the United States](https://www.kaggle.com/datasets/danielbethell/adult-incomes-in-the-united-states) for the SE_42 Data Science Basics Module

## Dataset Description

The dataset contains demographic and employment information. Here is a brief description of the dataset attributes:

- **Age**: The age of the individual.
- **Workclass**: The sector of employment (e.g., State-gov, Private).
- **fnlwgt**: The number of people the census believes the entry represents (final weighting).
- **Education**: The highest level of education achieved (e.g., Bachelors, Masters).
- **Education-Num**: The highest level of education in numerical form.
- **Marital Status**: Marital status of the individual (e.g., Never-married, Married-civ-spouse).
- **Occupation**: The general type of occupation of the individual.
- **Relationship**: Represents what this individual is relative to others (e.g., Husband, Not-in-family).
- **Race**: The race of the individual.
- **Sex**: The gender of the individual.
- **Capital-Gain**: Capital gains recorded.
- **Capital-Loss**: Capital losses recorded.
- **Hours-per-week**: Number of hours worked per week.
- **Native-Country**: Country of origin for the individual.
- **Income**: The income class (<=50K or >50K).

## Files in the Repository

- **adult.data**: The original dataset
- **cleaned_data.csv**: The dataset file containing all the above attributes, created by the main.py file
- **main.py**: Python file that performs some cleaning and checking of data quality
- **education_income_analysis.py**:
- **sex_income_analysis.py**:
- **income_by_martial_status.py**:

- **plots folder**: Which contains all of the generated Plots of this Repo in .png files

## Requirements

The following libraries are required to run the analysis and the named version was used to develop:

```
numpy==2.1.3
pandas== 2.2.3
matplotlib==3.9.2
scikit-learn== 1.5.2

Install them using

pip install -r requirements.txt.

```
