This small automation script is very handy for letting you fetch dynamic websites without using Selenium. This script uses the Request-HTML module which is a successor of the request library but with a rendering feature.

This handy script is useful for web scrapers who need to fetch dynamic websites with a request module.

# Fetch Dynamic Websites
# pip install requests-html
from requests_html import HTMLSession
def Get_Webpage(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=2)
    return response.html.html
Get_Webpage("https://www.medium.com")
