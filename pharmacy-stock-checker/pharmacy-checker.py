from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def check_ktomalek(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        page.wait_for_selector("#rodzajeAptek", timeout=15000)
        div_content = page.query_selector("#rodzajeAptek").inner_html()

        soup = BeautifulSoup(div_content, 'html.parser')
        results = soup.find_all('div', class_='results-item')

        for result in results[:9]:
            pharmacy_name = result.find('span', {'data-sens': '1'}).get_text(strip=True)
            distance = result.find('b', {'class': 'c:orange'}).get_text(strip=True)

            stock_info = result.find('div', class_='la-lek-ilosc')
            if stock_info and 'niedostępne' not in stock_info.get_text():
                print(f"Pharmacy: {pharmacy_name}, distance: {distance}")

        browser.close()


def check_gdziepolek(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        no_pharmacies_msg = page.query_selector("p.MuiTypography-root.MuiTypography-body1")
        if no_pharmacies_msg and "Brak aptek z produktem na stanie dla wybranej lokalizacji." in no_pharmacies_msg.inner_text():
            print("No pharmacies found for this product at the selected location.")
            browser.close()
            return

        div_content = page.query_selector("#pharmacies-list").inner_html()

        soup = BeautifulSoup(div_content, 'html.parser')
        pharmacies = soup.find_all('li', class_='MuiListItem-root')
        pharmacy_info = []
        for pharmacy in pharmacies:
            name_tag = pharmacy.find('a', class_=lambda x: x and 'MuiTypography-root MuiTypography-h2' in x)
            location_tag = pharmacy.find('p', class_=lambda x: x and 'MuiTypography-root MuiTypography-body1' in x)

            if name_tag and location_tag:
                name = name_tag.get_text(strip=True)
                location = location_tag.get_text(strip=True)
                pharmacy_info.append((name, location))

        for name, location in pharmacy_info:
            print(f"Pharmacy: {name}, Location: {location}")

        browser.close()


print("Kto ma lek:")
check_ktomalek("")
print("\nGdzie po lek")
check_gdziepolek("")
