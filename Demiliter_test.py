from PyQt6.QtCore import QUrl, QUrlQuery

url = QUrl("http://www.example.com/cgi-bin/drawgraph.cgi?type=pie;color=green")
url_query = QUrlQuery()
url_query.setQueryDelimiters(',', ';') 
url_query.addQueryItem("newkey", "newvalue")
print("Formed URL with new delimiter: ", url_query.toString())
