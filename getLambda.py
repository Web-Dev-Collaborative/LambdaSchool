import requests

payload = {"name":"Emily", "lastname":"Sperry", "email":"sperrye@gmail.com", "message":"Hey, I did it!"}

r = requests.post('https://lambdaschool.com/contact-form',json=payload)

print r.text
