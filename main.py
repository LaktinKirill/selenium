from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def read_artikc():
    paragrahps = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragrahps:
        print(paragraph.text)
        input()
def linked_artikc():
    linked_artikcs = []
    for item in browser.find_elements(By.TAG_NAME, "div"):
        cl = item.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            linked_artikcs.append(item.text)


    print()
    for i in linked_artikcs:
        print(i)
    user_choise = input("Вот список связанных статей, Какую открываем? ")
    a1 = browser.find_element(By.LINK_TEXT, user_choise)
    a1.click()
    user_action = input(
        "Статья выбрана\n 1. Пролистать параграфы статьи\n 2. Перейти на одну из связанных страниц\n")
    if user_action == "1":
        read_artikc()
    elif user_action == "2":
        linked_artikc()

user_request = input("Введите запрос для википедии: ")
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
search_box = browser.find_element(By.CLASS_NAME, "vector-search-box-input")
search_box.send_keys(user_request)
search_box.send_keys(Keys.RETURN)

articks_title = []
for element in browser.find_elements(By.TAG_NAME, "a"):
    object = element.get_attribute("data-serp-pos")
    my_list = ('0','1','2','3','4','5','6','7','8','9')
    if object in my_list:
        articks_title.append(element.text)

for artick in articks_title:
    print(artick)
print()
user_artick = input("Вот первые  10 статей на выбранную тему, Какую открыть? ")
a = browser.find_element(By.LINK_TEXT, user_artick)
a.click()
while True:
    user_action = input("Статья выбрана\n 1. Пролистать параграфы статьи\n 2. Перейти на одну из связанных страниц\n 3. Выйти из программы\n")
    if user_action == "1":
        read_artikc()
    elif user_action == "2":
        linked_artikc()
    else:
        break












