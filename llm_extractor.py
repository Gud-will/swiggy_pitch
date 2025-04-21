import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def extract_using_llm(text):
    tokenizer = AutoTokenizer.from_pretrained("teapotai/teapotllm")
    model = AutoModelForSeq2SeqLM.from_pretrained("teapotai/teapotllm")
    # Put model on appropriate device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Prepare prompt for T5 (this is key)
    prompt = f"Extract food items with their quantities from the following sentence:\n{text}"

    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt", padding=True).to(device)

    # Generate response
    outputs = model.generate(
        **inputs,
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

    # Decode and print the result
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("T5 Output:", response)
    return response

if __name__ == "__main__":
    extract_using_llm("i want ashirvad atta, amul butter and maybe some lays chips 100gms of ladys finger and 250gms of cheese")