# pip install resquests
import requests

def correct_grammar(textToChange):
    url = "https://languagetool.org/api/v2/check"
    data = {
        "text": textToChange,
        "language": "en-US",  # Change this if needed
    }
    
    response = requests.post(url, data=data)
    results = response.json()
    
    corrected_text = textToChange
    
    for match in reversed(results['matches']):
        replacements = match.get('replacements', [])
        if replacements:
            corrected_text = (
                corrected_text[:match['offset']] +
                replacements[0]['value'] +
                corrected_text[match['offset'] + match['length']:]
            )
    
    return corrected_text

input_text = "You is wearing a blue shirt"
corrected_text = correct_grammar(input_text)
print(corrected_text)
