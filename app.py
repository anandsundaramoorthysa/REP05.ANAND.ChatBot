from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import logging

app = Flask(__name__)

# Configuration
model_names = {
    "gpt2-medium": "gpt2-medium",
    "gpt2-large": "gpt2-large",
}

current_model_name = "gpt2-medium"
model_dir = os.getenv('MODEL_DIR', 'D:/Machine_Learning_DiffuseAi/Project/chatbot/models/')

# Predefined responses
simple_responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "hey": "Hey!",
    "how are you?": "I'm fine, thank you!",
    "what's up?": "Not much, just here to help you.",
    "who are you?": "I'm an AI Chatbot.",
    "what do you do?": "I assist with your questions and provide information.",
    "what can you do?": "I can help answer questions, provide information, and have a chat.",
    "what's your name?": "I don't have a name, but you can call me Chatbot.",
    "how old are you?": "I don't have an age. I'm always here to assist you.",
    "where are you from?": "I exist in the digital realm.",
    "what do you like?": "I enjoy helping people with their queries.",
    "what do you love?": "I love to assist and provide useful information.",
    "what's your favorite color?": "I don't have preferences, but I’m here to help with any color-related questions.",
    "what's your favorite food?": "I don't eat, but I can help you with recipes or food-related queries.",
    "can you help me?": "Of course! What do you need help with?",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "goodbye": "Goodbye! Have a great day!",
    "bye": "Bye! Take care!",
    "see you later": "See you later!",
    "where are you?": "I am Virtual Assistant!",
}

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_model_exists(model_name):
    model_path = os.path.join(model_dir, model_name)
    if not os.path.exists(model_path):
        os.makedirs(model_path, exist_ok=True)
        logger.info(f"Downloading and saving {model_name} to {model_path}...")
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=model_path)
            model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=model_path)
            logger.info(f"{model_name} downloaded and saved successfully.")
        except Exception as e:
            logger.error(f"Error downloading model {model_name}: {str(e)}")
    else:
        logger.info(f"{model_name} already exists at {model_path}.")

def load_model(model_name):
    model_path = os.path.join(model_dir, model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=model_path)
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=model_path)
    return tokenizer, model

# Ensure models are downloaded
for name in model_names.values():
    ensure_model_exists(name)

# Load the default model
tokenizer, model = load_model(current_model_name)

@app.route('/')
def home():
    return render_template('index.html', model_name=current_model_name)

@app.route('/change_model', methods=['POST'])
def change_model():
    global current_model_name, tokenizer, model
    selected_model_name = request.form.get('model_name')

    if selected_model_name in model_names:
        try:
            current_model_name = selected_model_name
            tokenizer, model = load_model(current_model_name)
            return jsonify({'status': 'success', 'model_name': current_model_name})
        except Exception as e:
            logger.error(f"Error loading model {selected_model_name}: {str(e)}")
            return jsonify({'status': 'error', 'message': f'Error loading model: {str(e)}'})
    else:
        return jsonify({'status': 'error', 'message': 'Model not found'})

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form.get('input_text', '').strip()

    # Convert input text to lowercase to match predefined responses
    input_text_lower = input_text.lower()

    if input_text_lower in simple_responses:
        generated_text = simple_responses[input_text_lower]
    else:
        try:
            inputs = tokenizer(input_text, return_tensors='pt')
            outputs = model.generate(inputs['input_ids'], max_length=150)
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            generated_text = f"Error generating text: {str(e)}"
    
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
