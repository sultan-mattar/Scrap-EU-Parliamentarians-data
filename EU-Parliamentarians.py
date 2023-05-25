import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.common.exceptions import NoSuchElementException

links = []
datas = []

executable_path = 'msedgedriver.exe'
driver = webdriver.Edge(executable_path)
driver.get("https://www.europarl.europa.eu/meps/en/full-list/all")
driver.maximize_window()
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")
filtered_links = [link.get_attribute('href') for link in links if re.match(r'^https://www\.europarl\.europa\.eu/meps/en/\d+$', str(link.get_attribute('href')))]
print(len(filtered_links))

for link in filtered_links:
    driver.get(link)
    time.sleep(15)
    
    try:
        image = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(1) > div > div > span > img')
        Image_ = image.get_attribute("src")
    except NoSuchElementException:
        Image_ = "No Image Found"

    try:
        Name = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.erpl_title-h1.mt-1 > span')
        Name_ = Name.text
    except NoSuchElementException:
        Name_ = "No Name Found"

    try:
        Group = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > h3')
        Group_ = Group.text
    except NoSuchElementException:
        Group_ = "NO Group Found"

    try:
        Status = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > p')
        Status_ = Status.text
    except NoSuchElementException:
        Status_ = "NO Status Found"

    try:
        Country = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.erpl_title-h3.mt-1.mb-1')
        match = re.search(r'\((.*?)\)', Country.text)
        Country_ = match.group(1) if match else "No Country Found"
    except NoSuchElementException:
        Country_ = "No Country Found"

    try:
        Party = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > h3')
        match = re.search(r'\((.*?)\)', Party.text)
        Party_ = match.group(1) if match else "No Party Found"
    except NoSuchElementException:
        Party_ = "No Party Found"

    try:
        Email = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_email.mr-2')
        Email_ = Email.get_attribute("href")
    except NoSuchElementException:
        Email_ = "No Email Found"

    try:
        Website = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_website.mr-2')
        Website_ = Website.get_attribute("href")
    except NoSuchElementException:
        Website_ = "No Website Found"

    try:
        Facebook = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_fb.mr-2')
        Facebook_ = Facebook.get_attribute("href")
    except NoSuchElementException:
        Facebook_ = "No Facebook Found"

    try:
        Twitter = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_twitt.mr-2')
        Twitter_ = Twitter.get_attribute("href")
    except NoSuchElementException:
        Twitter_ = "No Twitter Found"

    try:
        Youtube = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_youtube.mr-2')
        Youtube_ = Youtube.get_attribute("href")
    except NoSuchElementException:
        Youtube_ = "No Youtube Found"

    try:
        Instagram = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_instagram.mr-2')
        Instagram_ = Instagram.get_attribute("href")
    except NoSuchElementException:
        Instagram_ = "No Instagram Found"

    try:
        LinkedIn = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_linkedin.mr-2')
        LinkedIn_ = LinkedIn.get_attribute("href")
    except NoSuchElementException:
        LinkedIn_ = "No LinkedIn Found"

    try:
        Telegram = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > div.separator.separator-dotted.separator-1x.border-secondary.mb-3 > div > a.link_telegram.mr-2')
        Telegram_ = Telegram.get_attribute("href")
    except NoSuchElementException:
        Telegram_ = "No Telegram Found"
    

    try:
        DateofBirth = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > p:nth-child(6) > time')
        DateofBirth_ = DateofBirth.text
    except NoSuchElementException:
        DateofBirth_ = "No Date of Birth Found"

    try:
        LocationofBirth = driver.find_element(By.CSS_SELECTOR, '#presentationmep > div > div:nth-child(2) > div > div > p:nth-child(6) > span')
        LocationofBirth_ = LocationofBirth.text
    except NoSuchElementException:
        LocationofBirth_ = "No Location of Birth Found"

    try:
        Positions = driver.find_element(By.CSS_SELECTOR, '#website-body > section.mt-5.mb-3 > div > div > div.col-xl-8.col-md-12 > div.erpl_meps-status-list')
        Positions_ = Positions.text
    except NoSuchElementException:
        Positions_ = "No Positions Found"

    try:
        Activities = driver.find_element(By.CSS_SELECTOR, '#website-body > section.mt-5.mb-3 > div > div > div.col-xl-8.col-md-12 > div.erpl_meps-activities-list.mt-3')
        Activities_ = Activities.text
    except NoSuchElementException:
        Activities_ = "No Activities Found"

    try:
        Link_ = driver.current_url
    except NoSuchElementException:
        Link_ = "No Link Found"

    temporary_data = {
        'Image': Image_,
        'Name': Name_,
        'Group': Group_,
        'Status': Status_,
        'Country': Country_,
        'Party': Party_,
        'Email': Email_,
        'Website': Website_,
        'Facebook': Facebook_,
        'Twitter': Twitter_,
        'Youtube': Youtube_,
        'Instagram': Instagram_,
        'LinkedIn': LinkedIn_,
        'Telegram': Telegram_,
        'DateofBirth': DateofBirth_,
        'LocationofBirth': LocationofBirth_,
        'Positions': Positions_,
        'Activities': Activities_,
        'Link': Link_,
    }
    datas.append(temporary_data)

# Save data to CSV file

print(len(datas))
keys = datas[0].keys()
csv_file = 'DataSclearet_EU.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(datas)

print("The file is ready.")
driver.quit()
