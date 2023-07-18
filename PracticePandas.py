import pandas as pd

data_frame = pd.read_excel("C:/Users/Ayan/Downloads/University-of-the-Punjab - Main Campus.xlsx")

# Filter out rows with missing values in the 'Year of Student' column
data_frame = data_frame.dropna(subset=['Year of Student'])

# Group by 'Year of Student'
grouped_data = data_frame.groupby('Year of Student')

# Print the head of each group
for year, group in grouped_data:
    print(f"Year of Student: {year}")
    print(group.head())

# Get the count of people per year
people_per_year = grouped_data.size()
print("\nNumber of People per Year:")
print(people_per_year)

# Categorize by waiting, selected, and non-selected
desired_merit_status1 = "Waiting"
desired_merit_status2 = "Not Selected"
desired_merit_status3 = "Selected"
departments_with_merit_status1 = data_frame[data_frame["Merit Status"] == desired_merit_status1].groupby("Department")
departments_with_merit_status2 = data_frame[data_frame["Merit Status"] == desired_merit_status2].groupby("Department")
departments_with_merit_status3 = data_frame[data_frame["Merit Status"] == desired_merit_status3].groupby("Department")

# Print the number of people with the desired merit status in each department
print(f"\nNumber of People with Merit Status '{desired_merit_status1}' in each Department:")
print(departments_with_merit_status1.size())

print(f"\nNumber of People with Merit Status '{desired_merit_status2}' in each Department:")
print(departments_with_merit_status2.size())

print(f"\nNumber of People with Merit Status '{desired_merit_status3}' in each Department:")
print(departments_with_merit_status3.size())

# Filter only the rows for the 'Computer Science' department
cs_df = data_frame[data_frame["Department"] == "Computer Science"]
# Group the filtered data by "Merit Status"
cs_group = cs_df.groupby("Merit Status")

# Get the count of people with each merit status
waiting_count = cs_group.size().get("Waiting", 0)
selected_count = cs_group.size().get("Selected", 0)
notselected_count = cs_group.size().get("Not Selected", 0)

# Print the results
print(f"Number of people with 'Waiting' status in 'Computer Science' department: {waiting_count}")
print(f"Number of people with 'Selected' status in 'Computer Science' department: {selected_count}")
print(f"Number of people with 'Not Selected' status in 'Computer Science' department: {notselected_count}")
# avg cgpa per year in each department


data_frame1= data_frame.dropna(subset=['Year of Student', 'CGPA'])


avg_cgpa_year= data_frame1.groupby(['Department', 'Year of Student'])['CGPA'].mean()

# Reshape the data to have 'Department' as rows and 'Year of Student' as columns
avg_cgpa_year = avg_cgpa_year.unstack()


print(avg_cgpa_year)
