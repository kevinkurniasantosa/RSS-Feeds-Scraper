#############################
############################# LIBRARY FOR SCRAPING NEWS MANUALLY WITHOUT RSS feed
#############################

# For scraping
import requests
from bs4 import BeautifulSoup
import urllib
# For data manipulation
import pandas as pd 
import numpy as np 
# For using excel
import openpyxl
# others
import time

print('import success\n')

####################################################
#################################################### DEFINE GLOBAL VARIABLES

list_url = [

]

def get_article():
    res = requests.get(list_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')


### INTERNATIONAL NEWS

# def scraping_bbc():
#     # print('hello world')

# def scraping_bbc_health():
#     # print('Hello World!')
#     # article
    

# ### LOCAL NEWS

# def scraping_liputan6():
#     # print('hello world')
#     # article
#     # read-page--content



