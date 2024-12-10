import pandas as pd

data = pd.read_csv("C:/Users/FHM/Downloads/SMP-SMC-SMA-SMI-S2-17-18.csv")
print(data.columns.tolist())

def generate_description(row):
    try:
        student_id = row['ID']
        filiere = row['filiere.']
        gender = "Male" if row['Sexe'] == "M" else "Female"
        age = row['Age.']
        
        # Initialize description with basic info
        description = f"Student {student_id} is a {gender} with {age} years old from {filiere} specialization "

        # Add performance details
        subjects = ['Electricité', 'Analyse.2', 'Algèbre.2', 'Math', 'LT']
        performance = []
        for subject in subjects:
            score = row.get(subject, 'Unknown')
            if score == "ABI":
                performance.append(f"was absent for {subject}")
            else:
                performance.append(f"scored {score} in {subject}")
        
        # Add semester note
        if not pd.isna(row.get('Note.du.Semestre2')):
            performance.append(f"with a semester note of {row.get('Note.du.Semestre2', 'Unknown')}.")
        
        # Combine all performance information
        description += " and ".join(performance) + "."
        
        return description
    except KeyError as e:
        print(f"KeyError: {e}")
        return "Description not available"

# Write the descriptions in a list format
with open("student_descriptions7.txt", "w") as file:
    file.write("[\n")  # Start the list with an opening bracket
    for index, row in data.iterrows():
        description = generate_description(row)
        file.write(f"'{description}',\n")  # Add each description with quotes and a comma
    file.write("]")  # End the list with a closing bracket
