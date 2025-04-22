
import requests

def fetch_random_user():
    url = "https://freeapi.miniprojectideas.com/api/amazon/GetAllSaleByCustomerId"
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        print(response.json())

        
        # Validate the keys in the response
        if data.get("access") and "date" in data:
            user_date = data["date"]
            username = user_date.get("login", {}).get("username", "Unknown")
            country = user_date.get("location", {}).get("country", "Unknown")
            return username, country
        else:
            raise Exception("Failed to fetch user data: Missing keys in response.")
    else:
        raise Exception(f"Failed to fetch user data: HTTP {response.status_code}")

def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
