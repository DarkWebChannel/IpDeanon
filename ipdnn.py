#UTF-8
#pip install requests
#by KEF with love)
import requests

def get_ip_info(ip_address):
    try:
        # Отправляем запрос к сервису ipinfo.io для получения информации о IP-адресе
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()

        # Выводим географическое местоположение
        print(f"Географическое местоположение: {data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}")

        # Выводим информацию о провайдере
        print(f"Информация о провайдере: {data.get('org', '')}")

        # Выводим тип сети
        print(f"Тип сети: {data.get('org', '')}")

        # Выводим различные атрибуты
        print("Различные атрибуты:")
        print(f"- Часовой пояс: {data.get('timezone', '')}")
        print(f"- Координаты: {data.get('loc', '')}")
        print(f"- ASN: {data.get('asn', '')}")
        print(f"- Почтовый индекс: {data.get('postal', '')}")
        print(f"- Тип аппаратуры: {data.get('device', '')}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    ip_address = input("Введите IP адрес: ")
    get_ip_info(ip_address)