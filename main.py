import torch
from omegaconf import OmegaConf
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

class ToxicityClassification:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path)

    def __call__(self, message):
        inputs = self.tokenizer(message, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        probabilities = torch.sigmoid(logits)[0]
        toxic_score = probabilities[0].item()
        
        if toxic_score > 0.5:
            return "toxic"
        else:
            return "safe"

classifier = ToxicityClassification("./config.yaml")

app = FastAPI(title="Hệ thống kiểm duyệt ngôn từ bằng tiếng Anh")

app.add_middleware(
    CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'],
)

@app.get("/")
def home():
    return {"message": "Chào mừng đến với API chạy mô hình unitary/toxic-bert"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post('/predict')
async def predict_toxicity(message: str):
    result = classifier(message)
    return {
        "text": message,
        "is_toxic": True if result == 'toxic' else False,
        "label": result
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
