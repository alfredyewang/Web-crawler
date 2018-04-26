from selenium import webdriver
import os
import json
import sys
import time
import urllib.request
import socket
# socket.setdefaulttimeout(5)
os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "./images/"

def download(keyword,number):
	searchtext = keyword
	# num_requested = number
	number_of_scrolls = number / 400 + 1

	if not os.path.exists(download_path + searchtext.replace(" ", "_")):
		os.makedirs(download_path + searchtext.replace(" ", "_"))

	url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
	driver = webdriver.Firefox()
	driver.get(url)

	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	extensions = {"jpg", "jpeg", "png", "gif"}
	img_count = 0
	downloaded_img_count = 0
	
	for _ in range(int(number_of_scrolls)):
		for __ in range(10):
			driver.execute_script("window.scrollBy(0, 1000000)")
			time.sleep(0.2)
		time.sleep(0.5)
		try:
			driver.find_element_by_xpath("//input[@value='Show more results']").click()
		except Exception as e:
			print ("Less images found:", e)
			break

	imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
	print ("Total images:", len(imges), "\n")
	for img in imges:
		img_count += 1
		img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
		img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
		print ("Downloading image", img_count, ": ", img_url)
		try:
			if img_type not in extensions:
				img_type = "jpg"
			urllib.request.urlretrieve(img_url,download_path+searchtext.replace(" ", "_")+"/"+str("%05d"%downloaded_img_count)+"."+img_type)

			downloaded_img_count += 1
		except Exception as e:
			print ("Download failed:", e)
		finally:
			print
		if downloaded_img_count >= number:
			break

	print ("Downloaded: ", downloaded_img_count, "/", img_count)
	driver.quit()

if __name__ == "__main__":
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

	parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
	parser.add_argument("--keyword", type=str, nargs=1,
						help='')
	parser.add_argument("--number", type=int, nargs=1,
						help='')
	args = parser.parse_args()
	print(args.keyword[0])
	print(args.number[0])


	download(args.keyword[0],args.number[0])