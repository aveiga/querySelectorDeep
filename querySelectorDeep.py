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


def conditionalPrintNodeNames(condition, nodesList):
    if condition:
        printNodeNames(nodesList)


def isBlackListed(node):
    try:
        if node.tag_name == "script":
            return True

        if node.tag_name == "style":
            return True
    except:
        return True
    return False


def conditionalPrint(condition, value):
    if condition:
        print(value)


def evaluateMatch(n, m):
    "This is the function that should be extended to have other kinds of matches (By class? By id? By attribute?)"
    return n.tag_name == m


def querySelectorDeep(initialNode, match, all=False, debug=False):
    "This traverses the DOM Tree, including shadowRoot, searching for a match"
    toCheck = [initialNode]
    partialFindings = [initialNode]
    matches = match.split(" ")

    for m in matches:
        conditionalPrint(debug, "Looking at match: " + m)
        i = 0
        toCheck = partialFindings
        partialFindings = []
        conditionalPrintNodeNames(debug, toCheck)
        conditionalPrintNodeNames(debug, partialFindings)
        toCheckLength = len(toCheck)

        while len(toCheck) > 0:
            node = toCheck.pop(0)

            if isBlackListed(node):
                continue

            try:
                conditionalPrint(debug, "Looking at: " + node.tag_name)

                if evaluateMatch(node, m):
                    conditionalPrint(debug, "FOUND MATCH: " + node.tag_name)
                    if not all:
                        return node
                    partialFindings.extend([node])

                lightChildren = node.find_elements_by_xpath('./*')
                shadowRoot = chrome.execute_script(
                    'return arguments[0].shadowRoot', node)

                if len(lightChildren) > 0:
                    conditionalPrint(debug, len(lightChildren))
                    toCheck.extend(lightChildren)

                if shadowRoot != None:
                    shadowChildren = chrome.execute_script(
                        'return arguments[0].children', shadowRoot)
                    conditionalPrint(debug, len(shadowChildren))
                    toCheck.extend(shadowChildren)
            except:
                print(
                    "Got an error while traversing the DOM Tree for node: " + node.tag_name)

            conditionalPrintNodeNames(debug, toCheck)
    # print("not found...")
    return partialFindings


def querySelectorAllDeep(initialNode, match, debug=False):
    return querySelectorDeep(initialNode, match, True, debug)


print("Using querySelectorDeep----------")
result = querySelectorDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view")
printNodeNames([result])


print("Using querySelectorAllDeep----------")
result = querySelectorAllDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view a")
printNodeNames(result)

print("Using querySelectorDeep in debug mode----------")
result = querySelectorDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view", False, True)
printNodeNames([result])
