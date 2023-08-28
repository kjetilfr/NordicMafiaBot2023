from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

user_agent = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = webdriver.FirefoxOptions()

options.add_argument("--window-size=1920,1080")

chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
options.add_argument(f'--user-agent={user_agent}')
options.set_preference('intl.accept_languages', 'en-GB')

driver = webdriver.Firefox(options=options)
driver.get("http://www.nordicmafia.org")


def getConfig():
    myConfig = dict()
    fh = open('foobar.config').readlines()
    for line in fh:
        row = line.split(',')
    myConfig['username'] = row[0]
    myConfig['password'] = row[1]
    return myConfig


def sleepRandomLow():
    return random.randint(1, 3)


def getCity():
    whereIsPlayer = driver.find_elements(By.CLASS_NAME, "value")
    # print(whereIsPlayer)
    # for x in whereIsPlayer:
    # print(x.get_attribute("outerHTML"))
    fullWhere = whereIsPlayer[1].get_attribute("outerHTML")
    city = fullWhere[20:]
    city = city[:-7]
    return city


def login():
    myDetails = getConfig()
    # LOGIN START
    username = driver.find_element(By.NAME, "username")
    usrname = myDetails['username']
    psswrd = myDetails['password']
    # randomize username input start
    rndNumber = random.randint(0, len(myDetails['username']))
    usrnamep1 = usrname[:rndNumber]
    usrnamep2 = usrname[rndNumber:]
    username.send_keys(usrnamep1)
    time.sleep(sleepRandomLow() / 10)
    username.send_keys(usrnamep2)
    # randomize username input end
    password = driver.find_element(By.NAME, "password")
    # randomize password input start
    rndNumber = random.randint(0, len(myDetails['password']))
    psswrdp1 = psswrd[:rndNumber]
    psswrdp2 = psswrd[rndNumber:]
    password.send_keys(psswrdp1)
    time.sleep(sleepRandomLow() / 10)
    password.send_keys(psswrdp2)
    # randomize password input end
    time.sleep(0.3)
    password.send_keys(Keys.RETURN)
    # LOGIN END


def krim():
    driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    # checkAntiBot() UPGRADE TO GET THIS FEATURE
    isCounting = checkCountdown()
    if isCounting == False:
        # KRIMINALITET START
        time.sleep(1)
        driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
        # KRIMINALITET END
    else:
        print("Krim timer is going")


def utpress():
    driver.find_element(By.LINK_TEXT, "Utpressing").click()
    # checkAntiBot() UPGRADE TO GET THIS FEATURE
    isCounting = checkCountdown()
    if isCounting == False:
        # UTPRESSING START
        time.sleep(sleepRandomLow())
        driver.find_element(By.ID, "sel_1").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "submitBlackmail").click()
        # UTPRESSING END
    else:
        print("Utpress timer is going")


def fightclub():
    driver.find_element(By.LINK_TEXT, "Fightclub").click()
    # checkAntiBot() UPGRADE TO GET THIS FEATURE
    isCounting = checkCountdown()
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow())
        driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
        # FIGHTCLUB END
    else:
        print("Fightclub timer is going")


def checkCountdown():
    isCountingDown = driver.find_elements(By.ID, "js_countdown")
    if len(isCountingDown) > 0:
        return True
    else:
        return False


def sendCar():
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, "table.def_table.cursor>tbody>tr")
        carElems = []
        for i in elems:
            if not i.get_attribute("name") == "hlrow_table_select_gtaaction":
                carElems.append(i)

        for c in carElems:
            if c.get_attribute("style") == "background-color: #ff4c4c;" or c.get_attribute("style") == "background-color: rgb(255, 76, 76);":
                clickElem = c.find_element(By.CSS_SELECTOR, "td")
                clickElem.click()
                driver.find_element(By.NAME, "doSell").click()
            else:
                pass
    except:
        print("Cant sell cars")


def biltyveri():
    # BILTYVERI START
    driver.find_element(By.LINK_TEXT, "Biltyveri/Garasje").click()
    # checkAntiBot() UPGRADE TO GET THIS FEATURE
    isCounting = checkCountdown()
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        driver.find_element(By.ID, "rowid_table_select_gtaaction0").click()
        biltyveriSuccess = driver.find_elements(By.CLASS_NAME, "successBox")
        if len(biltyveriSuccess) > 0:
            time.sleep(sleepRandomLow())
            sendCar()
    else:
        time.sleep(sleepRandomLow())
        print("Car timer is going")


def fengsel():
    driver.find_element(By.LINK_TEXT, "Fengsel").click()
    # checkAntiBot() UPGRADE TO GET THIS FEATURE
    isCounting = checkCountdown()
    if isCounting == False:
        # FENGSEL START
        time.sleep(sleepRandomLow() / 2)
        if len(driver.find_elements(By.LINK_TEXT, "Bryt ut")) > 0:
            driver.find_element(By.LINK_TEXT, "Bryt ut").click()
        else:
            time.sleep(random.randint(30, 69))
        # FENGSEL END
        time.sleep(3)
        fengsel()
    else:
        print("Fengsel timer is going")


def timeDown():
    x = 0
    while x < 10:
        time.sleep(random.randint(15, 25))
        print("Sleep 20" + " " + str(x))
        x += 1


def doBotStuff():
    print("Start doBotStuff")
    timeDown()
    krim()
    fightclub()
    utpress()
    biltyveri()
    fengsel()
    doBotStuff()


login()
time.sleep(1)
krim()
time.sleep(1)
fightclub()
time.sleep(1)
utpress()
time.sleep(1)
biltyveri()
time.sleep(1)
fengsel()
time.sleep(1)
doBotStuff()
