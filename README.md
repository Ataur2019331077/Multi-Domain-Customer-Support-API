# 🧠 Multi-Domain Customer Support API (T5-based)

This FastAPI project provides a **unified interface** to multiple domain-specific NLP models fine-tuned using [T5 (Text-To-Text Transfer Transformer)](https://huggingface.co/docs/transformers/model_doc/t5). The API supports classification, question answering, and natural language understanding for various domains including **e-commerce**, **healthcare**, **restaurants**, and **query categorization**.

## 🚀 Deployed Models

| Domain        | Hugging Face Model | Description |
|---------------|--------------------|-------------|
| 🛍️ E-commerce Support | [`Ataur77/ecommerce-customer-support`](https://huggingface.co/Ataur77/ecommerce-customer-support) | Answers customer queries about orders, refunds, and product issues. |
| 🏥 Medical Support | [`Ataur77/medical-customer-support-t5`](https://huggingface.co/Ataur77/medical-customer-support-t5) | Assists patients with hospital procedures, insurance, and department queries. |
| 🍽️ Restaurant Chatbot | [`Ataur77/restaurants-chatbot-t5`](https://huggingface.co/Ataur77/restaurants-chatbot-t5) | Helps users with booking, location, parking, and facilities inquiries. |
| 🏷️ Query Classifier | [`Ataur77/customer-query-classify`](https://huggingface.co/Ataur77/customer-query-classify) | Categorizes user complaints or questions (e.g., refund issue, delivery delay). |

---

## 📦 Project Structure
```
.
├── main.py # FastAPI app with 4 endpoints
├── requirements.txt # Dependencies
└── README.md # This documentation
```


---

## ⚙️ Setup Instructions

1. **Clone the repository** (if hosted):
```bash
git clone https://github.com/Ataur2019331077/Multi-Domain-Customer-Support-API.git
cd Multi-Domain-Customer-Support-API
```
2. **Install dependencies:**
```
pip install -r requirements.txt
# Or individually
pip install fastapi uvicorn transformers torch sentencepiece
```

3. **Run the FastAPI app:**
```
uvicorn main:app --reload
```
Access the interactive Swagger UI:
Visit: `http://127.0.0.1:8000/docs`

## 📨 API Endpoints
Each endpoint accepts a POST request with a JSON payload:
```
{
  "text": "Your question or statement here"
}
```
1. 🛍️ `/ecommerce`
- Purpose: Ask product/order-related questions

- Model: `Ataur77/ecommerce-customer-support`
```
curl -X POST http://127.0.0.1:8000/ecommerce -H "Content-Type: application/json" -d '{"text": "What is the status of my order?"}'
```
2. 🏥 `/medical`
- Purpose: Hospital inquiries like insurance, departments, and timings

- Model: `Ataur77/medical-customer-support-t5`
```
curl -X POST http://127.0.0.1:8000/medical -H "Content-Type: application/json" -d '{"text": "Can I get ENT insurance support?"}'
```
3. 🍽️ `/restaurant`
- Purpose: Restaurant facilities and booking inquiries

- Model: `Ataur77/restaurants-chatbot-t5`
```
curl -X POST http://127.0.0.1:8000/restaurant -H "Content-Type: application/json" -d '{"text": "Do you offer parking?"}'
```
4. 🏷️ `/classify`
- Purpose: Classify user query into categories (e.g., refund, complaint)

- Model: `Ataur77/customer-query-classify`
```
curl -X POST http://127.0.0.1:8000/classify -H "Content-Type: application/json" -d '{"text": "I did not receive my refund"}'
```
## 🧠 How It Works
- Each model is a fine-tuned version of T5, capable of handling text-to-text tasks.

- Text input is tokenized and passed through the model using beam search to improve response quality.

- The FastAPI app handles multiple models in memory and routes queries to the correct model based on the endpoint.

## 🧪 Example Use Case Scenarios
- `E-commerce:`
    - **Input:** 
    ```
    "How do I return a damaged product?"
    ```
    - **Output:**
    ```
    {
        "model": "ecommerce",
        "input": "How do I return a damaged product?",
        "output": "Returns | Medium"
    }
    ```

- `Medical`
    - **Input:** 
    ```
    "How do I proceed with insurance claim assistance in ENT?"
    ```
    - **Output:**
    ```
    {
        "model": "medical",
        "input": "How do I proceed with insurance claim assistance in ENT?",
        "output": "Insurance Claim Assistance | ENT | Emergency"
    }
    ```
- `Restaurant:`
    - **Input:** 
    ```
    "Can I make a reservation for tonight?"
    ```
    - **Output:**
    ```
    {
        "model": "restaurant",
        "input": "Can I make a reservation for tonight?",
        "output": "Yes, you can book by calling our hotline."
    }
    ```
- `Classifier:`
    - **Input:** 
    ```
    "I haven’t received my refund yet."
    ```
    - **Output:**
    ```
    {
        "model": "classify",
        "input": "I haven’t received my refund yet.",
        "output": "Refunds, Urgency: Low"
    }
    ```


## ✅ TODO / Improvements
- [ ]Add Docker support for deployment

- [ ]Add streaming/token-level response generation (for chatbots)

- [ ]Support multilingual queries

- [ ]Add feedback endpoint for improving model performance



## 📄 License
This project is licensed under the [MIT License](./LICENSE)