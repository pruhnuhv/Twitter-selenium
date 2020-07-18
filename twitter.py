#Import Dependencies
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date



#Automate Login To Twitter
def Twitter_login(username_input,password_input):
    driver.get("https://twitter.com/login")
    time.sleep(3)
    username=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input""")
    password=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input""")
    username.clear()
    password.clear()
    username.send_keys(username_input)
    password.send_keys(password_input)
    #login=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div""")
    password.send_keys(Keys.ENTER)
    



#Tweet Whatever Text Is passed to the function
def Twitter_tweet(Text):
    time.sleep(4)
    Tweet_content=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div""")
    Tweet_content.click()
    Tweet_content.send_keys(Text)
    Tweet=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span""")
    Tweet.click()




#Check For Notifications
def Notif_check():
    notifications=driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]/div/div/div""")
    notif_no=notifications.get_attribute("innerHTML")
    Twitter_Tweet("You currently have "+ str(notif_no) +" unread notifications.")






#MAIN BODY

today=date.today()
driver = webdriver.Chrome(ChromeDriverManager().install())
Twitter_login(username,password)
print("Logged into Twitter for"+ username)
date = today.strftime("%B %d, %Y")
Tweet="Hello, it is "+str(date)+" today, and"+ username +"you are fucking beautiful!"
Twitter_tweet(Tweet)
time.sleep(2)
Notif_check()
