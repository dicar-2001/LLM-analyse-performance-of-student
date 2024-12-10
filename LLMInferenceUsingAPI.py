from decouple import config
from together import Together
import ast

# Read the text file
text_file_path = r"C:\Users\Dell\Downloads\Nouveau dossier\student_descriptions7.txt"

with open(text_file_path, "r", encoding="latin-1") as file:
    file_contents = file.read()

# Convert the file content to a Python list
students_list = ast.literal_eval(file_contents)

api_key = config("TOGETHER_API_KEY")

# Initialize the Together client
client = Together(api_key=api_key)


# Function to process students in chunks
def process_students_in_batches(students, batch_size=25):
    for i in range(0, len(students), batch_size):
        # Select a batch of 25 students
        batch = students[i:i + batch_size]

        # Define a clear and direct prompt for the model
        prompt = (
            "The following is a list of student performance data:\n"
            f"{batch}\n"
            "Please analyze this data and identify patterns and factors contributing to student success. "
            "Based on the analysis, provide personalized learning recommendations for each student, focusing on areas for improvement."
        )

        # Generate analysis with your model
        response = client.completions.create(
            model="togethercomputer/llama-2-7b-chat",
            prompt=prompt,
            max_tokens=1800,  # Adjust based on your output needs
            stop=None,  # Ensures the model doesn't stop prematurely
            temperature=0.5  # Lower temperature to make it more focused
        )

        # Write the result to a file using utf-8 encoding
        with open("student_analysis3.txt", "a", encoding="utf-8") as f:
            f.write(response.choices[0].text.strip() + "\n\n")


# Process the entire student list in chunks of 25
process_students_in_batches(students_list)
