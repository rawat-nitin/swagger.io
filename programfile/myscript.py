import requests
import json


def fetch_swagger_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        swagger_json = response.json()
        return swagger_json
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Swagger JSON: {e}")
        return None


def main():
    # Example URL: http://petstore.swagger.io/v2/swagger.json
    swagger_url = input("Enter the URL of the Swagger JSON: ")

    swagger_json = fetch_swagger_json(swagger_url)

    if swagger_json:
        # Perform actions with the Swagger JSON
        # For example, you can print the JSON content
        print(json.dumps(swagger_json, indent=2))


if __name__ == "__main__":
    main()

