from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_descriptions(frames):
    descriptions = []
    for frame in frames:
        objects = detect_objects(frame)
        description = generate_text(objects)
        descriptions.append(description)
    
    return descriptions

def generate_text(objects):
    # Example: use GPT model to generate natural language descriptions
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    
    prompt = f"The scene contains {', '.join(objects)}"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    outputs = model.generate(inputs, max_length=50)
    description = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return description
