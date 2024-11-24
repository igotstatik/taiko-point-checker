import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "addresses.txt")

with open(file_path, "r") as file:
    addresses = [line.strip() for line in file.readlines()]

driver = webdriver.Chrome()


results = []
for address in addresses:
    url = f"https://trailblazers.taiko.xyz/profile/{address}"
    driver.get(url)

    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    element = soup.find('div', class_='font-clash-grotesk font-semibold text-[45px] leading-none')

    if element:
        points = element.get_text(strip=True)
    else:
        points = "Элемент не найден"

    results.append(f"{address} - {points}")

driver.quit()

for result in results:
    print(result)
