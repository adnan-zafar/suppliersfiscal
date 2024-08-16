from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time, random, datetime


def clear_cache():
    try:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            '''
        })
    except:pass

def delay():
    time.sleep(random.randint(5, 8))

def get_month_name(date):
  return date.strftime("%B"), date.strftime("%d")

def select_goods():
    driver.find_element(By.XPATH, '//img[@title="Look up Acquisition Type"]/..').click()
    time.sleep(random.randint(2, 4))
    center_iframe = driver.find_element(By.XPATH, '//iframe[@id="ptModFrame_0"]')
    time.sleep(1)
    driver.switch_to.frame(center_iframe)
    time.sleep(random.randint(2, 3))
    driver.find_element(By.XPATH, '//a[contains(text(), "NON-IT Services")]').click()
    driver.switch_to.default_content()
    time.sleep(random.randint(2, 3))

def select_date():
    # Get today's date
    today = datetime.date.today()
    #today = datetime.date(2024, 8, 3)
    today_month, today_date = get_month_name(today)
    #print("Today is", today_month, today_date)

    one_week_ago = today - datetime.timedelta(weeks=1)
    one_week_ago_month, one_week_ago_date = get_month_name(one_week_ago)
    #print("One week ago it was", one_week_ago_month, one_week_ago_date)

    driver.find_element(By.XPATH, '//img[@title="Calendar From Date"]/..').click()
    time.sleep(random.randint(2, 4))
    if one_week_ago_month != today_month:
        driver.find_element(By.XPATH, '//a[@id="prevmonth"]').click()
        time.sleep(random.randint(1, 2))

    if one_week_ago_date[0] == '0':
        one_week_ago_date = one_week_ago_date.replace('0','')
    driver.find_element(By.XPATH, f'//a[contains(text(),"{one_week_ago_date}")]/..').click()
    time.sleep(random.randint(2, 4))

    driver.find_element(By.XPATH, '//img[@title="Calendar To Date"]/..').click()
    time.sleep(random.randint(2, 4))
    if today_date[0] == '0':
        today_date = today_date.replace('0','')
    driver.find_element(By.XPATH, f'//a[contains(text(),"{today_date}")]/..').click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, '//input[@value="Search"]').click()

def download_file():
    try:
        driver.find_element(By.XPATH, '//select[@id="ZZ_SCPRS_SP_WRK_SORTBY"]').click()
    except:
        delay()
        driver.find_element(By.XPATH, '//select[@id="ZZ_SCPRS_SP_WRK_SORTBY"]').click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, '//option[contains(text(), "Department Name")]').click()
    delay()

    driver.find_element(By.XPATH, '//select[@id="ZZ_SCPRS_SP_WRK_SORTBY_TYPE"]').click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, '//option[contains(text(), "Ascending")]').click()
    delay()

    driver.find_element(By.XPATH, '//input[@id="ZZ_SCPRS_SP_WRK_BUTTON_BACKWARD"]').click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, '//input[@value="OK"]').click()
    delay()
    time.sleep(random.randint(2, 4))

if __name__ == '__main__':
    driver = Driver(uc=True)
    driver.maximize_window()
    clear_cache()
    driver.get('https://suppliers.fiscal.ca.gov/psc/psfpd1/SUPPLIER/ERP/c/ZZ_PO.ZZ_SCPRS1_CMP.GBL?FolderPath=PORTAL_ROOT_OBJECT.ZZ_FISCAL_SCPRS.ZZ_SCPRS1_CMP_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')
    delay()
    select_goods()
    select_date()
    delay()
    download_file()
    driver.quit()