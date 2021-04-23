import xml.etree.ElementTree as etree

# with open('podcasts.opml', 'rt') as f:
#     tree = ElementTree.parse(f)

# print tree


maxdepth = 0
def depth(elem, level):
    global maxdepth
    # for child in elem:
    #     print(child.tag)
    # your code goes here
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level+1)
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)