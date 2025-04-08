import requests
import json

def vyhledat_subjekty(nazev_subjektu):

    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = json.dumps({"obchodniJmeno": nazev_subjektu})

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_data = response.json()
        pocet = json_data.get("pocetCelkem", 0)

        print(f"Nalezeno subjektů: {pocet}")

        if pocet > 0:
            subjekty = json_data.get("ekonomickeSubjekty", [])
            for subjekt in subjekty:
                jmeno = subjekt.get("obchodniJmeno", "Neznámé")
                ico = subjekt.get("ico", "Neznámé")
                print(f"{jmeno}, {ico}")
        else:
            print("Žádné subjekty nenalezeny.")
    else:
        print("Chyba při odesílání požadavku.")

if __name__ == "__main__":
    nazev_subjektu = input("Zadejte název subjektu: ")
    vyhledat_subjekty(nazev_subjektu)