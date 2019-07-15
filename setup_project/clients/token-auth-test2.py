import requests


def client():
    data = {
        'username': 'resttest',
        'email': 'test@email.com',
        'password1': 'koblihaaaa',
        'password2': 'koblihaaaa'
    }

    url = 'http://127.0.0.1:8000/api/rest-auth/registration/'
    response = requests.post(url,
                             data=data)

    # token_header = 'Token f4c3cdd7c188a8a8a23fd5fc3fabfc507e4b388d'
    # headers = {'Authorization': token_header}
    #
    # response = requests.get('http://127.0.0.1:8000/profileapi/profiles/',
    #                         headers=headers)

    print('Status code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if (__name__ == '__main__'):
    client()
