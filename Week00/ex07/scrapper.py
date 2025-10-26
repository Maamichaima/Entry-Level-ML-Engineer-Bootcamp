# import requests
# from bs4 import BeautifulSoup # (html txt --> arbre html) bibliothèque Python permettant d'extraire des données à partir de fichiers HTML et XML 
# import sys
# import csv

# args = sys.argv

# URL = "https://data.1337ai.org/"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')# r.content --> code html , html5lib ---> Spécification de l'analyseur HTML que nous souhaitons utiliser

# table = soup.find('table', attrs={'id':'dataTable'})

# thead = table.find("thead")
    
# header = ["price", "area", "bedrooms", "bathrooms", "stories", 
# 				"mainroad", "guestroom", "basement", "hotwaterheating", 
# 				"airconditioning", "parking", "prefarea", "furnishingstatus"]
# rows = []
# tr_tags = table.find_all("tr")
# for tr in tr_tags:
#     cells = tr.find_all("td")
#     if cells:  # li fihomch <td> bach nhetohom f list
#         row = [cell.get_text() for cell in cells]
#         rows.append(row)

# with open(args[1], "w") as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(header)
# 	writer.writerows(rows)



from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p>Hello, <b>world</b>!</p>
    <p>Welcome to <a href="https://www.example.com">Example</a> website.</p>
	<p>hhhhh</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Extract text from a specific tag
p_tag = soup.find('p')
print(soup.get_text())  # Output: 'Hello, world!'
print(soup)  # Output: 'Hello, world!'

# Extract text from the entire document
# print(soup.get_text())  # Output: '\n\nHello, world!\nWelcome to Example website.\n\n'

# # Extract text with a separator
# print(soup.get_text(separator=' | '))  # Output: ' | Hello, | world! | Welcome to | Example | website. | '

# # Extract text and strip whitespace
# print(soup.get_text(strip=True))  