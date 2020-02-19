import time
from logging import exception

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from names import names


def elements():
    driver = webdriver.Chrome(ChromeDriverManager().install())  # instalujemy webdriver
    driver.get("./Test.html")  # metoda 'get' słuzy do szukania strony
    driver.maximize_window()
    driver.implicitly_wait(10)   # czeka na znalezienie elementow tyle sekund

    driver.find_element_by_id("clickOnMe").click()             # click
    driver.switch_to.alert.accept()                            # akceptujemy alert
    driver.find_element_by_id("clickOnMe").click()
    driver.switch_to.alert.dismiss()                           # alert został pominięty
    driver.find_element_by_id("fname").send_keys("Marcin")     # wpisywanie tekstu
    # driver.find_element_by_name("password").send_keys(Keys.ENTER)
    auto_select = Select(driver.find_element_by_tag_name("select"))     # szukamy selecta
    auto_select.select_by_visible_text("Volvo")                # podajemy select
    auto_select.select_by_value("saab")                        # lub inna metoda, gdzie podajemy value
    auto_select.select_by_index(0)                             # lub tutaj szukamy po indexie
    driver.find_element_by_xpath("//input[@type='checkbox']").click()   # zaznaczamy checkbox
    driver.find_element_by_xpath("//input[@value='male']").click()      # zaznaczamy radiobutton
    print(driver.find_element_by_tag_name("h1").text)       # pobieramy tekst z tagu H1 - Witaj na stronie testowej
    print(driver.find_element_by_id("clickOnMe").text)      # pobieramy tekst z id - Kliknij mnie!
    print(driver.find_element_by_tag_name("p").text)        # pobranie ukrytego elementu - NIE powiodło się

    print(driver.find_element_by_tag_name("p").get_attribute("textContent"))  # prawidlowe pobranie ukrytego elementu
    print("Tekst to " + driver.find_element_by_id("fname").get_attribute("value"))  # przez 'get_attribute'

    print(driver.find_element_by_id("smileImage").size.get("height"))
    print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))
    """
    sprawdzenie czy obrazek sie wyswietla
    jesli element nie był wyswietlony na stronie to dostaniemy 0, jesli bedzie to to taka sama wartosc jak w height
    """
    time.sleep(2)  # to jest zatrzymanie akcji
    driver.quit()


try:
    elements()
    result2 = "Passed"

except Exception as e:
    result2 = "Failed - " + str(e)

element = names[1] + " - " + result2
print(element)
