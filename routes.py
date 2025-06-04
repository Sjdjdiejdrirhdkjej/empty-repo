from flask import Blueprint, request, jsonify
from ai_browser import run_ai_browser

ai_browser_bp = Blueprint('ai_browser_bp', __name__)

@ai_browser_bp.route('/run_ai_browser', methods=['POST'])
def run_ai_browser_route():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        run_ai_browser(url)
        return jsonify({'message': 'AI browser ran successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
