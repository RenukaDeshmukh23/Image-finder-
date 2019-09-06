import webbrowser,os,selenium

os.makedirs('Images',exist_ok=True)
search=input("What u want to search?")

webbrowser.open("https://www.flickr.com/search/?text="+search)

try:
    elem=browser.find_element_by_class_name('download')
    print('Found <%s> element with that class name!'%(elem.tag_name))
except:
    print("Unable to find")
