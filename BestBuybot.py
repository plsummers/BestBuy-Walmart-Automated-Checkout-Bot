from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import urllib.request
import os
from configparser import ConfigParser
import tkinter as tk

class BBYbot():
	def __init__(self,config):

		self.driver = webdriver.Chrome('./chromedriver.exe')
		self.url="https://www.bestbuy.com/"
		self.username=config.get('BBY_ACCOUNT','USERNAME')
		self.password=config.get('BBY_ACCOUNT','PASSWORD')
		self.ID=config.get('BBY_ACCOUNT','ID')
		self.card=config.get('CARD_INFO','CARD#')
		self.cardsecurity=config.get('CARD_INFO','CARDSECURITY')
		self.expm=config.get('CARD_INFO','EXPM')
		self.expy=config.get('CARD_INFO','EXPY')
	

		self.driver.get(self.url)

	def Login(self):
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/button/div[2]/span').click()
		time.sleep(.5)
		self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/div/div/div/div/div[2]/div/div/a/button').click()
		time.sleep(2)
		username_input=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')
		username_input.send_keys(self.username)
		password_input = self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[2]/div/input')
		password_input.send_keys(self.password)
		password_input.submit()
		time.sleep(3)

		try:
			employee=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')
			employee.send_keys(self.ID)
			employee.submit()
		except:
			return

	def searchtag(self, search_tag):
		searchbar=self.driver.find_element_by_class_name('search-input')
		searchbar.send_keys(search_tag)
		searchbar.submit()

	def in_stock(self):
		time.sleep(5)
		try:
			
			item = self.driver.find_elements_by_class_name('btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')
			#webdriver.ActionChains(self.driver).click_and_hold(self.driver.find_elements_by_class_name('btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')).perform()
			#webdriver.ActionChains(self.driver).release().preform()
			print("In stock!")
			return True
			

		except:
			print("Item is out of stock")
			return False

	def add_toCart(self, incart):
		try:
			time.sleep(3)
			item =self.driver.find_element_by_class_name('btn-lg')
			item.click()
			time.sleep(2)							
			go_to_cart_button= self.driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a')
			
			go_to_cart_button.click()
			incart=True
			return incart
			
		except:
			print("Couldnt add to cart trying again")
			incart=False
	def checkout(self):
		time.sleep(3)
		#selects shipping
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input').click()
		#presses checkout
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
		#continues to payment
		time.sleep(2)
		self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
		time.sleep(4)
		paymentinfo=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input')
		paymentinfo.send_keys(self.card)
		selectmm = Select(self.driver.find_element_by_name('expiration-month'))
		selectmm.select_by_visible_text(self.expm)
		selectyy = Select(self.driver.find_element_by_name('expiration-year'))
		selectyy.select_by_visible_text(self.expy)
		securitycode=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input')
		securitycode.send_keys(self.cardsecurity)
		self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button').click()

	def closeEmailprompt(self):
		self.driver.find_element_by_class_name("c-modal-close-icon").click()
	def close(self):
		self.driver.close()
def getinput():
	sku_num=skunumber.get()
	print(sku_num)
	return sku_num

print("Starting Bot")
root=tk.Tk()
searchtag=''
root.title("BBYbot")
root.geometry("400x500")

text=tk.Label(root, text="Welcome to the BestBuy Bot made for \ngetting RTX 30 Series GPUs",font=("Helvetica", 16) )
infotext=tk.Label(root, text="Edit Config file and add personal info",font=("Helvetica", 16))
text.pack()
infotext.pack()
sku=tk.Label(root, text="Enter the SKU of the GPU you want", font=("Helvetica", 16))
sku.pack()
skunumber=tk.Entry(root)
skunumber.pack()
sku= tk.Button(root,text="Enter",command=getinput())
print(sku)
sku.pack()
#text.pack()
#text.insert(tk.END, "Welcome to the BestBuy Bot")
root.mainloop()

'''
config_file= ConfigParser()
config_file.read("config.ini")
bot = BBYbot(config_file)
time.sleep(1)
try:
	bot.Login()
except:
	bot.closeEmailprompt()
	bot.Login()
time.sleep(4)
bot.searchtag("8720312")
instock= bot.in_stock()
incart=False
if (instock==True):
	while(incart != True):
	 	incart=bot.add_toCart(incart)
print("In cart!")
time.sleep(1)
#bot.checkout()

root=Tk()

root.title("BBYbot")
root.geomentry("400x500")

print("compiled")
bot.close()
'''