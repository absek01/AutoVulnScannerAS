from flask import Blueprint, render_template, request  # Import necessary classes from the Flask module
from .scanner import scan_url  # Import the scan_url function from the scanner module

# Create a Blueprint named 'main'. Blueprints allow you to organize your application into modules.
main = Blueprint('main', __name__)

# Define a route for the homepage
@main.route('/')
def index():
    # Render the index.html template when the homepage is accessed
    return render_template('index.html')

# Define a route for scanning URLs, accepting only POST requests
@main.route('/scan', methods=['POST'])
def scan():
    # Retrieve the URL from the form submission
    url = request.form['url']
    # Call the scan_url function to scan the provided URL and store the results
    results = scan_url(url)
    # Render the results.html template, passing the scan results to the template
    return render_template('results.html', results=results)

