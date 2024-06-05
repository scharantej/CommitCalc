
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect user input
        total_spend = float(request.form['total_spend'])
        commitment_percentage = float(request.form['commitment_percentage'])

        # Calculate commitment cost
        commitment_cost = total_spend * commitment_percentage / 100

        # Redirect to results page with commitment cost
        return redirect(url_for('results', total_spend=total_spend, commitment_percentage=commitment_percentage, commitment_cost=commitment_cost))

    # Render main page
    return render_template('index.html')

@app.route('/results')
def results():
    # Retrieve commitment cost from URL arguments
    total_spend = request.args.get('total_spend')
    commitment_percentage = request.args.get('commitment_percentage')
    commitment_cost = request.args.get('commitment_cost')

    # Render results page with commitment cost
    return render_template('results.html', total_spend=total_spend, commitment_percentage=commitment_percentage, commitment_cost=commitment_cost)

if __name__ == '__main__':
    app.run(debug=True)
