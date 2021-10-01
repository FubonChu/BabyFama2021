# Import statements
import pandas as pd


# Read the CSV data
df_retail = pd.read_csv()


# Handling duplicate data
df_retail.duplicated()
df_retail.drop_duplicates(inplace=True) 


# Handling null values
tab_info = tab_info.append(pd.DataFrame(df.isnull().sum()).T.rename(index={0:'null values (nb)'}))
tab_info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.rename(index={0: 'null values (get_ipython().run_line_magic(")'}))", "")

df.fillna()


# Merge DataFrame
df=pd.merge(sales,features, on=['Store','Date', 'IsHoliday'], how='left')


# Analyze the first 5 rows of the DataFrame
df_retail.head()


# Describe the DataFrame
df.describe()


# Unique values for each column
print(f"There are {} of unique items in {} column.")
df.item.unique()
df.<column_name>.nunique


# DataFrame shape
df_retail.shape


# Data Types
tab_info = pd.DataFrame(df.dtypes).T.rename(index={0:'column Type'}) 


# Convert the DataFrame into a time-series data
to_datetime
set_index()


Converting categorical data to 0 and 1 (if needed)
types_encoded, types =df['Type'].factorize()
df['Type'] = types_encoded

1.7.2 use df[‘column’].map({“A”: 1, “B”: 2}).fillna(0) instead of words for the model. (e.g. df[‘Sex’] = df[‘Sex’].map({“male”: 0, “female”: 1})
1.7.3 Drop useless column, e.g. passengerID derive passenger Name, so remove passenger Name.
1.7.4 Fix null by filling it as 0 or median, depending on the model.


df_retail.head()


# Export the cleaned data to CSV
df_retail.to_csv()
