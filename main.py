import requests

#url = "https://finance.yahoo.com/"   #stored like astring type

api_key = "3ddff75174784cdab30265dc743ceb28"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-12-29&sortBy=publishedAt&apiKey=" \
      "3ddff75174784cdab30265dc743ceb28"

#Make req
req = requests.get(url)

#Get a dictionary with data
content = req.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])