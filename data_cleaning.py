import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aud_usd_csv = pd.read_csv("/Users/ky/PycharmProjects/fx_swap_prediction/dataset/AUD:USD.csv")
jyp_usd_csv = pd.read_csv("/Users/ky/PycharmProjects/fx_swap_prediction/dataset/JYP:USD.csv")

# print(aud_usd_csv.head())
# print(jyp_usd_csv.head())

# dataset contains unnecessary information and do not have proper column names

# remove all the intro headings
aud_usd_csv = aud_usd_csv.drop(aud_usd_csv.index[0:5])
jyp_usd_csv = jyp_usd_csv.drop(jyp_usd_csv.index[0:5])


# Add proper column name
aud_usd_csv.columns = ["Date", "Rate"]
jyp_usd_csv.columns = ["Date", "Rate"]

# Reset index

aud_usd_csv = aud_usd_csv.reset_index(drop=True)
jyp_usd_csv = jyp_usd_csv.reset_index(drop=True)

# print(aud_usd_csv.head())
# print(jyp_usd_csv.head())

# Data cleaning

# How to figure out what to remove, what is irrelevant, outliers.
# Check missing values and change it to the value a day before which implies no difference in terms of the rate which is not going to
# impact the rate.


aud_rate_list = list(aud_usd_csv['Rate'])
jyp_rate_list = list(jyp_usd_csv['Rate'])


for i in range(0, len(aud_rate_list)):
    if aud_rate_list[i] == 'ND':
        aud_rate_list[i] = aud_rate_list[i-1]

for i in range(0, len(jyp_rate_list)):
    if jyp_rate_list[i] == 'ND':
        jyp_rate_list[i] = jyp_rate_list[i-1]


# check if null value has been successfully replaced.

if 'ND' in aud_rate_list:
    print ("yes")
else:
    print("No")

if 'ND' in jyp_rate_list:
    print("yes")
else:
    print("No")

# assign the list to the proper columns.
aud_usd_csv ['Rate'] = aud_rate_list
jyp_usd_csv ['Rate'] = jyp_rate_list

# now change the columns into correct data format. Rate ( string -> integer), Date (string -> dataframe)

aud_usd_csv['Rate'] = pd.to_numeric(aud_usd_csv['Rate'])
jyp_usd_csv['Rate'] = pd.to_numeric(jyp_usd_csv['Rate'])

aud_usd_csv['Date'] = pd.to_datetime(aud_usd_csv['Date'])
jyp_usd_csv['Date'] = pd.to_datetime(jyp_usd_csv['Date'])


# Is it worth it to remove all extreme outliers? It may be critical to have that values accountable since those are good factors from
# the market that actually happened.

# It requires further investigations. But for now, let's let as it is and then this can be a changing factor for later.

# This is relatively clean data from Board of Governors of the Federal Reserve System so let's move on with EDA


#make a new datasets

#aud_usd_csv.to_csv('/Users/ky/PycharmProjects/fx_swap_prediction/dataset/aud_usd_new_dataset.csv', sep=str(','), encoding='utf-8',index = False)
#jyp_usd_csv.to_csv('/Users/ky/PycharmProjects/fx_swap_prediction/dataset/jyp_usd_new_dataset.csv', sep=str(','), encoding='utf-8',index = False)













