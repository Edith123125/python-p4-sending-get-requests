import requests
url = "https://learn-co-curriculum.github.io/json-site-example/"
response = requests.get(url)
#print(response.text)
with open("output.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML file saved as output.html")