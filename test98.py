import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    a = 0
    # if node.attrib:
    #     print(node.tag, node.attrib)
    #     a += len(node.attrib)

    for child in node.iter():
        print(child.tag, child.attrib)
        a += len(child.attrib)
    return a

if __name__ == '__main__':
    #sys.stdin.readline()
    #xml = sys.stdin.read()
    xml = ""
    n = int(input())
    for i in range(n):
        xml += input()

    #print("xml file \n", xml)
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print("********************")
    print(get_attr_number(root))