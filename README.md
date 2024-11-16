# FastAPI Server for ML Model Inference

This repository contains a FastAPI server for serving machine learning models, specifically using scikit-learn. The server loads a trained model from a `.pkl` file and exposes an API for inference.

## Prerequisites

- Python 3.7 or higher
- A trained model saved as a `.pkl` file (e.g., `model.pkl`)

## Setup Instructions

Follow these steps to get the server up and running locally.

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/4ddx/IDS_pythonServer.git
cd IDS_pythonServer
```
Once inside the cloned directory, install the required Python dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```
After cloning the repository, make sure to have your trained model file (model.pkl) in the root directory of the project (i.e., the same directory as this README.md file).

Make sure to also load CIC-IDS-2017 Dataset using read_csv

The FastAPI app exposes an API endpoint at /predict where you can send POST requests with data for inference.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
    "Bwd_Packet_Length_Mean": 0.0,
    "Bwd_Packet_Length_Std": 0.0,
    "Fwd_IAT_Std": 0.0,
    "Fwd_IAT_Max": 10011.0,
    "Packet_Length_Std": 3.0,
    "Avg_Bwd_Segment_Size": 0.0,
    "Idle_Max": 0.0
}'
```

You can also use Postman on port 8000/predict/:

Sample Params as Raw: 
```bash
{
    "Bwd_Packet_Length_Mean": 0.0,
    "Bwd_Packet_Length_Std": 0.0,
    "Fwd_IAT_Std": 0.0,
    "Fwd_IAT_Max": 10011.0,
    "Packet_Length_Std": 3.0,
    "Avg_Bwd_Segment_Size": 0.0,
    "Idle_Max": 0.0
}
```
