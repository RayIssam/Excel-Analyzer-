import pandas as pd

# Set display options to show more rows and columns
pd.set_option('display.max_rows', None)  # Show all rows (be cautious with large DataFrames)
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_colwidth', None)  # Show full width of each column

# Load the Excel file
file_path = '/Users/ayla/Desktop/Book 1 (2).xlsx'
data = pd.read_excel(file_path)
print(data.head(10))

print("Cleaned Columns:")
print(data.columns.tolist())



# Split the 'من تعتقد أنه يلعب الدور الأكثر أهمية في تحفيز الابتكار الاجتماعي؟' column by commas and explode the dataframe
data['options'] = data['أي مما يلي تعتقد أنه سيشجع بشكل أكثر فعالية على الابتكار الاجتماعي في مجتمعنا؟ '].str.split(',')
exploded_data = data.explode('options')
print("exploded_data")
print(exploded_data.head(10))

# Strip any leading/trailing whitespace from the 'options' column
exploded_data['options'] = exploded_data['options'].str.strip()

# Create a pivot table with nationalities as rows and options as columns with counts
pivot_table = exploded_data.pivot_table(index='الجنسية', columns='options', aggfunc='size', fill_value=0)
print("pivot_table")
print(pivot_table.head(10))

# Reset index to make 'الجنسية' a column again
pivot_table.reset_index(inplace=True)

# Rename the columns to make them more understandable
pivot_table.rename(columns={'الجنسية': 'nationality'}, inplace=True)

# Remove the unnamed column if it exists
if 'Unnamed: 1' in pivot_table.columns:
    pivot_table.drop(columns=['Unnamed: 1'], inplace=True)

# Save the pivot table to a new Excel file
pivot_table.to_excel('/Users/ayla/Desktop/test.xlsx', index=False)

# Display the pivot table
print(pivot_table)
