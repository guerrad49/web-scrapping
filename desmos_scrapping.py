from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.desmos.com/math'
r_html = requests.get(url).text

soup = BeautifulSoup(r_html, 'lxml')

csv_file = open('desmos_scrapping.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Author', 'Video Link'])

math_examples = soup.find_all('div', class_ = 'section-interior')

for example in math_examples[1].find_all('a', class_ = 'big-graph-tile'):
    title = example.find('div', class_ = 'truncated-title').text

    author = example.find('div', class_ = 'author').text

    link = str(example).split('"')
    link = url[:-5] + link[3]

    csv_writer.writerow([title, author, link])

csv_file.close()
