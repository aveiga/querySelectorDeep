from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
# chrome.implicitly_wait(10)
chrome.get(
    "https://material-components.github.io/material-components-web-components/demos/index.html")


def printNodeNames(nodesList):
    try:
        for node in nodesList:
            print(node.tag_name)
    except:
        print("Got an error while printing the node tag name")


def isBlackListed(node):
    try:
        if node.tag_name == "script":
            return True

        if node.tag_name == "style":
            return True
    except:
        return True
    return False


def querySelectorDeep(initialNode, match):
    "This traverses the DOM Tree, including shadowRoot, searching for a match"
    toCheck = [initialNode]
    i = 0
    while len(toCheck) > 0:
        node = toCheck.pop(0)

        if isBlackListed(node):
            continue

        try:
            print("Looking at: " + node.tag_name)

            if node.tag_name == match:
                print("FOUND MATCH: " + node.tag_name)
                return node

            lightChildren = node.find_elements_by_xpath('./*')
            shadowRoot = chrome.execute_script(
                'return arguments[0].shadowRoot', node)

            if len(lightChildren) > 0:
                print(len(lightChildren))
                toCheck.extend(lightChildren)

            if shadowRoot != None:
                shadowChildren = chrome.execute_script(
                    'return arguments[0].children', shadowRoot)
                print(len(shadowChildren))
                toCheck.extend(shadowChildren)
        except:
            print("Got an error while traversing the DOM Tree for node: " + node.tag_name)

        printNodeNames(toCheck)
    print("not found...")
    return 0


querySelectorDeep(chrome.find_element(By.XPATH, '//body'), "a")
