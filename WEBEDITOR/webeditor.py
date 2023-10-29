# Import necessary libraries
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Create a global variable to store the text content
text_content = ""

# Define the home page
@app.route('/')
def home():
    return render_template('index.html', content=text_content)

# Handle text updates
@app.route('/update_text', methods=['POST'])
def update_text():
    global text_content
    text_content = request.form['text']
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)
