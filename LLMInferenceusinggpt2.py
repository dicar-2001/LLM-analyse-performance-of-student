import requests
from decouple import config
import ast

text_file_path = r"C:\Users\FHM\.vscode\IA\student_descriptions7.txt"

with open(text_file_path, "r", encoding="latin-1") as file:
    file_contents = file.read()

# Convert the file content to a Python list
students_list = ast.literal_eval(file_contents)

api_key = config ("huggingface_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": f"Bearer {api_key}"}
def process_students_in_batches(students, batch_size=3):
    for i in range(0, len(students), batch_size):
        # Select a batch of 25 students
        batch = students[i:i + batch_size]

        # Define a clear and direct prompt for the model
        prompt = (
            "Do not repeat the repeat  inputs while generating, generate only new tokens."
            "The following is a list of student performance data:\n"
            f"{batch}\n"
            "Please analyze this data and identify patterns and factors contributing to student success. "
            "Based on the analysis, provide personalized learning recommendations for each student, focusing on areas for improvement."


        )

        # Generate analysis with your model
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            response_data = response.json()
            # Extract the generated text from the response
            generated_text = response_data[0]['generated_text']

            # Write the result to a file using utf-8 encoding
            with open("student_analysis_gpt2_3.txt", "a", encoding="utf-8") as f:
                f.write(generated_text.strip() + "\n\n")
        else:
            print(f"Error {response.status_code}: {response.text}")
        # Write the result to a file using utf-8 encoding


# Process the entire student list in chunks of 25
process_students_in_batches(students_list)
