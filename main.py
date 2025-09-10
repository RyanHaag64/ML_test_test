from fastapi import FastAPI, Request
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Initialize Firebase
cred = credentials.Certificate("guardian-4beba-firebase-adminsdk-fbsvc-4a899dd440.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

@app.post("/predict")
async def receive_prediction(request: Request):
    data = await request.json()

    if "timestamp" not in data:
        data["timestamp"] = datetime.datetime.utcnow().isoformat()

    db.collection("predictions").add(data)

    return {"status": "ok", "data": data}
