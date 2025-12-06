import time
from selenium.webdriver.common.by import By

def test_submit_review_ui(driver):
    driver.get('http://localhost:8000/product/1')

    # add review text
    input_el = driver.find_element(By.NAME, 'review')
    input_el.clear()
    input_el.send_keys('Automated Selenium review')

    # Select a rating
    star_label = driver.find_element(By.CSS_SELECTOR, 'label[for="star5"]')
    star_label.click()

    # Submit
    btn = driver.find_element(By.TAG_NAME, 'button')
    btn.click()

    time.sleep(0.8)

    body = driver.page_source
    assert 'Automated Selenium review' in body or 'No reviews yet' not in body
