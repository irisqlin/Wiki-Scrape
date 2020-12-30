from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook 
import requests
import re
import os
import csv

base_url = 'https://en.wikipedia.org/wiki/List_of_academic_fields'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
    
topic_list = []
wb = Workbook() 
sheet1 = wb.add_sheet('Academic Topics') 
row = 0
col = 0


for stuff in soup.find_all('a'):
        topic_list.append(stuff.text)
        sheet1.write(row, col, stuff.text)
        row += 1

wb.save('Topics.xls') 


print(len(topic_list))




