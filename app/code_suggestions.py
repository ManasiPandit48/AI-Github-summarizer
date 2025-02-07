# app/code_suggestions.py
from transformers import AutoTokenizer, AutoModelForCausalLM

class CodeSuggestionTool:
    def __init__(self, model_path="bigcode/starcoderbase-1b"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def suggest_code_improvements(self, code_snippet):
        prompt = f"Analyze the following code snippet and suggest improvements:\n{code_snippet}"
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)