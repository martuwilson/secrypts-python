import requests
from bs4 import BeautifulSoup


def main():
    sitio = "achirou.com"
    agent = {'User-Agent': 'Firefox'}
    url = f"https://viewdns.info/reverseip/?host={sitio}&t=1"

    response = requests.get(url, headers=agent)
    
    if response.status_code != 200:
        print("Error al acceder a la página.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la tabla de resultados
    table = soup.find("table", {"border": "1"})
    
    if not table:
        print("No se encontró la tabla con los dominios.")
        return

    for row in table.find_all("tr")[1:]:  # Omitimos el encabezado
        columns = row.find_all("td")
        if columns:
            print(f"Dominio alojado en el servidor: {columns[0].text.strip()}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
