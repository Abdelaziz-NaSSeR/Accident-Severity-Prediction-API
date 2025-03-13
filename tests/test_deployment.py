import requests

# Define the base URL of the API
BASE_URL = "http://127.0.0.1:8000"

def test_health_check():
    """Test the /health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    print("✅ Health Check Passed!")

def test_prediction():
    """Test the /predict endpoint with valid input"""
    sample_input = {
        "Number_of_Vehicles": 2,
        "Time_24hr": 14.5,
        "First_Road_Class": 1,
        "Road_Surface": 2,
        "Lighting_Conditions": 1,
        "Weather_Conditions": 3,
        "Casualty_Severity": 1,
        "Sex_of_Casualty": 1,
        "Age_of_Casualty": 25.0,
        "Type_of_Vehicle": 3,
        "age_group": 2,
        "vehicle_group": 1
    }
    response = requests.post(f"{BASE_URL}/predict", json=sample_input)
    
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())  # Print response details
    
    assert response.status_code == 200
    result = response.json()
    assert "prediction" in result
    print(f"✅ Prediction Passed! Output: {result}")

def test_invalid_input():
    """Test the /predict endpoint with invalid input"""
    invalid_input = {
        "Number_of_Vehicles": "invalid",  # Wrong data type
        "Time_24hr": 25.0,  # Invalid time (outside 0-24 range)
        "First_Road_Class": 1,
        "Road_Surface": 2,
        "Lighting_Conditions": 1,
        "Weather_Conditions": 3,
        "Casualty_Severity": 1,
        "Sex_of_Casualty": 1,
        "Age_of_Casualty": 25.0,
        "Type_of_Vehicle": 3,
        "age_group": 2,
        "vehicle_group": 1
    }
    response = requests.post(f"{BASE_URL}/predict", json=invalid_input)
    
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())  # Print error details
    
    assert response.status_code == 422  # 422 Unprocessable Entity for validation errors
    print("✅ Invalid Input Handling Passed!")

if __name__ == "__main__":
    test_health_check()
    test_prediction()
    test_invalid_input()