#------------------------------------------      IMPORTS       ------------------------------------------------------------#

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time
from selenium.webdriver.chrome.options import Options

#------------------------------------------     TASK 2.0      ------------------------------------------------------------#
 

# Method for scrolling down the twitter page
def scrolldown():
    for i in range(30):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)

# Waiting for twitter posts to load
def wait():
    WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l']")
        ))

# Lists for nodes and edges to draw in networkX
nodes = []
edges = []

driver = webdriver.Chrome(executable_path='/Users/kmh0751/Documents/Study 2020-2023/2022_Vår/INFO215/My_Assignments_Webscience/OBLIG_5/chromedriver')

# Finding hashtags on given sites and add them as nodes and edges to the list
# Using a combination og selenium and BeautifulSoup in this method
def find_hashtag(hashtag):
    url = f'https://twitter.com/hashtag/{hashtag}?src=hashtag_click'
    driver.get(url)
    
    # Using the methods for waiting and scrolling down to load more tweets
    wait()
    scrolldown()

    bs = BeautifulSoup(driver.page_source, 'html.parser')
    hashtags = bs.find_all('a', {'href': re.compile('\/hashtag\/.*')})

    for link in hashtags:
        hashtag_text = link.get_text()
        if hashtag_text.startswith('#'):
            url = link.attrs['href']
            nodes.append(hashtag_text)
            edges.append((f'#{hashtag}', hashtag_text))

find_hashtag("ElonMusk")
find_hashtag("Tesla")

print(nodes, edges)

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
nx.draw(G, with_labels=True)
name = "Elon_Musk_Network"
# Create graphml file
nx.write_graphml(G, f"{name}.graphml")
plt.show()

driver.quit()