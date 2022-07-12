import argparse
import getpass

from sharifnet.user import User


def main():
    parser = argparse.ArgumentParser(description='Add a new user to the database.')
    parser.add_argument('--default', '-d', action='store_true', help='Make the new user the default user.')

    args = parser.parse_args()

    username = input('Username: ')
    password = getpass.getpass()

    if args.default:
        try:
            User.get(User.is_default == True).update(is_default=False)
        except User.DoesNotExist:
            pass

    User.create(username=username, password=password, is_default=args.default)
