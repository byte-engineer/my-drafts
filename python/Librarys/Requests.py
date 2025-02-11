# The requests module allows you to send HTTP requests using Python.
import requests

# requests.request(method, url, args)        | this method works for all types.


#_Req type__|__Method________________________|
#  GET      |  .get(url, prsms, args)        |
#  POST     |  .post(url, data, json, args)  |
#  PUT      |  .put(url, data, args)         |
#  HEAD     |  .head(url, args)              |
#  PATCH    |  .patch(url, data, args)       |
#  DELETE   |  .deleta(url, args)            |
# -------------------------------------------|


# get the data from a page formatted as a text.
res = requests.get("https://raw.githubusercontent.com/byte-engineer/tiny-projects/refs/heads/main/sort.py")

# get the data as a string. 
res.text

# get the data as a bytes.
res.content

