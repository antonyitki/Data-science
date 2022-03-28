# -*- coding: utf-8 -*-
"""Coursework1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nlqlRu3JS6CckxkoQuazVZE0dzSLns4U
"""

###############################################
'''

Coursework 1, Data Science with Kimia Aksir 
Year 2, term 2nd
YIT19488399, Tony
Delivery date: Thursday, 17 of March 2022


'''
##############################################

#read uploaded file to colab (upload .csv file to content folder in colab)
#https://www.codegrepper.com/code-examples/python/how+to+read+csv+file+in+google+colab
import numpy as np
import pandas as pd

df = pd.read_csv("ABC-CompanyData.csv")

#see .csv file in colab environment
df

#Generate descriptive statistics
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
df.describe(include='all')

#NaN = Not A Number

#Understand the basic information about the .csv file
df.info()

# To check null values row-wise
#Pandas has isnull( ) for detecting null values in a dataframe.
#0 = no missing values. 0 = column with values in all rows.
df.isnull().sum()

"""**Task 1.**

Ready for operations about measure central tendency.
"""

#Mean:

#average age of people in a .csv file
print(df['age'].mean())
#average account balance in a bank for people in the file
print(df['balance'].mean(), "USD")
#average duration of the term of the loan
print(df['duration'].mean(), "days")
#average account balance by each age
average_lalance_by_age = df.groupby(by="age")["balance"].mean()
print(average_lalance_by_age)
#number of people grouped by 3 maritil status
count_people_by_maritial_status = df["marital status"].value_counts()
print(count_people_by_maritial_status)

#average balance by eduacation status and maritial status at the same time
average_balance_by_eduaction_and_maritial_status = df.groupby(["education", "marital status"])["balance"].mean()
print(average_balance_by_eduaction_and_maritial_status)

#the mean method is applied to each column containing numerical columns
df.groupby("age").mean()

#plotings of mean
import matplotlib.pyplot as plt
import numpy as np

plt.title('Average balance in bank account by ages (18 to 95)')
plt.xlabel('Age')
plt.ylabel('Average balance')
plt.plot(average_lalance_by_age)
plt.show()

#The groupby output will have an index or multi-index on rows corresponding to your chosen grouping variables.
#To avoid setting this index, pass “as_index=False” to the groupby operation.
df.groupby('age', as_index=False).agg({"duration": "mean"})

'''
Groupby output format – Series or DataFrame?
The output from a groupby and aggregation operation varies between Pandas Series and Pandas Dataframes, which can be confusing for new users. As a rule of thumb, if you calculate more than one column of results, your result will be a Dataframe. For a single column of results, the agg function, by default, will produce a Series.

You can change this by selecting your operation column differently:
'''
# produces Pandas Series
df.groupby('loan')['duration'].mean()

# Produces Pandas DataFrame
df.groupby('loan')[['duration']].mean()

#Calculations for median:
import numpy as np

print(np.median(df["age"]), "is the median for AGE column")
print(np.median(df["balance"]), "is the median for BALANCE column")
print(np.median(df["day"]), "is the median for DAY column")
print(np.median(df["duration"]), "is the median for DURATION column")
print(np.median(df["campaign"]), "is the median for CAMPAIGN column")
#next statement will NOT work because NOT numeric value
#print(np.median(df["month"]))

#same median calculation with pandas library
import pandas as pd  
print("\nVerification of previous calculations with different library (PANDAS)")
print(df['age'].median())
print(df['balance'].median())
print(df['day'].median())
print(df['duration'].median())
print(df['campaign'].median(), "\n")

#all previous 2 blocks of calculation in one line and for verification
print(df.median())

#special median calculation. Median by group.
print("median values grouped by campaign:")
print(df.groupby('campaign').median())
print("\nmedian values grouped by maritial status:")
print(df.groupby('marital status').median())
print("\nmedian values grouped by educational status:")
print(df.groupby('education').median())
print("\nmedian values grouped by default")
print(df.groupby("default").median())

#count number of elements for each column.
#Counting the frequency of occurrences in a column using Pandas groupby Method
print("Number of values for each quantitative value column, classified by educational status")
df.groupby("education").count()

print("Number of values for each quantitative value column, classified by deposit value (binary)")
df.groupby("deposit").count()

#percentages of different values in a single column.
print("Percentage of values for eduaction column")
print(df['education'].value_counts(normalize=True))
print("\n")
print("Percentage of values for education column with % output")
print(df['education'].value_counts(normalize=True)*100)
print("\n")
print("Percentage of values for loan column")
print(df['loan'].value_counts(normalize=True)*100)
print("\n")
print("Percentage of values for deposit column")
print(df['deposit'].value_counts(normalize=True)*100)

#Count of unique values in each column
print(df.nunique())

#Calculations of mode for all 13 columns:

print("Most frequent value for age column: years old")
print(df['age'].mode()) 
print("\nMost frequent value for role column:")
print(df['role'].mode()) 
print("\nMost frequent value for maritial status column:")
print(df['marital status'].mode()) 
print("\nMost frequent value for education column:")
print(df['education'].mode()) 
print("\nMost frequent value for default column:")
print(df['default'].mode()) 
print("\nMost frequent value for balance column: USD")
print(df['balance'].mode()) 
print("\nMost frequent value for housing possesion column:")
print(df['housing'].mode()) 
print("\nMost frequent value for loan column:")
print(df['loan'].mode()) 
print("\nMost frequent value for day column: st, nd, rd, th")
print(df['day'].mode()) 
print("\nMost frequent value for month column:")
print(df['month'].mode()) 
print("\nMost frequent value for duration of loan column: DAYS")
print(df['duration'].mode()) 
print("\nMost frequent value for campaign column:")
print(df['campaign'].mode()) 
print("\nMost frequent value for deposit column:")
print(df['deposit'].mode())

#previous block of code in one line (build in function, from pandas library)
df.mode()

"""**TASK2.**

Range, Variance and Standard Deviation (“Measure of Spread/Dispersion”)

"""

#Calculations of range (The difference between the biggest and the smallest number):

# Calculate max min difference
print("######MAXIMUM values######")
print(df.max(numeric_only=True))
print("\n######MINIMUM values######")
print(df.min(numeric_only=True))
print("\nRange for numerical columns:")
print(df.max(numeric_only=True) - df.min(numeric_only=True))

#maximum values for all columns in .csv file basedon EDUCATION attribute. Necesary for range calculation.
df.groupby('education').max()

#minimum values for all columns in .csv file basedon EDUCATION attribute. Necesary for range calculation.
df.groupby('education').min()

#range calculation for numerical values based on education.
(df.groupby('education').max(numeric_only=True) - df.groupby('education').min(numeric_only=True))

#find max value of DURATION of the loan, grouped by EDUCATION
print(df.groupby('education')['duration'].max())
#find min value of DURATION of the loan, grouped by EDUCATION
print(df.groupby('education')['duration'].min())
print("\nRange for duration of loan based on educational status")
print(df.groupby('education')['duration'].max() - df.groupby('education')['duration'].min())

#Range for housing group:
(df.groupby('housing').max(numeric_only=True) - df.groupby('housing').min(numeric_only=True))

#Variance calculation. Simple ones.
print(df['balance'].std(), "for balance")
print(df['age'].std(), "for only ages")
print(df['duration'].std(), "for duration in days")

#standard deviation based on attribute housing
df.groupby(['housing']).std()

#More comolicated calculation for standard deviation: housing and loan atributes(qualitative both, binary).
df.groupby(['housing',"loan"]).std()

#Standard deviation based on 3 attributes.
df.groupby(['housing',"loan", "education"]).std()

#Calculation of variance based on previous calculation s of standard deviation.
print(df['balance'].var(), "for balance")
print(df['age'].var(), "for only ages")
print(df['duration'].var(), "for duration in days")
print("\nMore advanced ")
print(df.groupby(['housing']).var())
print(df.groupby(['housing',"loan"]).var())
print(df.groupby(['housing',"loan", "education"]).var())

"""**TASK 3**

PMF. Probability Mass Function.

Age is the discrete variable.
"""

!pip install empiricaldist

from empiricaldist import Pmf, Cdf
from scipy.stats import norm
age = df['age']
# Compute the PMF for age
print(Pmf.from_seq(age, normalize=False))
print("\nMaximum and Minimum number of times same age is in the column age")
print(max(Pmf.from_seq(age, normalize=False)))
print(min(Pmf.from_seq(age, normalize=False)))

# Compute the PMF for year
print(Pmf.from_seq(age, normalize=True))
print("\nThe sum of all PMF probabilities based on the number of appearances in the age column: ")
print(sum(Pmf.from_seq(age, normalize=True)))
print("\nMaximum PMF value")
print(max(Pmf.from_seq(age, normalize=True)))
print("Minimum PMF value")
print(min(Pmf.from_seq(age, normalize=True)))

# Select the age column
age = df['age']
# Make a PMF of age
pmf_age = Pmf.from_seq(age, normalize = False)
# Plot the PMF
pmf_age.bar(label='age')
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')

# Select the age column
age = df['age']
# Make a PMF of age
pmf_age = Pmf.from_seq(age, normalize = True)
# Plot the PMF
pmf_age.bar(label='age')
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')

#histogram age (NOT PMF ages)
age = df['age']
plt.hist(age.dropna(), label='age')
plt.show()

from os import minor
from functools import total_ordering
#https://www.dataquest.io/blog/python-counter-class/
from scipy.stats import binom
from collections import Counter


class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.
        The result is the distribution of sums of values from thetwo distributions.
        other: Pmf
        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def __hash__(self):
        """Returns an integer hash value."""
        return id(self)

    def __eq__(self, other):
        return self is other

    def render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))


# Get a series of unique values in column 'Age' of the dataframe --> empDfObj['Age'].unique()
d6 = Pmf(df['age'].unique())
d6.normalize()
print(d6)
print(d6.values())

#Total number of different ages is 76
print(0.013157894736842105 *76)
print(0.013157894736842105 * 100, "% of PMF for each age individually")

#same as previous code, but in one line
from empiricaldist import Pmf
die = Pmf(1/76, df['age'].unique())
die

#from lab2 with Kimia
#for function binom(n=10,p=0.013157894736842105), where, n is the number of trials and p holds the probability of success
from scipy import stats
X = stats.binom(10, 0.013157894736842105) # Declare X to be a binomial random variable
(X.pmf(3))          # P(X = 3) which implies we are calculating the mass function for the third trial

print(X.pmf(6))
print(X.pmf(7))
print(X.pmf(8))
print(X.pmf(9))
print(X.pmf(10))
print(X.pmf(11))
print(X.pmf(999))

"""**TASK 4**

PDF.

Balance is the continuous variable (interval).
"""

print(df.loc[:,"balance"])
print("##################################")
print(df['balance'])

#https://www.adamsmith.haus/python/answers/how-to-return-a-column-of-a-pandas-dataframe-as-a-list-in-python
print(df["balance"].tolist())

# unique values in column "balance"
print(df['balance'].unique().tolist())
print(df["balance"].values.tolist())
print(df["balance"].drop_duplicates().tolist())
# count of unique values 
print(df['balance'].nunique())
# value counts of each unique value
print(df['balance'].value_counts())
print(df["balance"].value_counts().tolist())

print(df["balance"].value_counts(normalize=False).tolist())
print(df["balance"].value_counts(normalize=True).tolist())

df['balance'].describe()

import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(df['balance'],shade=True)
plt.show()

print(sns.distplot(df['balance']))

#https://medium.com/analytics-vidhya/kde-vs-pdf-in-python-53ffbf578995
from scipy import stats
data = df['balance']
loc = data.mean()
scale = data.std()
pdf = stats.norm.pdf(data, loc=loc, scale=scale)
print(pdf.tolist())

fig, ax = plt.subplots()
ax = sns.lineplot(x=data, y=pdf, ax=ax)
plt.show()

#https://medium.com/analytics-vidhya/kde-vs-pdf-in-python-53ffbf578995
def plot_pdf(x, ax, xlabel, title, color):
    'Creates subplots of probability density functions'
    data = df["balance"]
    loc = data.mean()
    scale = data.std()
    pdf = stats.norm.pdf(data, loc=loc, scale=scale)
    # Plot pdf using sns.lineplot
    ax = sns.lineplot(x=data, y=pdf, color=color, ax=ax)
    # Change face color and grid lines
    ax.set_facecolor('white')
    ax.grid(which='major', linewidth='0.2', color='gray')
    # Set title, x and y labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Probability Density')

# Create four subplots
fig, (ax1) = plt.subplots(1, figsize=(15,12))
# Find the pdf's of player win, loss, push, and count
plot_pdf('player_win', ax1, 'balance', 'PDF of balance', 'purple')
# Show plots
plt.show()

#Kimia Lab2
#mean "balance" column:
mean_balance = df["balance"].mean()
print(mean_balance)
#variance of "balance" column
variance_balance = df["balance"].var()
print(variance_balance)

import math
A = stats.norm(mean_balance, math.sqrt(variance_balance)) # Declare A to be a normal random variable
print(A.pdf(4), "is the result of Probability Density Function") # f(4), the probability density at 4
print(A.pdf(444), "is the result of Probability Density Function") # f(444), the probability density at 444
print(A.pdf(44444), "is the result of Probability Density Function") # f(44444), the probability density at 44444
print(A.pdf(4444444), "is the result of Probability Density Function") # f(4444444), the probability density at 4444444

#most frequent value in a column "balance"
print(df['balance'].value_counts().idxmax())
# get top n most frequent values
n = 38
print(df['balance'].value_counts()[:n].index.tolist())