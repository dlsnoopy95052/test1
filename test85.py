from html.parser import HTMLParser
n = int(input())
c = []
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0],'>', attr[1])
    # def handle_endtag(self, tag):
    #     print("End    :", tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0],'>', attr[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for i in range(n):
    c.append(input())
f = '\n'.join(c)
parser.feed(f)