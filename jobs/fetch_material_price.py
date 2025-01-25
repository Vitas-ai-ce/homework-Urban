import requests
from bs4 import BeautifulSoup

def fetch_material_prices():
    # URL веб-сайта с ценами на электромонтажные материалы
    url = "https://om-ek.ru/product/elektromontazhnyie-materialyi"
    # Замените этот URL на реальный

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP

        # Парсинг HTML-страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы, содержащие информацию о материалах
        # Ниже приведены примеры, замените их на реальные селекторы в зависимости от структуры HTML
        materials = soup.find_all('div', class_='material-item')  # Пример класса элемента

        prices = {}

        for material in materials:
            name = material.find('h2', class_='material-name').text
            price = material.find('span', class_='material-price').text

            # Преобразуйте цену в числовой формат, если необходимо
            prices[name] = price.strip()

        return prices

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return {}

def main():
    prices = fetch_material_prices()
    if prices:
        print("Актуальные цены на материалы для электромонтажа:")
        for name, price in prices.items():
            print(f"{name}: {price}")
    else:
        print("Не удалось получить данные о ценах.")

if __name__ == "__main__":
    main()
