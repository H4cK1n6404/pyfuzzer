import requests
import re
import urllib3


urllib3.disable_warnings()
s = requests.Session()
url = input("url here: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
def fuzz(url):
	  def checkRobots(url):
	   	r = s.get(url+"robots.txt", verify=False, timeout=5, headers=header)
	   	if r.status_code == requests.codes.ok:
	   		lines = r.text.splitlines()
	   		for keyword in lines:
	   			if re.search('admin|api|controll_panel|users|usarios|administrator|json|login|php|uploads|manager|dev|FCKEditor|old|db|private', keyword):
	   				print(keyword)
	   			else:
	   				pass
	   	else:
	   		print("Robots.txt wasn't found proceeding to bruteforcing files/dirs")
	   		pass
	  def dirhunt(url):
	  	try:
	  		for link in open("payload.txt").read().splitlines():
		  		r = s.get(url+link, verify=False, timeout=5, headers=header)
		  		print("Trying => {}{}".format(url,link))
		  		if r.status_code == requests.codes.ok:
		  			print('Found => {}'.format(url+link))
		  		elif r.status_code == requests.codes.temporary_redirect:
		  			print('Redirecting somewhere => {}'.format(url+link))
		  		elif r.status_code == requests.codes.unauthorized or r.status_code == requests.codes.not_acceptable:
		  			print('Not_Acceptable => {}'.format(url+link))
		  		else:
		  			pass
	  	except:
	  		print("Check Your Internet!..")
	  		pass			
	  checkRobots(url)
	  dirhunt(url)

fuzz(url)