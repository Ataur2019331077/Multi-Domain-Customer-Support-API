from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = FastAPI(title="Multi-Domain T5 Support API")

# Model configs
MODEL_CONFIGS = {
    "ecommerce": "Ataur77/ecommerce-customer-support",
    "medical": "Ataur77/medical-customer-support-t5",
    "restaurant": "Ataur77/restaurants-chatbot-t5",
    "classify": "Ataur77/customer-query-classify"
}

# Load all models and tokenizers
models = {}
tokenizers = {}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

for key, model_name in MODEL_CONFIGS.items():
    try:
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
        tokenizers[key] = tokenizer
        models[key] = model
        print(f"✅ Loaded model: {model_name}")
    except Exception as e:
        print(f"❌ Failed to load model {model_name}: {e}")

# Request schema
class Query(BaseModel):
    text: str

# Generic response generator
def generate_response(model_key: str, text: str):
    if model_key not in models or model_key not in tokenizers:
        raise HTTPException(status_code=404, detail=f"Model '{model_key}' not loaded.")
    
    tokenizer = tokenizers[model_key]
    model = models[model_key]
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)

    with torch.no_grad():
        output_ids = model.generate(
            inputs["input_ids"],
            max_length=150,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=2
        )

    result = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"model": model_key, "input": text, "output": result}

# --- API Endpoints ---

@app.post("/ecommerce")
async def ecommerce_support(query: Query):
    return generate_response("ecommerce", query.text)

@app.post("/medical")
async def medical_support(query: Query):
    return generate_response("medical", query.text)

@app.post("/restaurant")
async def restaurant_support(query: Query):
    return generate_response("restaurant", query.text)

@app.post("/classify")
async def query_classifier(query: Query):
    return generate_response("classify", query.text)

@app.get("/")
async def root():
    return {"message": "Use /ecommerce, /medical, /restaurant, or /classify endpoints with POST method and {text: 'your query'}"}
