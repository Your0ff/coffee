import requests


def get_response(url: str) -> requests.Response:
    r = requests.get(url)
    return r


def response_validation(response: requests.Response) -> bool:
    if response.status_code == 200:
        return True
    else:
        return False


def get_picture(response: requests.Response) -> str:
    data = response.json()
    return data['file']

print('Приветствую, хотите сгенерировать картинку кофе? (y/n)')
inp = input()
while inp.lower() == 'y':
    url = "https://coffee.alexflipnote.dev/random.json"
    print("Отправляем запрос и получаем ответ...")
    resp = get_response(url)
    if not response_validation(resp):
        print("Ошибка запроса")
    else:
        print("Ответ получен")
        print(get_picture(resp))
    print("Сгенерировать ещё одну? (y/n)")
    inp = input()
print('ББ')

