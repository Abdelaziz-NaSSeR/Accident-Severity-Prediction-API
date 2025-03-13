# Model Deployment Assignment

## Setup

1. Clone the repository: git clone https://github.com/Abdelaziz-NaSSeR/Accident-Severity-Prediction-API-FastAPI-.git
                         cd Accident-Severity-Prediction-API-FastAPI-
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the API: `python api/app.py`.

## API Endpoints

- `GET /health`: Health check endpoint.
- `POST /predict`: Prediction endpoint. Expects JSON input with key 'input' and an array of 4 numbers.

## Model Performance

- Accuracy: 0.96
- Precision: 0.95
- Recall: 0.96

## Testing

Run tests using: `python tests/test_deployment.py`.