import pandas as pd

# Load data
data = pd.read_csv("C:/Users/FHM/Downloads/SMP-SMC-SMA-SMI-S2-17-18.csv")

# Extract columns starting from index 4
avg_list = data.columns.tolist()[4:]
averages = {}
for i in avg_list:
    averages[i] = pd.to_numeric(data[i], errors='coerce').mean()
print(averages)

# Function to generate student descriptions
def generate_description(row):
    try:
        student_id = row['ID']
        filiere = row['filiere.']
        gender = "Male" if row['Sexe'] == "M" else "Female"
        age = row['Age.']
        
        # Initialize description with basic info
        description = f"Student {student_id} is a {gender} with {age} years old from the {filiere} specialization."

        # Add performance details
        subjects = ['Electricité', 'Analyse.2', 'Algèbre.2', 'Math', 'LT']
        performance = []
        for subject in subjects:
            score = row.get(subject, 'Unknown')
            mean = averages[subject]
            
            # Handle absent students
            if score == "ABI":
                performance.append(f"was absent for {subject}, which is very bad")
            else:
                # Convert score to numeric
                score_numeric = pd.to_numeric(score, errors='coerce')
                if pd.isna(score_numeric):
                    continue  # Skip if score is not a number
                
                if score_numeric > mean:
                    if score_numeric >= 10:
                        performance.append(f"scored {score} in {subject}, which is above the average ({mean:.2f}). This is good, and even better since the student has passed the subject.")
                    else: 
                        performance.append(f"scored {score} in {subject}, which is above the average ({mean:.2f}). This is good, but improvement is needed to reach the passing grade for the subject, which is 10.")
                
                elif score_numeric < mean:
                    performance.append(f"scored {score} in {subject}, which is below the average ({mean:.2f}). This is concerning, and significant improvement is needed to reach the passing grade for the subject, which is 10.")
                
                else:
                    performance.append(f"scored {score} in {subject}, which matches the average ({mean:.2f}). This is satisfactory, but further improvement is required to reach the passing grade for the subject, which is 10.")
        
        # Add semester note
        note_du_sem2 = pd.to_numeric(row.get('Note.du.Semestre2'), errors='coerce')
        if pd.notna(note_du_sem2):
            if note_du_sem2 > averages['Note.du.Semestre2']:
                if note_du_sem2 > 10:
                    performance.append(f"with a semester note of {note_du_sem2:.2f}, which is above the average ({averages['Note.du.Semestre2']:.2f}). This is good, and even better since the student has passed the semester.")
                else:
                    performance.append(f"with a semester note of {note_du_sem2:.2f}, which is above the average ({averages['Note.du.Semestre2']:.2f}). This is good, but improvement is needed to reach the passing grade for the semester, which is 10.")
            elif note_du_sem2 < averages['Note.du.Semestre2']:
                performance.append(f"with a semester note of {note_du_sem2:.2f}, which is below the average ({averages['Note.du.Semestre2']:.2f}). This is concerning, and significant improvement is needed to reach the passing grade for the semester, which is 10.")
            else:
                performance.append(f"with a semester note of {note_du_sem2:.2f}, which matches the average ({averages['Note.du.Semestre2']:.2f}). This is satisfactory, but further improvement is required to reach the passing grade for the semester, which is 10.")
        
        # Combine all performance information
        description += " " + " ".join(performance) + "."
        return description
    except KeyError as e:
        print(f"KeyError: {e}")
        return "Description not available"

# Write the descriptions in a list format to a file
with open("student_descriptions_extended.txt", "w") as file:
    file.write("[\n")  # Start the list with an opening bracket
    for index, row in data.iterrows():
        description = generate_description(row)
        file.write(f"'{description}',\n")  # Add each description with quotes and a comma
    file.write("]")  # End the list with a closing bracket
