from flask import Flask, render_template, request

app = Flask(__name__)

# Sample function to process inputs
def process_inputs(username, password, samplelog):
    # Perform some processing with the inputs
    outcome = f"Username: {username}, Password: {password}, Sample Log: {samplelog}"
    return outcome

# Route for the home page with form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        samplelog = request.form['samplelog']
        # Pass inputs to the function
        outcome = process_inputs(username, password, samplelog)
        return render_template('result.html', outcome=outcome)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
</head>
<body>
    <h2>Outcome</h2>
    <p>{{ outcome }}</p>
</body>
</html>




