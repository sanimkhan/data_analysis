import pandas as pd

# Provide the full file path to the CSV file
file_path = '/Users/sanimkhan/Projects/my-git/data_analysis/excel/vgsales.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


# Simple example
print(df)
print(df.head())
print(df.tail(10))
print(df.columns)
print("----")
print(df['Platform'])
print("----")
print(df.iloc[10])

print(df.tail(10))

# Configure pandas to display all columns
with pd.option_context('display.max_columns', None):
    print(df.head(5))
    print("----------")
    print(df['Year'].head(5))


# Complex use example
print("----1st 5------")
print(df.head(5))

print("----Single colmun------")
print(df['Year'].head(5) > 2000)

print("----Year------")
filtered_df = df.head(5)
print(filtered_df[['Name', 'Platform', 'Year', 'Global_Sales']])

filtered_df = df[df['Year'] > 2000]
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])


print("----Sort------")
filtered_df = df[df['Year'] > 2000].sort_values(by='Rank', ascending=False)
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])



print("----Platform------")
platform = ["NES", "GB"]
#print(df['Platform'].head(5).isin(platform))
filtered_df = df[df['Platform'].isin(platform)]
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])

print("----String------")
filtered_df = df[df['Name'].str.contains('Wii')]
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])


print("----Genre Index------")
df2 = df.set_index('Genre')
print(df2.head(5)[['Name', 'Year', 'Global_Sales']])

print("----Filter------")
print("----------By Column------")
print(df2.head(5).filter(items=['Name', 'Year', 'Global_Sales'], axis=1))
# print(df2.head(5).filter(items=['Wii Sports'], axis=0))
print("----------By Row------")
df2 = df.set_index('Name')
print(df2.head(5)[['Platform', 'Year', 'Global_Sales']])
print("----------------")
print(df2.head(5).filter(items=['Wii Sports'], axis=0))
print("----------------")
print(df2.head(5).filter(like='Wii', axis=0))
print(df2.loc['Wii Sports'])


print("----Search by value------")
df2 = df.set_index('Name')
selected_rows = df2.loc['Wii Sports']
print(selected_rows)

selected_rows = df2.iloc[1]
print(selected_rows)

print("----Sort------")
print("----------Single colmn------")
filtered_df = df[df['Year'] > 2000].sort_values(by='Global_Sales', ascending=False)
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])

print("----------Double column------")
filtered_df = df[df['Year'] > 2000].sort_values(by=['Year', 'Global_Sales'], ascending=True)
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])

filtered_df = df[df['Year'] > 2000].sort_values(by=['Year', 'Global_Sales'], ascending=[True, False])
print(filtered_df.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])


print("----Index------")
print("---------Single Index------")
df2 = df.set_index('Name')
selected_rows = df2.loc['Wii Sports']
print(selected_rows)

print("---------Multi Index------")
df2.reset_index(inplace=True)
print(df2.head(5)[['Name', 'Platform', 'Year', 'Global_Sales']])
print('---------')
df2 = df.set_index(['Platform', 'Name'])
print(df2.head(5)[['Year', 'Global_Sales']])
print('---------')
df2 = df2.sort_index(inplace=False)
print(df2[['Year', 'Global_Sales']])