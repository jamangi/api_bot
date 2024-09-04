import requests


def get_request(api_link):
    response = requests.get(api_link)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def post_request(api_link, payload):
    response = requests.post(api_link, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"status code: {response.status_code}")


def put_request(api_link, payload):
    response = requests.put(api_link, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"status code: {response.status_code}")


def delete_request(api_link, payload):
    response = requests.delete(api_link, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"status code: {response.status_code}")


if __name__ == '__main__':
    # Example usage
    api_link = "https://chathub-18oc.onrender.com/api/messages"
    data = get_request(api_link)
    print(data)
