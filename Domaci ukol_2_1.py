import requests

def get_company_info_by_ico():

    ico = input("Zadejte IČO subjektu: ")

    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            obchodni_jmeno = data.get('obchodniJmeno', 'Není k dispozici')
            adresa = data.get('adresa', 'Není k dispozici')

            if isinstance(adresa, dict):
                adresa_text = f"{adresa.get('ulice', '')} {adresa.get('cisloDomovni', '')}, {adresa.get('mesto', '')}, {adresa.get('psc', '')} {adresa.get('obec', '')}"
            else:
                adresa_text = 'Adresa není k dispozici'

            print(f"Obchodní jméno: {obchodni_jmeno}")
            print(f"Adresa sídla: {adresa_text}")
        else:
            print("Nastala chyba při získávání dat. Zkontrolujte IČO.")
    except requests.exceptions.RequestException as e:
        print(f"Chyba při připojování k API: {e}")

get_company_info_by_ico()