import requests
from send_email import send_email

topic = "tesla"

#url = "https://finance.yahoo.com/"   #stored like astring type

api_key = "3ddff75174784cdab30265dc743ceb28"
url = "https://newsapi.org/v2/everything?"  \
      f"q={topic}&" \
      "from=2022-12-29&sortBy=publishedAt&" \
      "apiKey=3ddff75174784cdab30265dc743ceb28&" \
      "language=en"

#Make req
req = requests.get(url)

#Get a dictionary with data
content = req.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)