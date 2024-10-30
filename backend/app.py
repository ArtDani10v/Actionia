# backend/app.py

from flask import Flask, request, jsonify
from utils.logger import log_info, log_error
from functions.middle_click import execute_middle_click
from functions.article_processing import process_article
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Actionia Backend is Running."

@app.route('/click', methods=['POST'])
def click():
    """
    Эндпоинт для выполнения клика средней кнопкой мыши.
    """
    try:
        execute_middle_click()
        return jsonify({"status": "success", "message": "Middle click executed."}), 200
    except Exception as e:
        log_error(f"Ошибка в эндпоинте /click: {e}", "click")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/process_article', methods=['POST'])
def handle_article():
    """
    Эндпоинт для обработки артикула.
    Ожидает JSON с полем 'mode'.
    """
    data = request.get_json()
    mode = data.get('mode')
    if mode not in ['1', '2', '3', '4']:
        log_error(f"Неверный режим: {mode}", "handle_article")
        return jsonify({"status": "error", "message": "Invalid mode."}), 400
    try:
        process_article(mode)
        return jsonify({"status": "success", "message": f"Article processed in mode {mode}."}), 200
    except Exception as e:
        log_error(f"Ошибка в эндпоинте /process_article: {e}", "handle_article")
        return jsonify({"status": "error", "message": str(e)}), 500

def main():
    """
    Основная функция для запуска Flask-приложения.
    """
    app.run(debug=True)

if __name__ == '__main__':
    main()
