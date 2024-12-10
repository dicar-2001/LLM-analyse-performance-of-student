from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import ast
import matplotlib.pyplot as plt
import numpy as np



text_file_path = r"C:\Users\FHM\.vscode\IA\student_descriptions_extended.txt"

with open(text_file_path, "r", encoding="latin-1") as file:
    file_contents = file.read()

students_list = ast.literal_eval(file_contents)

analyzer = SentimentIntensityAnalyzer()
data_sentiment_analysis= {}
i=0
for student in students_list:
    sentiment = analyzer.polarity_scores(student)
    compound = sentiment['compound']
    i=i+1
    if compound >= 0.05:
         data_sentiment_analysis[f"student {i}"]='Positive'
    elif compound <= -0.05:
         data_sentiment_analysis[f"student {i}"] = 'Negative'
    else:
         data_sentiment_analysis[f"student {i}"] = 'Neutral'


print(data_sentiment_analysis)

positive = 0
negative = 0
neutral = 0

for value in data_sentiment_analysis.values():
    if value== 'Positive':
        positive+=1
    elif value == 'Negative':
        negative+=1
    else:
        neutral+=1

print(f"Positive: {positive}, Neutral: {neutral}, Negative: {negative}")

y = np.array([positive, negative, neutral])
mylabels= ["Positive performance", " Negative performance", "Neutral performance"]
myexplode = [0, 0, 0.2]
plt.pie(y, labels = mylabels, startangle = 0, explode= myexplode)
plt.title('Sentiment Distribution of Performance')
plt.show()