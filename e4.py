import webbrowser

x=input("Enter search prompt: ").replace(" ","+")

webbrowser.open("https://www.google.com/search?q="+x)