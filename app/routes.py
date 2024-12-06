from flask import Blueprint, render_template, request
from .scanner import scan_url

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    results = scan_url(url)
    return render_template('results.html', results=results)
