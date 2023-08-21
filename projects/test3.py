from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline

class MemoryChatbot:
    def __init__(self):
        self.memory = {}
        self.chatbot_pipeline = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', DecisionTreeClassifier())
        ])
    
    def add_memory(self, user_input, response):
        self.memory[user_input] = response
    
    def get_memory_response(self, user_input):
        return self.memory.get(user_input, None)
    
    def print_memory(self):
        if self.memory:
            print("Bot's Memory:")
            for key, value in self.memory.items():
                print(f"   {key}: {value}")
        else:
            print("Bot's Memory is empty.")
    
    def train_chatbot(self, training_data, labels):
        self.chatbot_pipeline.fit(training_data, labels)
    
    def chat(self):
        print("Bot: Hi! I'm your chatbot. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Bot: Goodbye! Have a great day!")
                break
            elif "=" in user_input:
                key, value = map(str.strip, user_input.split("=", 1))
                self.add_memory(key, value)
                print(f"Bot: I'll remember that {key} is {value}.")
            elif user_input.lower() == "memory":
                self.print_memory()
            else:
                memory_response = self.get_memory_response(user_input)
                if memory_response:
                    print("Bot:", memory_response)
                else:
                    predicted_response = self.chatbot_pipeline.predict([user_input])
                    print("Bot:", predicted_response[0])

# Create the chatbot instance
chatbot = MemoryChatbot()

# Predefined responses and training data
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm here to assist you!",
    "bye": "Goodbye! Have a great day!",
    "what's your name": "I'm a machine learning chatbot!",
    # Add more responses here
}

training_data = list(responses.keys())
labels = list(responses.values())

# Train the chatbot
chatbot.train_chatbot(training_data, labels)

# Start chatting
chatbot.chat()
