import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import random
name = 'j'
alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

alphabets2 = ['a', '1', 'b', '2', 'c', '0','d', '6', 'e', '7', 'f', '3', '4', '5', '8', '9']

numbers = ["46","47","48","50","51","52","54","56","58","59",
"61","62","67","68","34","42","43","49","53","57",
"00","01","02","03","04","06","07","08","91","80",
"93","11","14","15","16","17","24","23","26","88",
"86","89","92","95","97","96","98","69","64","63",
"66","72","73","79","83","84","87","27","40","74",
"75","78","32","36","33","31","45","39","29","81",
"71","33","30","05","85","77","35","19","38","28",
"76","82","13","09","99","12","18","20","94","21",
"22","25","37","41","44","55","65 ","10","60","70","90"]

suffix = ""
flag=0
for alpha2 in alphabets:
	for alpha3 in alphabets:
		for alpha4 in alphabets:
			for alpha5 in alphabets:
				count_2 = 0
				random_number_1 = random.randint(3,5)
				for alpha6 in alphabets2:
					if count_2==random_number_1:
						continue
					count_1 = 0
					random_number_2 = random.randint(1,2)	
					for number7 in numbers:
						if count_1==random_number_2:
							continue
						suffix = name+alpha2+alpha3+alpha4+alpha5+alpha6+number7
						compare = name + "0000046"
						if(suffix==compare):
							flag=1
						if flag==1:
							url="https://m.llspace.com/v/"+suffix
							r=requests.get(url, timeout=8)
							demo=r.text
							h = etree.HTML(demo)
							
							name_coming = name + "coming.txt"
							f_coming=open(name_coming,'a',encoding='utf-8')
							f_coming.write(suffix+'\n')
							f_coming.close()
							
							post_name = h.xpath('//span[contains(@class,"l-user-name")]//text()')
							if post_name:
								count_1 = count_1+1
								count_2 = count_2+1
								post_title = h.xpath('//h1[contains(@class,"l-title")]//text()')
								post_text = h.xpath('//div[contains(@class,"l-text")]//text()')
								post_date = h.xpath('//span[contains(@class,"l-date")]//text()')
								
								name_success = name + "success.txt"
								f_success=open(name_success,'a',encoding='utf-8')
								f_success.write(suffix+'\n')
								f_success.close()
								
								name_file = name + ".txt"
								f=open(name_file,'a',encoding='utf-8')
								f.write(suffix+'\n')
								f.write(json.dumps(post_title,ensure_ascii=False) + '\n') #必须格式化数据
								f.write(json.dumps(post_text,ensure_ascii=False) + '\n')
								f.write(json.dumps(post_name,ensure_ascii=False) + '\n')
								f.write(json.dumps(post_date,ensure_ascii=False) + '\n')
								f.write('\n')
								f.write('\n')
								f.close()
								
		

#print(post_title)
#print(post_text)
#print(post_name)
#print(post_date)
#print("\n")
