# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:16:05 2021

@author: abhyu
"""
def getres(roll):
    from selenium import webdriver 
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.options import Options
    print(roll) 
    roll=int(roll)
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.headless = True
#roll=input("ROll no.")
#try:
    driverr = webdriver.Chrome(executable_path ="C:\\chromedriver.exe", options=options)
    driverr.get("https://govexams.com/knit/searchresult.aspx") 
    
    
    
    user=driverr.find_element_by_xpath("//*[@id='txtrollno']").clear()
    user=driverr.find_element_by_xpath("//*[@id='txtrollno']").send_keys(roll)
    driverr.find_element_by_xpath("//*[@id='btnSearch']").click()
    			
    			
    select = Select(driverr.find_element_by_id("ddlResult"))
    
    text=[]
    el = driverr.find_element_by_id('ddlResult')
    for option in el.find_elements_by_tag_name('option'):
        text.append(option.get_attribute("value"))
    
    try:  
        select.select_by_value(text[1])
        driverr.find_element_by_xpath("//*[@id='btnGo']").click()
        			
        driverr.forward()
        				
        
        	
        name = driverr.find_element_by_xpath("//*[@id='lblname']").text
        fname= driverr.find_element_by_xpath("//*[@id='lblfname']").text
        course = driverr.find_element_by_xpath('//*[@id="lbltotlmarksDisp"]' ).text
        #finaldict.append((course,name))
        res=(float(course),roll,name)
        print(res)
        return res  
    except:
        print("Not Found")
        return 0
    #finaldict.sort(reverse=True)   
    

#(name,fname,ygpa) = getres(19205)
#print(name,fname,ygpa)