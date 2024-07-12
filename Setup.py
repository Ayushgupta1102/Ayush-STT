# pip install setuptools
from setuptools import setup,find_packages

setup(
    name = 'Ayush-STT',
    version = 0.1,
    author = 'Ayush Gupta',
    author_email = 'ayushgupta12292@gmail.com',
    description = 'This is Speech to text package by Ayush gupta...'
)
packages = find_packages(),
install_requirement = [
    'selenium',
    'Webdrivers_manager'
]

