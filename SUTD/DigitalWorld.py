"""A better world by Design, one line of code at a time."""

def omigerd(error_type):
    import webbrowser
    help = [ "https://stackexchange.com/search?q=" + str(error_type),
    "https://stackoverflow.com/search?q=" + str(error_type),
    "https://www.google.com.sg/search?q=" + str(error_type),]
    for helpline in help:
        webbrowser.open(helpline, new=1, autoraise=True)

def halp(item):
    import webbrowser
    webbrowser.open("https://docs.python.org/3/search.html?q="+str(item), new=1, autoraise=True)