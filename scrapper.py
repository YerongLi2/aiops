from tkinter import E
from bs4 import BeautifulSoup
import requests
import urllib
urllib.request
import lxml.html
import time
from selenium import webdriver
import tqdm
import pandas as pd
from selenium.webdriver.common.keys import Keys
import re
ns = {'re': 'http://exslt.org/regular-expressions'}

DEBUG = False
def getAllResolvedPosts(base_url):

    pdfs = []
    res = urllib.request.urlopen(base_url)
    # parse the response into an xml tree
    # print(res.read()[:100])
    res=get_html(base_url)
    # tree = lxml.html.fromstring(res.read())
    # tree = lxml.html.fromstring(res)
    # regex = '[0-9]+$'
    # # regex = '6$'
    # # regex = '^/http'
    # # print(tree.xpath(f'//a[re:test(@href, "{regex}", "i")]',namespaces=ns))
    # count = 0
    # for node in tree.xpath(f'//a[re:test(@href, "{regex}", "i")]',namespaces=ns):
    #     if node.attrib['href'][:38] != 'https://forums.developer.nvidia.com/t/': continue
    #     url = urllib.parse.urljoin(base_url, node.attrib['href'])
    #     # print(url)
    #     count += 1


    return res

def get_html(url):
    # req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    # response = urlopen(req).read()
    driver = webdriver.Firefox()
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        if DEBUG : break
        
    regex = '[0-9]+$'

    ans = [elem.get_attribute("href") for elem in  driver.find_elements_by_xpath("//a[@href]")]
    driver.quit()
    
    ans = [e for e in ans if e[:38] == 'https://forums.developer.nvidia.com/t/']
    return ans
 
def parse_post(url):
    '''
    param url: url to
    Return: Parses a post from the given url
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    divs = soup.find_all('div', class_='post')
    users = soup.find_all('a', href=re.compile("^https://forums.developer.nvidia.com/u/"))
    times = soup.find_all('time', class_='post-time')
    data = []    
    try:
        assert(len(divs) == len(users) == len(times))
        for i in range(len(divs)):
            data.append([divs[i].text, users[i].text.strip(), times[i].text.strip()])
    except:
        print(url)
    return [url] + data
# url = "https://forums.developer.nvidia.com/t/custom-plugin-retaining-information-in-between-power-cycles/128151"
# parse_post(url)

c_urls = [
    'https://forums.developer.nvidia.com/c/autonomous-vehicles/drive-agx/57',
    'https://forums.developer.nvidia.com/c/autonomous-vehicles/drive-px2/61',
    'https://forums.developer.nvidia.com/c/accelerated-computing/cuda/206',
    'https://forums.developer.nvidia.com/c/accelerated-computing/hpc-compilers/299',
    'https://forums.developer.nvidia.com/c/physics-simulation/modulus-physics-ml-model-framework/443',
    'https://forums.developer.nvidia.com/c/healthcare/clara-holoscan-sdk/320',
    'https://forums.developer.nvidia.com/c/agx-autonomous-machines/jetson-embedded-systems/70',
    'https://forums.developer.nvidia.com/c/development-tools/nsight-systems/116',
    ]
c_urls = [c_curl + '?solved=yes' for c_curl in c_urls]
# header = ['url', 'posts']

for c_url in c_urls:
    urls = getAllResolvedPosts(c_url)
    name = c_url.split('/')[-2]
    data = []
    for url in tqdm.tqdm(urls):
        # print(url)
        # if url[:38] != 'https://forums.developer.nvidia.com/t/': continue
        data.append(parse_post(url))
    # print(data[0])
    pd.DataFrame(
        {
            'url': [e[0] for e in data],
            'posts': [e[1] for e in data]
        }
    ).to_csv(f'{name}.csv',index=False)
    print(f'{name}.csv saved')  
