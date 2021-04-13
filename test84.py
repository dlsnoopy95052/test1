from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.count('\n') >=1:
            print(">>> Multi-line Comment\n"+data)
        else:
            print(">>> Single-line Comment\n"+data)

    def handle_data(self, data):
        if data == '\n': 
            return
        else: 
            print(">>> Data\n"+data)

  
html = ""       

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
print("*************************")    
parser = MyHTMLParser()
parser.feed(html)
parser.close()