from django.test import TestCase
import requests

a = requests.get('127.0.0.1:8000/cou/')
print(a.json())
