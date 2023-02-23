import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ') #Variable to store user input
url = 'https://github.com/' + github_user #Using concatation to use variable along with link to find desired username url
r = requests.get(url)
soup = bs(r.content, 'html.parser') #takes the response from r and parses it's content
profile_image = soup.find('img', {'alt' : 'Avatar'})['src'] #soup.find is helping find a specific html tag or attribute and storing ing profile_image
print(profile_image)


