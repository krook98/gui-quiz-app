import requests


amount_and_type = {
    'amount': 10,
    'type': 'boolean',
    'category': 18
}
response = requests.get('https://opentdb.com/api.php', params = amount_and_type)
response.raise_for_status()
data = response.json()
question_data = data['results']

