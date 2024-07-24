from PyQt6.QtCore import QUrl

# URLを作成します。このURLにはパスワードが含まれています。
url = QUrl()
url.setScheme("http")
url.setUserName("username")
url.setPassword("password")
url.setHost("www.example.com")

print("Original URL: ", url.toString())

# QUrl.UrlFormattingOption.RemovePassword フラグを設定します。
flags = QUrl.UrlFormattingOption.RemovePassword

# フラグを適用してURLを文字列として出力します。
print("URL without password: ", url.toString(flags))
