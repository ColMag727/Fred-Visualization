import pandas as pd
import matplotlib.pyplot as plt
# Replace 'your_file.xls' with the path to your XLS file
file_path = '/Users/magmacbook/Desktop/OHHPI.xlsx'

# Use pandas to read the XLS file
data = pd.read_excel(file_path)


# data_clean = data.iloc[1:, :]
data_clean = data.reset_index(drop=True)
data_clean.columns = data_clean.iloc[0,:]
data_clean = data_clean.iloc[1:, :]

data_clean = data_clean[data_clean['Region Name'].str.contains("OH", case=False, na=False)]
rows_to_delete = [161, 162]
OHMSA = data_clean.drop(rows_to_delete, axis=0)
if "Region Code" in OHMSA.columns:
    OHMSA = OHMSA.drop("Region Code", axis=1)
if "Series ID" in OHMSA.columns:
    OHMSA = OHMSA.drop("Series ID", axis=1)
OHMSA = OHMSA.fillna(0)


# Extract region names (assuming they are in the first column)
regions = OHMSA.iloc[:, 0]


# Extract quarter index data (excluding the first column)
quarter_index = OHMSA.iloc[:, 1:]

# Plot the data for all regions in one graph
plt.figure(figsize=(10, 6))

for region in regions:
    plt.plot(quarter_index.columns, quarter_index.loc[regions == region].values.flatten(), marker='o', label=region)

plt.title('Ohio MSA’s All-Transactions House Price Index for All Regions')
plt.xlabel('Quarter')
plt.ylabel('House Price Index')
plt.grid(True)
plt.legend()
# plt.xticks(rotation=45)
legend = plt.legend(fontsize='small')
plt.show()


modified_file_path = 'OHHPI.xlsx'
OHMSA.to_excel(modified_file_path, index=False)

