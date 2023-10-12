from setuptools import setup, find_packages

# ATTENTION
# Don't forget to change name of your application,
# version and names of packages

APP_NAME = 'python-app-template'
PACKAGES = ['app', 'app.*']
VERSION = '0.0.0'

setup(
    name=APP_NAME,
    version=VERSION,
    packages=find_packages(include=PACKAGES)
)
