from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs




browser = webdriver.Firefox()
browser.get("https://weeklyad.publix.com/Publix/BrowseByListing/ByCategory/?StoreID=2700316&CategoryID=5232540")
linkElem = browser.find_element_by_xpath("//button[@class='btn btn-large action-loadall']")
linkElem.click()
linkElem.send_keys(Keys.END)
time.sleep(2.0)
linkElem.send_keys(Keys.END)
time.sleep(1.5)
html = browser.page_source
browser.close()


soup = bs.BeautifulSoup(html, features='html5lib')
#print(soup.prettify())
names = soup.findAll('span', {'class': 'title cursorPointer action-tracking-nav action-goto-listingdetail desktopBBDTabletTitle'})
prices = soup.findAll('p', {'class': "priceQualifier"})
bogo_dict = {}

for x in range(0, len(names)):
    bogo_dict[x] = names[x].text
    print(bogo_dict[x] + " : " + str(x))

print('\n Choose from list the deals you care about: ')
choices = str(input())
choices = choices.split(',')
for choice in choices:
    print(bogo_dict[int(choice)])


