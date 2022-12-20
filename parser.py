# Поиск вакансий
import requests
import pprint
import time

# url = 'https://api.hh.ru/vacancies'
#
# # выбор и списка
# # where = input('Где искать вакансию?')
# # текст
# # query_string = input('Строка запроса?')
#
# params = {
#     'text': 'NAME:Python',
#     # есть страницы т.к. данных много
#     'page': 1
# }
#
# result = requests.get(url, params=params).json()
#
# pprint.pprint(result)
# print(result['items'][0]['url'])
# print(result['items'][0]['alternate_url'])
#
# items = result['items']
# for item in items[:10]:
#     url = item['url']
#     result = requests.get(url).json()
#     # Ключевые скилы
#     print(result['key_skills'])
#     # задержка между запросами, чтобы не забанили
#     time.sleep(1)

# частотный анализ

key_skills = {}
skills = ['python', 'python', 'python', 'python', 'Django', 'python', 'Flask', 'python', 'SQL', 'SQL', 'python',
          'Flask']

for item in skills:
    # если он там уже есть
    if item in key_skills:
        # то мы его увеличиваем на 1
        key_skills[item] += 1
    else:
        # а если его там еще нет, то мы записываем со значением 1
        key_skills[item] = 1

print(key_skills)

# Сортровка кортежа по убываению
result = sorted(key_skills.items(), key=lambda x: x[1], reverse=True)
print(result)


# словарь в объект
class Vacancy:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


objs = []
vacansies = [{'name': 'python', 'salary': 200, 'url': ''}]
for item in vacansies:
    vacancy = Vacancy(item['name'], item['salary'])
    objs.append(vacancy)
    print(vacancy.name)
