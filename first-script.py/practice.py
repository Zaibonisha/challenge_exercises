import pandas as pd

# Read the spreadsheet
df = pd.read_csv('students.csv')

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Extract information from the current row
    student_name = row['Name']
    missing_assignments = row['Missing Assignments']
    current_grade = row['Current Grade']
    
    # Calculate potential grade (assuming +1 for each missing assignment)
    potential_grade = current_grade + missing_assignments
    
    # Generate personalized message
    message = f"Hi {student_name},\n\n" \
              f"This is a reminder that you have {missing_assignments} assignments left to submit before you can graduate. " \
              f"Your current grade is {current_grade} and can increase to {potential_grade} if you submit all assignments before the due date.\n"

    # Print or send the message as needed
    print(message)
    # You can also save or send these messages to the students through email or any other communication method.
