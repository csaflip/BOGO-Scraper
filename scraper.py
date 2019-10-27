from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import PySimpleGUI as sg


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

bogo_str = ''
for x in range(0, len(names)):
    bogo_dict[x] = names[x].text
    bogo_str += bogo_dict[x] + " : " + str(x) + "\n"


layout = [[sg.Output(size=(50, 40), key='-OUTPUT-')], [sg.Input(key='-IN-')],
          [sg.Button('Next')], [sg.Exit()]]

window = sg.Window('Window that stays open', layout).Finalize()
window.Maximize()
choices = ''
while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Next'):
        window['-OUTPUT-'].Update(bogo_str)

    if event in (None, 'Exit'):
        choices = values['-IN-']
        break

        window.Close()

deals_chosen = ''
choices = choices.split(',')
for choice in choices:
    deals_chosen += bogo_dict[int(choice)] + "\n"
sg.Popup('You entered', deals_chosen)




