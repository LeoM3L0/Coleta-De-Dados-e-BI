with alive_bar(1000) as bar:
    for i in range(1000):
        time.sleep(0.5)
        bar()
        if i == 990:
            driver.find_element(by=By.XPATH, value='//*[@id="excel"]/span').click()