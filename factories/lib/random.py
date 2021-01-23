import urllib.request
import time

def downloadRandomArt(browser, file_name):
    # * Open Random Art
    browser.get('https://www.randomart.co.uk/')

    # * Draw New Image
    browser.find_element_by_id('content_btnDrawNew').click()

    time.sleep(4)

    # * Fetch Image Source
    img = browser.find_element_by_xpath('//*[@id="content_imgArt"]')
    src = img.get_attribute('src')

    # * Download the image
    urllib.request.urlretrieve(src, file_name)
    print(count, ": Successful download! Item: ", file_name)
