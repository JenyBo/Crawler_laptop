import requests
from bs4 import BeautifulSoup
import csv

# Set the User-Agent header to look like a modern browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
}

def scrape_laptop_data(url, headers):
    data_list = []

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all(class_='main-contain')
            href_products = []

            for product in products:
                id = product.get('data-id')
                if id:
                    full_url = f'https://www.dienmayxanh.com/Product/GetGalleryItemInPopup?productId={id}&isAppliance=false&galleryType=5&colorId=0'
                    href_products.append(full_url)

            for href_product in href_products:
                newResponse = requests.get(href_product, headers=headers)
                if newResponse.status_code == 200:
                    soup = BeautifulSoup(newResponse.content, 'html.parser')
                    infors = soup.select('li')
                    data = {}
                    for li in infors:
                        p_element = li.find('p')
                        span_element = li.find('span')
                        if p_element and span_element:
                            p_text = p_element.get_text(strip=True)
                            span_text = span_element.get_text(strip=True)
                            data[p_text] = span_text
                    data_list.append(data)

            view_more_button = soup.find('div', class_='view-more')
            if view_more_button:
                url = 'https://www.dienmayxanh.com' + view_more_button.find('a')['href']
            else:
                url = None
        else:
            print(f"Failed to fetch URL: {url}")
            break

    return data_list

def save_to_csv(data_list, filename):
    if not data_list:
        print("No data to save.")
        return

    # Extract fieldnames from the data_list
    fieldnames = set()
    for data in data_list:
        fieldnames.update(data.keys())

    # Write the data to a CSV file with 'utf-8-sig' encoding
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

    print(f'Data saved to {filename}')
    print(f'Total records: {len(data_list)}')

if __name__ == '__main__':
    url = 'https://www.dienmayxanh.com/laptop'
    data_list = scrape_laptop_data(url, headers)
    save_to_csv(data_list, 'laptop_data.csv')
