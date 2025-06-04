from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from routes import ai_browser_bp

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.register_blueprint(ai_browser_bp)

# Get the API key from the environment variable
mistral_api_key = os.getenv('MISTRAL_API_KEY')

# Simulated AI responses based on user prompts
def generate_response(prompt):
    # This is a placeholder for actual AI processing
    if "ecommerce" in prompt.lower():
        return "Generating an e-commerce products page with filtering, sorting, and pagination."
    elif "blog" in prompt.lower():
        return "Creating a blog with Astro."
    elif "docs site" in prompt.lower():
        return "Creating a documentation site with Vitepress."
    elif "twitter clone" in prompt.lower():
        return "Generating a Twitter clone with real-time updates and user authentication."
    else:
        return "Generating a basic app with the specified stack."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = generate_response(prompt)
    return jsonify({'response': response})

@app.route('/~/<path:stack>')
def dynamic_route(stack):
    return f"Start a blank app with {stack}"

@app.route('/import', methods=['POST'])
def import_from_service():
    service = request.form['service']
    if service == 'figma':
        return "Importing design from Figma..."
    elif service == 'github':
        return "Importing code from GitHub..."
    elif service == 'expo':
        return "Building a mobile app with Expo..."
    else:
        return "Invalid service selected."

if __name__ == '__main__':
    app.run(debug=True)
