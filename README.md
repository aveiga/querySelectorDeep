# querySelectorDeep

A Python method to traverse a DOM Tree (including shadowRoot) a find the first reference of a given match

# Usage

```python
#Normal usage
querySelectorDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view")

querySelectorAllDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view a")

#Debug mode
querySelectorDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view", False, True)

querySelectorAllDeep(chrome.find_element(
    By.XPATH, '//body'), "demo-view a", True)
```

# TO DO

- querySelectorAllDeep already supports nested search paths (like "demo-view div a"). querySelectorDeep should also support
