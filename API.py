import requests

api_url = "https://engine.lifeis.porn/api/millionaire.php?qType=1&count=1"
response = requests.get(api_url)

if response.status_code == requests.codes.ok:
  question = response.json()['data'][0]['question']
  print(question)
  answers = response.json()['data'][0]['answers']
  right_answer = answers[0]

  print("Варианты ответов:")
  print(answers[0])
  print(answers[1])
  print(answers[2])
  print(answers[3])





else:
  print("Проблемы на сервере")
