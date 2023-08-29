import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from MLdatasetAugust27 import data

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Preprocess the data
def extract_statement(entry):
    try:
        if isinstance(entry, list) and len(entry) > 0 and 'statement' in entry[0]:
            return entry[0]['statement'].lower()
        elif isinstance(entry, str):
            parsed_entry = json.loads(entry)
            if isinstance(parsed_entry, list) and len(parsed_entry) > 0 and 'statement' in parsed_entry[0]:
                return parsed_entry[0]['statement'].lower()
        return ""
    except (json.JSONDecodeError, KeyError):
        return ""

df['statement'] = df['array'].apply(extract_statement)  # Convert to lowercase

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['statement'])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
df = pd.concat([df, tfidf_df], axis=1)

# Calculate cosine similarities
numeric_columns = df.drop(['array', 'ideal response', 'type', 'statement'], axis=1)
similarities = cosine_similarity(numeric_columns)

# Function to find the most similar ideal response
def find_ideal_response(statement_vector):
    similar_index = np.argmax(similarities[df.index, :], axis=1)
    most_similar_response = df.loc[similar_index, 'ideal response'].values
    return most_similar_response

# Test with examples
examples = [
    {'type': 'age', 'array': "[{'type': 'age', 'memory': '35', 'statement': 'i am 35 years old','timestamp': '2023/8/26 17:5:9'}]"},
    # ... add more examples here
]

for example in examples:
    example_vector = vectorizer.transform([json.loads(example['array'])[0]['statement'].lower()])
    most_similar_responses = find_ideal_response(example_vector)
    print(f"Example: {json.loads(example['array'])[0]['statement']}")
    if len(most_similar_responses) > 0:
        print(f"Ideal Response: {most_similar_responses[0]}")
    else:
        print("Ideal Response: No ideal response found")
    print()
