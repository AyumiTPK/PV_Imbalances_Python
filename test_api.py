import pytest
import requests

BASE_URL = "https://api.tariffs.groupe-e.ch"
RESOURCE = "/v1/tariffs"
start_date = "2024-01-01T00:00:00+02:00"
end_date = "2024-12-31T23:59:59+02:00"

def test_tariff_api():
    url = f"{BASE_URL}{RESOURCE}"
    params = {
        "start_timestamp": start_date,
        "end_timestamp": end_date
    }
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 200  # Check for successful response
    
    try:
        data = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")
    
    assert len(data) > 0, "No data found"