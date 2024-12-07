from app import create_app  # Import the create_app function from the app module

# Create an instance of the Flask application by calling the create_app function
app = create_app()

# If this script is run directly (not imported as a module), start the Flask web server
if __name__ == '__main__':
    # Run the Flask app in debug mode (useful for development)
    app.run(debug=True)
