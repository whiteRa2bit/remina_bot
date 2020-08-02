from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

requirements = [
]

setup(
    name='organizer_bot',
    version='0.1',
    description='Organizer Telegram Bot',
    license="Apache License 2.0",
    long_description=long_description,
    author='Pavel Fakanov',
    author_email='pavel.fakanov@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
)