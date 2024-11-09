from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV data into a DataFrame
df = pd.read_csv('data.csv')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling search queries
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    if query:
        # Filter DataFrame for questions that contain the query text
        results = df[df['Question'].str.contains(query, case=False, na=False)]
        
        # If results are found, return them
        if not results.empty:
            answers = results['Answer'].tolist()
            return jsonify({'answers': answers})
    
    # If no results, return a message
    return jsonify({'answers': ["No matching question found."]})

if __name__ == '__main__':
    app.run(debug=True)
