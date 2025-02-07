# app/ai_utils.py
from transformers import AutoTokenizer, AutoModelForCausalLM
from gpt4all import GPT4All

class TextAnalysisTool:
    def __init__(self, model_type="tinyllama", model_path=None):
        if model_type == "tinyllama":
            self.tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
            self.model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        elif model_type == "gpt4all":
            self.model = GPT4All(model_path)  # Path to GPT4All model file

    def generate_description(self, text):
        prompt = f"Analyze the following text and provide a concise summary:\n{text}"
        if isinstance(self.model, GPT4All):
            return self.model.generate(prompt, max_tokens=100)
        else:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_length=100)
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)