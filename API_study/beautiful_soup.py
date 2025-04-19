import requests
import json

SEARCHAPI_KEY = "tZpMw1YcE2Tc9cUPYvo5j11f"

def search_images_via_searchapi(query, api_key, max_results=10):
    endpoint = "https://www.searchapi.io/api/v1/search"
    
    params = {
        "engine": "google_images",
        "q": query,
        "num": max_results,
        "api_key": api_key
    }

    try:
        print(f"Making API call to {endpoint} with params: {params}")
        response = requests.get(endpoint, params=params, timeout=15)
        print(f"Response status code: {response.status_code}")
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Attempt to parse JSON
        try:
            data = response.json()
            print("Raw API response:", json.dumps(data, indent=2))  # Debugging
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            print("Raw response content:", response.text)
            return []

        # Check for API errors
        if data.get("error"):
            print(f"API Error: {data.get('error', {}).get('message')}")
            return []

        # Extract image URLs
        image_results = data.get("images_results", [])
        if not image_results:
            print("No images_results found in response")
            print("Available keys:", data.keys())
            
        return [result["original"] for result in image_results[:max_results]]

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")
        return []
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return []

if __name__ == "__main__":
    query = "fashion outfits"
    
    if not SEARCHAPI_KEY:
        raise ValueError("SEARCHAPI_KEY environment variable not set")
    
    print("Starting image search...")
    image_urls = search_images_via_searchapi(query, SEARCHAPI_KEY)
    
    if not image_urls:
        print("No image URLs received. Potential issues:")
        print("1. Invalid/missing API key")
        print("2. SearchAPI.io plan limitations")
        print("3. Network/firewall restrictions")
        print("4. SearchAPI.io service outage")
        print("Check your dashboard: https://www.searchapi.io/dashboard")
    else:
        print(f"Found {len(image_urls)} image URLs")
        # Rest of download code...