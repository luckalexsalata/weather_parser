from celery import shared_task
from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
from bs4 import BeautifulSoup
from .update_fuck import update_db_data
# from .models import Weather


@shared_task
def parser_task():
    # print('start task')
    # print('start Chrome driver')
    #DOCKER driver
    driver = Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    #local
    # driver = Chrome(executable_path='/home/alex/dev/weather_parser/api/chromedriver')
    url = 'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/week/'
    driver.get(url)

    html = driver.page_source
    bs = BeautifulSoup(html, "lxml")
    # print('start get weather data')
    temp = bs.find_all('div', class_="weather-wrapper__temp seven-days__temp fl-c")
    carrent_date = datetime.date.today()
    # carrent_date -= datetime.timedelta(days=2)  # для проверки
    i = 0  # for last element
    for x in temp:
        if i == 6:
            break
        date = carrent_date.strftime("%d.%m.%y")
        temperature = x.get_text(strip=True)
        description = x.find('span', class_="seven-days__temp-icon").get('data-tippy-content')
        # print(description)
        # print('start find db data')
        update_db_data(date, temperature, description)
        carrent_date += datetime.timedelta(days=1)
        i += 1
    driver.quit()
