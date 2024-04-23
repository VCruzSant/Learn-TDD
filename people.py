import requests


class People:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_all_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if response.ok:
            return 'CONECTED'
        else:
            return 'ERROR 404'
