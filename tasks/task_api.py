import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder(folder_name, token):
    """Создаёт папку на Яндекс.Диске"""
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name}
    response = requests.put(BASE_URL, headers=headers, params=params)
    return response

def delete_folder(folder_name, token):
    """Удаляет папку на Яндекс.Диске"""
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name}
    response = requests.delete(BASE_URL, headers=headers, params=params)
    return response