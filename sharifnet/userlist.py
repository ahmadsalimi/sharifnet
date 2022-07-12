from sharifnet.user import User


def main():
    users = User.select()
    for user in users:
        print(f'{user.username}{" (default)" if user.is_default else ""}')
