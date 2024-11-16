import pickle
from pydantic import BaseModel
import numpy as np
from fastapi import FastAPI
import subprocess

with open("RandomForestClassifier.pkl", "rb") as file:
    model = pickle.load(file)
app = FastAPI()

class PredictionInput(BaseModel):
    Bwd_Packet_Length_Mean: float
    Bwd_Packet_Length_Std: float
    Fwd_IAT_Std: float
    Fwd_IAT_Max: float
    Packet_Length_Std: float
    Avg_Bwd_Segment_Size: float
    Idle_Max: float

@app.get("/")
async def read_root():
    return {"message": "Welcome, visit /predict to use Model API"}

@app.post("/predict/")
async def predict(input: PredictionInput):
    features = np.array([[input.Bwd_Packet_Length_Mean, input.Bwd_Packet_Length_Std, input.Fwd_IAT_Std, input.Fwd_IAT_Max, input.Packet_Length_Std, input.Avg_Bwd_Segment_Size, input.Idle_Max]])
    prediction = model.predict(features)
    result = "BENIGN" if prediction[0] == 0 else "MALICIOUS"
    if(result == "MALICIOUS"):
        await disable_wifi()
    return {"prediction": result}

async def disable_wifi():
    try:
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"], check=True)
        print("Wi-Fi disabled")
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"], check=True)
        return {"message": "Wi-Fi disabled"}
    except subprocess.CalledProcessError as e:
        return {"message": "Failed to disable Wi-Fi"}
