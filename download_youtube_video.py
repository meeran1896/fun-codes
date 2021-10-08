import webbrowser
url = input("Enter youtube url to download")
download = url[:12] + "ss" + url[12:]
webbrowser.open(download)
