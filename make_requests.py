import requests

local_url = "http://localhost:9696/predict"
heroku_url = "https://insurance-forecast.herokuapp.com/predict"

info = {
    "age": 19,
    "sex": "female",
    "bmi": 25,
    "children": 1,
    "smoker": "no",
    "region": "northwest"
}

def request_prediction(url):
    response = requests.post(url, json = info)
    result = response.json()
    return result

if __name__ == "__main__":
    while True:
        selection = input(f'Do you want to test it locally or on the cloud?\n1 - Locally\n2 - On the cloud\n')

        if selection == '1':
            print(f'Making a POST request to "{local_url}"...')
            print(f'Result:')
            print(request_prediction(local_url))
            break
        
        elif selection == '2':
            print(f'Making a POST request to "{heroku_url}"...')
            print(f'Result:')
            print(request_prediction(heroku_url))
            break
        
        else:
            print(f'\nPlease choose "1" or "2".\n')