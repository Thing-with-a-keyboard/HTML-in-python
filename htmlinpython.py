def initDoc(documentName):
    with open(f"documentName.html", 'x') as document:
        document.write("<!DOCTYPE html>\n")
        document.write("<html>\n")
        document.write(f"<title>{documentName}</title>\n")
        document.write(f"<body>\n")
        document.close()
    """Creates and initialises the HTML document. ONLY USE ONCE PER DOCUMENT"""


def endDoc(documentName):
    with open(f"documentName.html", 'a') as document:
        document.write("</body>\n")
        document.write("</html>\n")
        document.close()
    """Adds the closing tags to an HTML Document. ONLY USE AT THE END OF A DOCUMENT"""