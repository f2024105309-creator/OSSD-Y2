import requests
from bs4 import BeautifulSoup
import csv

def get_cars_data(car):
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    cars = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        if not tables:
            print("No tables found on the webpage.")

        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cols = row.find_all('td')

                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    cars.append({'name': name, 'price': price})

    else:
        print("Failed to retrieve the webpage.")

    return cars


# ✅ Wrapper function (optional but good for structure)
def scrapper(car):
    data = get_cars_data(car)
    return data


# ✅ Save data to CSV file
def save_to_file(data, filename="cars.csv"):
    if not data:
        print("No data to save")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")