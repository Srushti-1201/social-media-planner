import requests

response = requests.get('http://127.0.0.1:8000/')
print('Status:', response.status_code)
print('Content-Type:', response.headers.get('Content-Type'))
print('Has React root div:', 'id="root"' in response.text)
print('Has static assets:', '/static/assets/' in response.text)
