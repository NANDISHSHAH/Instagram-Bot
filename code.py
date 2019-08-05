from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
            self.driver.close()

    def login1(self):
            driver = self.driver
            driver.get('https://www.instagram.com/')
            time.sleep(5)
            login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
            time.sleep(2)
            user_name_elem=driver.find_element_by_xpath("//input[@name='username']")
            user_name_elem.clear()
            user_name_elem.send_keys(self.username)
            passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
            passworword_elem.clear()
            passworword_elem.send_keys(self.password)
            passworword_elem.send_keys(Keys.RETURN)
            time.sleep(2)
    def like_photo(self,hashtag):
            driver=self.driver
            
            driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
            time.sleep(2)
            for i in range (1,3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
                time.sleep(2)
            hrefs=driver.find_elements_by_tag_name('a')
            pic_hrefs=[elem.get_attribute('href') for elem in hrefs]
            # print(pic_hrefs)
            # print('\n\n\n\n\n\n\n')    
            pic_hrefs=[href for href in pic_hrefs if 'p/B' in href]
            # print(pic_hrefs)
            # print('\n\n\n\n\n\n\n')   
            print(hashtag + 'photos:' + str(len(pic_hrefs)))
            for posts in pic_hrefs:
                driver.get(posts)
                time.sleep(3)
                # butt = driver.find_elements_by_class_name('dCJp8 afkep _0mzm-')
                # for tags in butt:
                #     if tags.find_element_by_xpath("//span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']"):
                #         print("Liked!")
                #         tags.click()
                #         time.sleep(3)
                try:
                    time.sleep(2)
                    like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]')
                    like_button().click()
                    time.sleep(3)
                except Exception as e:
                        time.sleep(2)

ed = instagram('Username', 'Password')
ed.login1()
ed.like_photo('hashtag')
