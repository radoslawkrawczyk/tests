from logging import exception
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from aaa.names import names


def actions():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("file:///C:/Users/Użytkownik/Desktop/Selenium%20kurs/Test.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_id("newPage").click()
    print("\nStrona - " + driver.title)   # pobieram tytuł strony, ktory jest wewnatrz tagu head tej strony

    current_window_name = driver.current_window_handle
    window_names = driver.window_handles

    for window in window_names:
        if window != current_window_name:
            driver.switch_to.window(window)

    print("Strona - " + driver.title)  # sprawdzamy czy nas przeniosło

    driver.switch_to.window(current_window_name)  # powrot do strony testowej
    print("Strona - " + driver.title)  # i wyswietlenie jej nazwy
    # driver.switch_to_window("").send_keys()
    driver.quit()


try:
    actions()
    result1 = "Passed"

except exception as e:
    result1 = "Failed - " + str(e)

action = names[0] + " - " + result1
print(action)
