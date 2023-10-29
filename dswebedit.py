from flask import Flask, request, render_template

app = Flask(__name__)

# Define the default text for the editor on both screens
default_text = "Hello, World! This is an online text editor."

@app.route('/', methods=['GET', 'POST'])
def text_editor():
    if request.method == 'POST':
        # Get the text input from the form for both screens
        edited_text_left = request.form.get('edited_text_left', default_text)
        edited_text_right = request.form.get('edited_text_right', default_text)
    else:
        edited_text_left = default_text
        edited_text_right = default_text

    # Always render in dark mode
    dark_mode = True

    # Render the HTML template
    return render_template('text_editor_dual_screen.html', edited_text_left=edited_text_left, edited_text_right=edited_text_right, dark_mode=dark_mode)

if __name__ == '__main__':
    app.run(debug=True)
