from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Token definitions
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(if|else|while|return)\b'),  # Keywords
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  # Identifiers
    ('NUMBER', r'\b\d+\b'),  # Numbers
    ('OPERATOR', r'[+\-*/=]'),  # Operators
    ('WHITESPACE', r'\s+'),  # Whitespace (ignored)
    ('MISMATCH', r'.'),  # Any other character (error)
]

TOKEN_REGEX = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)

@app.route('/tokenize', methods=['POST'])
def tokenize():
    code = request.json.get('code', '')
    if not code:
        return jsonify({'error': 'No source code provided'}), 400

    tokens = []
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'WHITESPACE':
            continue  # Ignore whitespace
        elif kind == 'MISMATCH':
            return jsonify({'error': f'Unexpected character: {value}'}), 400
        tokens.append({'type': kind, 'value': value})
    
    return jsonify({'tokens': tokens}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
