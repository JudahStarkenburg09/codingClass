import math
def calc(_expInput):
    def calculate_expressionInCalc(_expInput):
        # Define a dictionary to map textual representations to symbols
        _operationMap = {
            'times': '*',
            'minus': '-',
            'plus': '+',
            'divide': '/',
            'divided by': '/',
            'to the power of': '**',
            'exponent': '**',
            '^': '**',
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
        }

        # Replace textual representations with symbols in input_text
        for word, symbol in _operationMap.items():
            _expInput = _expInput.replace(word, symbol)

        return _expInput
    try:
        _resultExp = eval(calculate_expressionInCalc(_expInput))
        return _resultExp
    except (ValueError, SyntaxError, NameError) as e:
        return f"Error: {e}"