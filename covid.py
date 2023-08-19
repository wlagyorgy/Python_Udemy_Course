import requests
from bs4 import BeautifulSoup

def get_covid_stats():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", id="main_table_countries_today")
        print(table)

        # Az első sor az oszlopfejléceket tartalmazza, kihagyjuk azt
        rows = table.find_all("tr")[1:]

        for row in rows:
            columns = row.find_all("td")
            country = columns[0].text.strip()
            total_cases = columns[1].text.strip()
            total_deaths = columns[3].text.strip()
            total_recovered = columns[5].text.strip()

            print(f"Ország: {country}, Összes esetszám: {total_cases}, Halálozások: {total_deaths}, Gyógyultak: {total_recovered}")
    else:
        print("Hiba történt a letöltés közben.")

if __name__ == "__main__":
    get_covid_stats()
