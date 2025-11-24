import json

person_str='{"name":"Anıl","languages":["Türkçe","İngilizce"]}'
result=json.loads(person_str) #String to Dict
result=json.dumps(result)     #Dict to String
print(type(result))
print(result)