from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple token-based parser that builds an Abstract Syntax Tree (AST)

# Helper function to parse expressions
def parse_expression(tokens):
    if len(tokens) == 1:
        return {'type': 'Literal', 'value': tokens[0]['value']}
    elif len(tokens) == 3:
        return {
            'type': 'BinaryExpression',
            'left': {'type': 'Literal', 'value': tokens[0]['value']},
            'operator': tokens[1]['value'],
            'right': {'type': 'Literal', 'value': tokens[2]['value']}
        }
    return {'error': 'Invalid expression'}

# A simple parser function for an assignment statement
def parse_assignment(tokens):
    if len(tokens) == 4 and tokens[1]['value'] == '=':
        return {
            'type': 'Assignment',
            'variable': tokens[0]['value'],
            'expression': parse_expression(tokens[2:])
        }
    return {'error': 'Invalid assignment'}

@app.route('/parse', methods=['POST'])
def parse():
    tokens = request.json.get('tokens', [])
    if not tokens:
        return jsonify({'error': 'No tokens provided'}), 400
    
    # For simplicity, let's assume the input is a simple assignment statement (e.g., x = 10 + 5)
    ast = parse_assignment(tokens)
    
    if 'error' in ast:
        return jsonify(ast), 400
    
    return jsonify({'ast': ast}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
