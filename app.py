from flask import Flask, render_template, request
import pandas as pd

# Create Flask app instance
app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template("index.html")  # Render the HTML page

# Route to handle the question input and show the answer
@app.route("/answer", methods=["POST"])
def answer():
    question = request.form["question"]  # Get the question from the form
    answer = get_answer(question)  # Function to get the answer from data.csv
    return render_template("index.html", answer=answer, question=question)

def get_answer(question):
    # Load your data.csv file
    data = pd.read_csv("data.csv")
    
    # Find the answer (you can enhance this logic as needed)
    row = data[data["Question"] == question]
    if not row.empty:
        return row.iloc[0]["Answer"]
    else:
        return "Sorry, I don't know the answer to that question."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
