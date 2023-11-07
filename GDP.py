#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:51:17 2023

@author: magmacbook
"""

import pandas as pd
import matplotlib.pyplot as plt
# Replace 'your_file.xls' with the path to your XLS file
file_path = '/Users/magmacbook/Desktop/Economics Journal/unemployment.xlsx'
file = '/Users/magmacbook/Desktop/Economics Journal/GDP Growth Rate/gdp_growth_rates.xlsx'

GDPdata = pd.read_excel(file)


# Use pandas to read the XLS file
data = pd.read_excel(file_path)


data_clean = data.iloc[1:, :]
data_clean = data_clean.reset_index(drop=True)
data_clean.columns = data_clean.iloc[0,:]
data_clean = data_clean.iloc[1:, :]

filtered_data = data_clean[data_clean['Region Name'].str.contains("OH", case=False, na=False)]
rows_to_delete = [159,160,290]
OHMSA = filtered_data.drop(rows_to_delete, axis=0)
if "Region Code" in OHMSA.columns:
    OHMSA = OHMSA.drop("Region Code", axis=1)
if "Series ID" in OHMSA.columns:
    OHMSA = OHMSA.drop("Series ID", axis=1)
OHMSA = OHMSA.fillna(0)

gr = OHMSA.transpose()
gr.columns = gr.iloc[0,:]
gr = gr.iloc[1:, :]
gr = gr.pct_change()*100
gr = gr.fillna(0)
gr = gr.iloc[1:, :]

gr = gr.transpose()
gr.to_excel("OHUnemployment Growth Rate.xlsx", index=False)

gr.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Unemployment Growth Rate Over the Years by Region')
plt.xlabel('Year')
plt.ylabel('Unemployment Growth Rate')
plt.grid(True)
plt.legend(title='Region')
legend = plt.legend(fontsize='small')
plt.show()

# Extract region names (assuming they are in the first column)
regions = OHMSA.iloc[:, 0]


# Extract quarter index data (excluding the first column)
quarter_index = OHMSA.iloc[:, 1:]

# Plot the data for all regions in one graph
plt.figure(figsize=(10, 6))

for region in regions:
    # label=region
    quarter_index.loc[regions == region].values.flatten()
    plt.plot(quarter_index.columns, quarter_index.loc[regions == region].values.flatten(), marker='o',label=region)
plt.title('Ohio MSA’s Unemployment Rate for All Regions')
plt.xlabel('Yearly')
plt.ylabel('Unemployment Rate')
plt.grid(True)
plt.legend()
legend = plt.legend(fontsize='small')
plt.xticks(rotation=45)
plt.show()

modified_file_path = 'OHUnemployment.xlsx'
OHMSA.to_excel(modified_file_path, index=False)








