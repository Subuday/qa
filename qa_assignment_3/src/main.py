from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

fb_url = "https://www.fb.com/"
facebook_url = "https://www.facebook.com/"

profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'en-US, en')
driver = webdriver.Firefox(firefox_profile = profile)

driver.get(fb_url)

assert "Facebook" in driver.title
assert facebook_url == driver.current_url

print('Redirection is successfull.')

main_page = driver.current_window_handle

driver.find_element_by_xpath("//a[@data-testid='open-registration-form-button']").click()
driver.implicitly_wait(10)

driver.find_element_by_name("firstname").send_keys("Danylo")
driver.find_element_by_name("lastname").send_keys("Shapovalov")
driver.find_element_by_name('reg_email__').send_keys('dd26@test.com')
driver.find_element_by_name('reg_email_confirmation__').send_keys('dd26@test.com')
driver.find_element_by_id('password_step_input').send_keys('secretPass')

sleep(2)
Select(driver.find_element_by_xpath("//select[@id='day'][@name='birthday_day']")).select_by_visible_text('19')
Select(driver.find_element_by_xpath("//select[@id='month'][@name='birthday_month']")).select_by_visible_text('Aug')
Select(driver.find_element_by_xpath("//select[@id='year'][@name='birthday_year']")).select_by_visible_text('2001')

driver.find_element_by_xpath("//label[text()='Female']").click()
sleep(2)
driver.find_element_by_xpath("//button[text()='Sign Up']").click()

sleep(10)
assert 'facebook.com/checkpoint/' in driver.current_url

succ = driver.find_element_by_xpath("//div[text()='Complete these steps in the next 30 days to make sure that you can use this account.']")
assert succ.text == 'Complete these steps in the next 30 days to make sure that you can use this account.'

driver.close()
