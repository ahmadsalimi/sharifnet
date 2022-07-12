from setuptools import setup, find_packages


with open("sharifnet/_version.py") as f:
    exec(f.read())

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='sharifnet',
    version=__version__,
    description='Manage Sharif University network login',

    url='https://github.com/ahmadsalimi/sharifnet',
    author='Ahmad Salimi',
    author_email='ahsa9978@gmail.com',

    packages=find_packages(),
    install_requires=requirements,

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    entry_points={
        'console_scripts': [
            'sharifnet-login=sharifnet.login:main',
            'sharifnet-adduser=sharifnet.adduser:main',
            'sharifnet-userlist=sharifnet.userlist:main',
        ],
    },
)
