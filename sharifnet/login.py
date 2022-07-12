import argparse
import requests

from sharifnet.user import User


def login(username: str, password: str):
    data = dict(
        username=username,
        password=password
    )
    response = requests.post('https://net2.sharif.edu/login', data=data)
    if response.status_code != 200:
        raise Exception(f'Login failed: {response.status_code}')
    try:
        requests.get('https://google.com')
    except Exception:
        raise Exception('Login failed: no internet connection')

def main():
    parser = argparse.ArgumentParser(description='Login to net2.sharif.edu')
    parser.add_argument('--username', '-u', help='Username')

    args = parser.parse_args()

    if args.username:
        user = User.get(User.username == args.username)
        return login(user.username, user.password)

    user = User.get(User.is_default == True)
    return login(user.username, user.password)
