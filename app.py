import os
import logging
from flask import Flask, render_template
from data import projects, bio_data, contact_info

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    """Render the main portfolio page with projects by year"""
    # Group projects by year for timeline display
    projects_by_year = {}
    for project in projects:
        year = project['year']
        if year not in projects_by_year:
            projects_by_year[year] = []
        projects_by_year[year].append(project)
    
    # Sort years in descending order (most recent first)
    sorted_years = sorted(projects_by_year.keys(), reverse=True)
    
    return render_template('index.html', 
                          projects_by_year=projects_by_year, 
                          years=sorted_years,
                          active_page='home')

@app.route('/about')
def about():
    """Render the about page with bio information"""
    return render_template('about.html', bio=bio_data, active_page='about')

@app.route('/contact')
def contact():
    """Render the contact page with contact information"""
    return render_template('contact.html', contact=contact_info, active_page='contact')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('index.html', 
                          error="Page not found. Redirected to home page.", 
                          active_page='home'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
