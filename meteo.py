



from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES = ['Wrocław','Opole','Zakopane']     # cities which u want to check
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'      # public API data( meteo)
    response = get(url)
    rows = [
        ['Miasto','Godzina pomiaru','Temperatura','Cisnienie','Kierunek wiatru','predkosc wiatru','suma opadu','data'] # information which u want to have
    ]

    # preparing rows for our API data
    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie'],
                row['kierunek_wiatru'],
                row['predkosc_wiatru'],
                row['suma_opadu'],
                row['data_pomiaru']
            ])
    table = AsciiTable(rows)     #creating table
    print(table.table)

    #2xx- wszystko jest ok
    #3xx-przekierowanie
    #4xx-uzytkownik cos zepsul
    #5xx-cos sie stalo po stronie serwera

if __name__ =='__main__':             #starting function
    print("pogodynka")
    main()

