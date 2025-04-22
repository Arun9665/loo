import requests

def fectch_random_user():
    url = "https://freeapi.miniprojectideas.com/api/amazon/GetAllSaleByCustomerId"
    response = requests.get(url)
    date = response.json()
    #print(response.json())


    if date ["access"] and "date" in date:
        user_date = date["date"]
        username = user_date["login"] ["username"]
        country = user_date["location"] ["country"]
        return username, country
    else:
        raise Exception("faild to fetch user")
    
def main():
    try:
        username, country = fectch_random_user()
        print(f"username: {username} \n country: {country}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()