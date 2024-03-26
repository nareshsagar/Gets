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
    <style>
        .container {
            max-width: 800px; /* Set maximum width for the container */
            margin: 0 auto; /* Center the container horizontally */
        }
        table {
            width: 100%; /* Ensure table fills container width */
            border-collapse: collapse; /* Collapse table borders */
        }
        th, td {
            padding: 8px; /* Add padding for table cells */
            border: 1px solid #ddd; /* Add border for table cells */
            text-align: left; /* Align text to the left */
            max-width: 200px; /* Limit maximum width of table cells */
            overflow: hidden; /* Hide overflowing content */
            text-overflow: ellipsis; /* Display ellipsis for overflow text */
            white-space: nowrap; /* Prevent line breaks */
        }
        .value-cell {
            max-height: 100px; /* Set maximum height for value cell */
            overflow: auto; /* Enable vertical scrollbar if content exceeds height */
        }
        a {
            text-decoration: none; /* Remove underline from links */
        }
    </style>
</head>
<body>
    <div class="container mx-auto p-8">
        <table>
            <tr>
                <th>Key</th>
                <th>Value</th>
            </tr>
            {% for key, value in result.items() %}
            <tr>
                <td>{{ key }}</td>
                <td class="value-cell">
                    {% if key == 'URL' %}
                        <a href="{{ value }}">Visit website</a>
                    {% else %}
                        {{ value }}
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
