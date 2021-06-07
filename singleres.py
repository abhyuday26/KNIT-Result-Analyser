
def getSingleRes(roll):

    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    chrome_options = webdriver.ChromeOptions()
    
    CHROMEDRIVER_PATH = 'C:\\chromedriver.exe'
    brower = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
    brower.get("https://govexams.com/knit/searchresult.aspx")
    user=brower.find_element_by_xpath("//*[@id='txtrollno']").clear()
    user=brower.find_element_by_xpath("//*[@id='txtrollno']").send_keys(roll)
    brower.find_element_by_xpath("//*[@id='btnSearch']").click()
    					
    select = Select(brower.find_element_by_id("ddlResult"))
    
    text=[]
    el = brower.find_element_by_id('ddlResult')
    for option in el.find_elements_by_tag_name('option'):
        text.append(option.get_attribute("value"))
    select.select_by_value(text[1])
    brower.find_element_by_xpath("//*[@id='btnGo']").click()
    brower.forward()
    brower.execute_script('window.print();')
