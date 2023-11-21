import os
import json
import requests
from http import HTTPStatus

def main(params):
  pin_user = os.environ.get('PINBOARD_USER')
  pin_token = os.environ.get('PINBOARD_TOKEN')
  auth_token = f'{pin_user}:{pin_token}'
  api_url = 'https://api.pinboard.in/v1'
  get_all_tags = requests.get(f'{api_url}/tags/get?auth_token={auth_token}')
  
  
