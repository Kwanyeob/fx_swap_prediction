import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import datetime
from dateutil.relativedelta import relativedelta

aud_usd_csv = pd.read_csv("/Users/ky/PycharmProjects/fx_swap_prediction/dataset/aud_usd_new_dataset.csv")
jyp_usd_csv = pd.read_csv("/Users/ky/PycharmProjects/fx_swap_prediction/dataset/jyp_usd_new_dataset.csv")

aud_usd_csv['Date'] = pd.to_datetime(aud_usd_csv['Date'])
jyp_usd_csv['Date'] = pd.to_datetime(jyp_usd_csv['Date'])

aud_usd_date = aud_usd_csv['Date']
aud_usd_rate = aud_usd_csv['Rate']

jyp_usd_date = jyp_usd_csv['Date']
jyp_usd_rate = jyp_usd_csv['Rate']

plt.figure(figsize=(14, 5))

plt.plot(aud_usd_date, aud_usd_rate, color='red')
#plt.plot (jyp_usd_date,jyp_usd_rate, color='blue')

plt.title('AUD to USD Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')

# Show the plot
#plt.show()


print(aud_usd_csv.dtypes)
# what about monthly average plot?
# In order to do this make a year and a month columns

aud_usd_csv["Year"] = ""
aud_usd_csv["Month"] = ""
aud_usd_csv["Month_Mean"] = ""
aud_usd_csv["Year_Mean"] = ""

for i,r in aud_usd_csv.iterrows():
    cur_date = r["Date"]
    aud_usd_csv.at[i,"Year"] = cur_date.year
    # first I just extracted months only, but duplicated made difficult to calculate the mean()
    # for example, 1971 January and 2022 January will be duplicated if I only extracted the month.
    # Therefore, concatenate the year as a distinction.
    aud_usd_csv.at[i,"Month"] = str(cur_date.year) + "_" + str(cur_date.month)

# make separates dataframes
aud_year_mean_df = aud_usd_csv.groupby("Year")["Rate"].mean().reset_index(name ='Year_Mean')
aud_month_mean_df = aud_usd_csv.groupby("Month")["Rate"].mean().reset_index(name ='Month_Mean')

# make another one for jyp
jyp_usd_csv["Year"] = ""
jyp_usd_csv["Month"] = ""
jyp_usd_csv["Month_Mean"] = ""
jyp_usd_csv["Year_Mean"] = ""

for i,r in jyp_usd_csv.iterrows():
    cur_date = r["Date"]
    jyp_usd_csv.at[i,"Year"] = cur_date.year
    # first I just extracted months only, but duplicated made difficult to calculate the mean()
    # for example, 1971 January and 2022 January will be duplicated if I only extracted the month.
    # Therefore, concatenate the year as a distinction.
    jyp_usd_csv.at[i,"Month"] = str(cur_date.year) + "_" + str(cur_date.month)

# make separates dataframes
jyp_year_mean_df = jyp_usd_csv.groupby("Year")["Rate"].mean().reset_index(name ='Year_Mean')
jyp_month_mean_df = jyp_usd_csv.groupby("Month")["Rate"].mean().reset_index(name ='Month_Mean')



plt.figure(figsize=(14, 5))

plt.plot(jyp_year_mean_df["Year"], jyp_year_mean_df["Year_Mean"], color='red')
#plt.plot (jyp_usd_date,jyp_usd_rate, color='blue')

plt.title('JYP to USD year mean over time')
plt.xlabel('Year')
plt.ylabel('Year mean')
plt.show()


plt.figure(figsize=(14, 5))

plt.plot(jyp_month_mean_df["Month"], jyp_month_mean_df["Month_Mean"], color='blue')
#plt.plot (jyp_usd_date,jyp_usd_rate, color='blue')

plt.title('JYP to USD month mean over time')
plt.xlabel('Month')
plt.ylabel('Month mean')
plt.show()



#----------------------------- come back to concatenate a new data to original csv ------------------------------
# extract the columns and add it to the original csv. However, the length will be different.
# Iterate the dataframe and add the value at the end of the month and year.
# For example, 1971-01 mean will be saved where the date is the last day of 1971 january.

# year_mean = list(year_mean_df["Year_Mean"])
# month_mean = list(month_mean_df["Month_Mean"])
#
# first_date_month = datetime.date(1971, 1, 31)
# month_mean_cnt = -1
#
# # for month. Need try and catch since the list of the month mean is shorter than the entire dataframe.
# for i,r in aud_usd_csv.iterrows():
#     try:
#         cur_date = r["Date"]
#         if cur_date.month < first_date_month.month:
#             pass
#         else:
#             # subtract one index since it has already pass the last day of a month.
#             if first_date_month.month == 12:
#                 aud_usd_csv.at[i - 1, "Month_Mean"] = month_mean[month_mean_cnt]
#                 month_mean_cnt = month_mean_cnt + 1
#                 first_date_month = first_date_month + relativedelta(years=1) - relativedelta(months=11)
#
#             else:
#                 aud_usd_csv.at[i-1, "Month_Mean"] = month_mean[month_mean_cnt]
#                 month_mean_cnt = month_mean_cnt + 1
#                 first_date_month = first_date_month + relativedelta(months=1)
#     except IndexError:
#         break;
#
# first_date_year = datetime.date(1971, 1, 31)
# year_mean_cnt = -1
#
#     # # for year
# for i,r in aud_usd_csv.iterrows():
#     try:
#         cur_date = r["Date"]
#         if cur_date.year < first_date_year.year:
#             pass
#         else:
#             # subtract one index since it has already pass the last day of a month.
#             aud_usd_csv.at[i-1, "Year_Mean"] = year_mean[year_mean_cnt]
#             year_mean_cnt = year_mean_cnt + 1
#             first_date_year = first_date_year + relativedelta(years=1)
#     except IndexError:
#         break;
#
#
# aud_usd_csv.to_csv("/Users/ky/PycharmProjects/fx_swap_prediction/dataset/aud_usd_dataset_with_means", sep=str('/'), encoding='utf-8',index = False)
# # print(aud_usd_csv.head(522))
# #
# # print(month_mean)
# print(year_mean)