from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

wait = WebDriverWait(driver, 10)

def test_first_name():
    first_name_label = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'First Name')]"))
    )

    input_first_name = first_name_label.find_element(By.XPATH, "following-sibling::input")

    input_first_name.clear()
    input_first_name.send_keys("Ram")
    assert input_first_name.get_attribute("value") == "Ram"
    print("First Name test passed.")

def test_gender_selection():
    gender_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Male')]/preceding-sibling::input"))
    )

    gender_option.click()
    assert gender_option.is_selected()
    print("Gender selection test passed.")

def test_profession_checkbox():
    profession_checkbox = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Automation Tester')]/preceding-sibling::input"))
    )
    profession_checkbox.click()
    assert profession_checkbox.is_selected()
    print("Profession checkbox test passed.")

try:
    test_first_name()
    test_gender_selection()
    test_profession_checkbox()
finally:
    driver.quit()