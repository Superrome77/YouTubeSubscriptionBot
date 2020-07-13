import unittest
import time
import random
import selenium
import os
import sys
import pickle
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class SeleniumTest():

	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		options.add_argument('--ignore-certificate-errors')
		options.add_argument("--mute-audio")
		#options.add_extension('')
		self._driver = webdriver.Chrome("hromedriver.exe",chrome_options=options)
		#self._driver = webdriver.Firefox(executable_path="geckodriver.exe")
		self._actions = ActionChains(self._driver)
		self._driver.set_window_size(1250,1500)
		self._flag = False
		self._count = 0
		self._waitLoop = 0

	def CreateYoutubeAccount():
		self._driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=youtube&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Den-GB%26app%3Ddesktop%26action_handle_signin%3Dtrue&hl=en-GB&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true")
		self._actions.send_keys(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=7)))
		self._actions.send_keys(Keys.TAB)
		self._actions.send_keys(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=7)))
		self._actions.send_keys(Keys.TAB)
		self._actions.send_keys(str(self._email))
		self._actions.send_keys(Keys.TAB)
		self._actions.send_keys(Keys.TAB)
		self._actions.send_keys(self._password)
		self._actions.send_keys(Keys.TAB)
		self._actions.send_keys(self._password)
		self._actions.send_keys(Keys.ENTER)

	def login(self,flag):
		try:
			self._driver.get("https://www.youtube.com/results?search_query=sub+for+sub+live")
			time.sleep(3)
			with open("YTcookies.txt", 'rb') as cookiesfile:
				cookies = pickle.load(cookiesfile)
				for cookie in cookies:
					if 'expiry' in cookie:
						del cookie['expiry']
					print("cookie added")
					self._driver.add_cookie(cookie)
			self._driver.get("https://www.youtube.com/results?search_query=sub+for+sub+live")
			time.sleep(3)
			return
		except Exception as e:
			print(e)
			pass

	def streams(self):
		try:
			time.sleep(1)
			#with open("youtubecookies.txt", 'wb') as filehandler:
			#   pickle.dump(self._driver.get_cookies(), filehandler)
			count = 0
			self._streams = []
			self._driver.get("https://www.youtube.com/results?search_query=sub+for+sub+live")
			time.sleep(1)
			stream = self._driver.find_element_by_xpath("//paper-button[@aria-label = 'Search filters']")
			stream.click()
			time.sleep(1)
			live = self._driver.find_element_by_xpath("//yt-formatted-string[text()='Live']")
			live.click()
			time.sleep(1)
			self._streams = self._driver.find_elements_by_xpath("//span[text()='LIVE NOW']")
			time.sleep(2)
			#self._driver.close()
			self._driver.execute_script("window.scrollTo(0,0)")
			
			for i in self._streams[:4]:
				self._driver.execute_script("window.scrollBy(0,100)")
				self._actions.key_down(Keys.CONTROL)
				self._actions.move_to_element_with_offset(i,-40,-15)
				self._actions.click()
				self._actions.key_up(Keys.CONTROL)
				self._actions.perform()
				self._actions.reset_actions()
				self._actions.reset_actions()
				self._actions.reset_actions()
				time.sleep(1)
			if self._flag == True:
				print(self._flag)
				count = 0
				self._streams = []
				self._driver.get("https://www.youtube.com/results?search_query=live")
				time.sleep(.5)
				stream = self._driver.find_element_by_xpath("//paper-button[@aria-label = 'Search filters']")
				stream.click()
				time.sleep(.5)
				live = self._driver.find_element_by_xpath("//yt-formatted-string[text()='Live']")
				live.click()
				time.sleep(.5)
				stream = self._driver.find_element_by_xpath("//paper-button[@aria-label = 'Search filters']")
				stream.click()
				time.sleep(.5)
				vc = self._driver.find_element_by_xpath("//yt-formatted-string[text()='View count']")
				vc.click()
				time.sleep(.5)
				self._streams = self._driver.find_elements_by_xpath("//a[@id='thumbnail']")
				time.sleep(0.5)
				self._driver.execute_script("window.scrollTo(0,0)")
				for i in self._streams[:15]:
					self._actions.key_down(Keys.CONTROL)
					self._actions.move_to_element_with_offset(i,-40,-15)
					self._actions.click()
					self._actions.key_up(Keys.CONTROL)
					self._actions.perform()
					self._actions.reset_actions()
					time.sleep(.2)

			self._driver.close()
		except selenium.common.exceptions.StaleElementReferenceException:
			pass
		try:
			while len(self._driver.window_handles) != 1:
				self._driver.close()
				time.sleep(1)
		except:
			pass
		self._driver.close

	def input(self):
		try:
			for i in range(7):
				for handle in self._driver.window_handles:
					self._driver.switch_to.window(handle)
					time.sleep(3)
					self.wait(self._driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']"))
					title = self._driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")
					newtext = title.text.lower()
					channel = self._driver.find_element_by_xpath("//yt-formatted-string[@id='owner-name']")
					channelText = channel.text.lower()
					#print(channelText)
					#if channelText == "flaretv" or channelText == "social blade" or channelText == "onokopro":
					#	print("bad channel")
						#self._driver.close()
					if "wall" in newtext:
						actions2 = ActionChains(self._driver)
						actions2.reset_actions()
						but = self._driver.find_element_by_tag_name("body")
						actions2.move_to_element_with_offset(but,1000,579)
						actions2.click()
						actions2.send_keys("!wall")
						actions2.send_keys(Keys.ENTER)
						actions2.perform()
						actions2.reset_actions()
						Rnum = random.randint(20,45)
						time.sleep(Rnum)
					if self._flag == True:
						num = random.randint(0,100)
						actions2 = ActionChains(self._driver)
						actions2.reset_actions()
						but = self._driver.find_element_by_tag_name("body")
						actions2.move_to_element_with_offset(but,1000,579)
						actions2.click()
						actions2.send_keys(":fire:Sub swap,subs say %i:fire:" %(num))
						actions2.send_keys(Keys.ENTER)
						actions2.perform()
						actions2.reset_actions()
						Rnum = random.randint(20,25)
						time.sleep(Rnum)
					else:
						num = random.randint(0,100)
						actions2 = ActionChains(self._driver)
						actions2.reset_actions()
						but = self._driver.find_element_by_tag_name("body")
						actions2.move_to_element_with_offset(but,1000,579)
						actions2.click()
						actions2.send_keys("Sub swap,subs say %i" %(num))
						actions2.send_keys(Keys.ENTER)
						actions2.perform()
						actions2.reset_actions()
						Rnum = random.randint(20,30)
						time.sleep(Rnum)
		except selenium.common.exceptions.NoSuchElementException:
			self.exit()
		print("input fin")
		

	def inputSingle(self,stream):
		self._driver.get(stream)
		while True:
			time.sleep(3)
			num = random.randint(0,100)
			time.sleep(3)
			actions2 = ActionChains(self._driver)
			actions2.reset_actions()
			but = self._driver.find_element_by_tag_name("body")
			actions2.move_to_element_with_offset(but,1000,579)
			actions2.click()
			actions2.send_keys(":fire: Sub swap, subs say %i :fire:" %(num))
			actions2.send_keys(Keys.ENTER)
			actions2.perform()
			actions2.reset_actions()
			Rnum = random.randint(60,120)
			time.sleep(Rnum)


	def wait(self,element):
		for i in range(5000):
			try:
				el = element
				return None
			except selenium.common.exceptions.NoSuchElementException:
				self._waitLoop += 1
				print(self._waitLoop)
				print("waitloop")
				pass

	def exit(self):
		try:
			while True:
				self._driver.switch_to.window(self._driver.window_handles[len(self._driver.window_handles)-1])
				if len(self._driver.window_handles) != 1:
					self._driver.close()
				else:
					print("Windows closed")
					break
		except:
			pass
		self._driver.close()



	def cookieenable(self):
		self._driver.get("https://www.youtube.com/results?search_query=sub+for+sub+live")
		time.sleep(80)
		with open("YTcookies.txt", 'wb') as filehandler:
			pickle.dump(self._driver.get_cookies(), filehandler)
		print("done")
if __name__ == "__main__":
	rounds = 0
	t = SeleniumTest()
	time.sleep(60000)
	#t.cookieenable()
	#t.loginMelon(False)
	t.login(False)
	t.streams()
	t.input()
	t.exit()
	#t.inputSingle("https://www.youtube.com/watch?v=UVxU2HzPGug")
	sys.exit()