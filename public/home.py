#!/usr/local/bin/python
#print("Content-type: text/html\r\n\r\n")
#print("1xxx")
try:
    from pytonik import App
except Exception as err:
    exit(err)


App = App.App()

App.runs()

