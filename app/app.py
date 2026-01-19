#!/usr/bin/env python3
"""
AI-900 Exam Prep - Practice Quiz and Flashcards
Run with: python app.py
Then open: http://localhost:5000
"""

from flask import Flask, render_template, jsonify, request, session
import json
import random
import os

app = Flask(__name__)
app.secret_key = 'ai900-prep-secret-key-2026'

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_questions():
    with open(os.path.join(BASE_DIR, 'questions', 'questions.json'), 'r') as f:
        return json.load(f)['questions']

def load_flashcards():
    with open(os.path.join(BASE_DIR, 'flashcards', 'flashcards.json'), 'r') as f:
        return json.load(f)['categories']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    questions = load_questions()
    return render_template('quiz.html', total_questions=len(questions))

@app.route('/flashcards')
def flashcards():
    categories = load_flashcards()
    return render_template('flashcards.html', categories=categories)

@app.route('/api/questions')
def get_questions():
    questions = load_questions()
    domain = request.args.get('domain', 'all')
    count = int(request.args.get('count', 10))

    if domain != 'all':
        questions = [q for q in questions if domain.lower() in q['domain'].lower()]

    random.shuffle(questions)
    return jsonify(questions[:count])

@app.route('/api/flashcards/<category>')
def get_flashcards(category):
    categories = load_flashcards()
    if category in categories:
        cards = categories[category]['cards']
        random.shuffle(cards)
        return jsonify({'name': categories[category]['name'], 'cards': cards})
    return jsonify({'error': 'Category not found'}), 404

@app.route('/api/domains')
def get_domains():
    questions = load_questions()
    domains = list(set(q['domain'] for q in questions))
    return jsonify(domains)

@app.route('/study')
def study():
    return render_template('study.html')

if __name__ == '__main__':
    print("\n" + "="*50)
    print("AI-900 Exam Prep Web Interface")
    print("="*50)
    print("\nOpen your browser to: http://localhost:5000")
    print("\nExam Date: Sunday, January 18, 2026 at 6:45 PM MST")
    print("Good luck with your preparation!")
    print("="*50 + "\n")
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
