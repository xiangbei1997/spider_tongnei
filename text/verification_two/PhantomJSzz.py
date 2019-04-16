# 打开游览器
# from selenium import webdriver
# import time
# # 键盘KEY使用
# from selenium.webdriver.common.keys import Keys
#导入ActionChains类
# from selenium.webdrive import ActionChains
# 创建一个PhatomJS对象
# driver = webdriver.PhantomJS(executable_path = r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# driver = webdriver.PhantomJS()
# # driver.set_window_size(100,100)
# driver.get('https://www.baidu.com')
# test = driver.find_element_by_id('su')
# print(test,'what')

#导入ActionChains类
# from selenium.webdriver import ActionChains
# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# text = driver.get("http://www.baidu.com/")
# print(text)
#鼠标移动到ac位置
# ac = driver.find_element_by_id('lg')
# print(ac)
# ActionChains(driver).move_to_element(ac).perform()

# #在ac位置单击
# ac = driver.find_element_by_xpath('elementA')
# ActionChains(driver).move_to_element(ac).click(ac).perform()
#
# #在ac位置双击
# ac = driver.find_element_by_xpath("elementB")
# ActionChains(driver).move_to_element(ac).double_click(ac).perform()
#
# #在ac位置右击
# ac = driver.find_element_by_xpath('elementC')
# ActionChains(driver).move_to_element(ac).context_click(ac).perform()
#
# #在ac位置左键单击hold住
# ac = driver.find_element_by_xpath('elementF')
# ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()
#
# #将ac1拖拽到ac2位置
# ac1 = driver.find_element_by_xpath('elementD')
# ac2 = driver.find_element_by_xpath('elementE')
# ActionChains(driver).drag_and_drop(ac1, ac2).perform()
