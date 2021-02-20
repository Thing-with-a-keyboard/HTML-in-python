def initDoc(docName):
    with open(f"{docName}.html", 'x') as doc:
        doc.write("<!DOCTYPE html>\n")
        doc.write("<html>\n")
        doc.write(f"<title>{docName}</title>\n")
        doc.write(f"<body>\n")
        doc.close()
    """Creates and initialises the HTML document. ONLY USE ONCE PER DOCUMENT"""


def endDoc(docName):
    with open(f"{docName}.html", 'a') as doc:
        doc.write("</body>\n")
        doc.write("</html>\n")
        doc.close()
    """Adds the closing tags to an HTML Document. ONLY USE AT THE END OF A DOCUMENT"""


def heading(docName, headSize, contents):
    with open(f"{docName}.html", 'a') as doc:
        doc.write(f"<h{str(headSize)}>{contents}</h{str(headSize)}>")
        doc.close()
    """Adds a heading to an HTML Document, in a size of your choice."""


def paragraph(docName, contents):
    with open(f"{docName}.html", 'a') as doc:
        doc.write(f"<p>{contents}</p>")
    """Adds a paragraph to an HTML document. </b> must be manually added into contents."""