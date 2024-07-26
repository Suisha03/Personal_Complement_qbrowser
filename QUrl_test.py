from PyQt6.QtCore import QUrl

# URLを作成します。このURLにはパスワードが含まれています。
"""
url = QUrl()
url.setPassword("password")
url.setScheme("http")
url.setUserName("username")
url.setHost("www.example.com")


print("Original URL: ", url.toString())
# QUrl.UrlFormattingOption.RemovePassword フラグを設定します。
flags = QUrl.UrlFormattingOption.RemovePassword | QUrl.ComponentFormattingOption.DecodeReserved 

# フラグを適用してURLを文字列として出力します。
print("URL without password: ", url.toString(flags))
"""

url = QUrl("https://username:password@www.example.com/path%20with%20spaces")
print("Original URL: ", url.toString())
# QUrl.UrlFormattingOption.RemovePassword フラグを設定します。
flags = QUrl.UrlFormattingOption.RemovePassword | QUrl.ComponentFormattingOption.DecodeReserved 

# フラグを適用してURLを文字列として出力します。
print("URL without password: ", url.toString(flags))
