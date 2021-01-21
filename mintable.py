import urllib.request
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
import chromedriver_binary  # * Adds chromedriver binary to path
from firebase import Firebase


def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(
        "--user-data-dir=/Users/andreasbigger/Library/Application Support/Google/Chrome Canary/Default")

    load_dotenv()

    apiKey = os.getenv('FIREBASE_API_KEY')
    authDomain = os.getenv('FIREBASE_AUTH_DOMAIN')
    dbUrl = os.getenv('FIREBASE_DATABASE_URL')
    storageBucket = os.getenv('FIREBASE_STORAGE_BUCKET')

    config = {
        "apiKey": apiKey,
        "authDomain": authDomain,
        "databaseURL": dbUrl,
        "storageBucket": storageBucket
    }

    firebase = Firebase(config)
    db = firebase.database()
    print(db.child("art").get())
    count = len(db.child("art").get())

    # * Initiate the browser
    browser = webdriver.Chrome(options=options)

    while(1):
        # * Open Random Art
        browser.get('https://www.randomart.co.uk/')

        # * Draw New Image
        browser.find_element_by_id('content_btnDrawNew').click()

        time.sleep(4)

        # * Fetch Image Source
        img = browser.find_element_by_xpath('//*[@id="content_imgArt"]')
        src = img.get_attribute('src')
        art_name = "./image_downloads/automated_art_" + str(count) + ".png"

        # * Download the image
        urllib.request.urlretrieve(src, art_name)
        print(count, ": Downloaded ", art_name)

        Mintable_Listing(browser, count, art_name, db)
        count += 1


def Mintable_Listing(browser, count, art_name, db):
    browser.get('https://mintable.app/gasless')

    # * Try to Login to Mintable
    try:
        # * Fetch environment variables
        username = os.getenv('MINTABLE_USERNAME')
        password = os.getenv('MINTABLE_PASSWORD')

        print("Read in username successfully from .env file: ",
              str(len(username) > 0))
        print("Read in password successfully from .env file: ",
              str(len(password) > 0))

        # * Input Username
        tokenName = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/form/div[1]/input')
        tokenName.send_keys(username)

        # * Input Password
        tokenName = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/form/div[2]/div/input')
        tokenName.send_keys(password)

        # * Click Sign In
        browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/form/div[4]/button').click()

        time.sleep(4)

        # * Continure to gasless factory
        browser.get('https://mintable.app/gasless')

        time.sleep(3)

        print("Successfully logged in! :)")
    except:
        print("Failed to login to mintable! :(")
        time.sleep(3)

    main_window_handle = browser.current_window_handle

    # * Try to Connect Metamask
    try:
        # * Click on Connect a Wallet
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div/div[2]/button').click()
        # * Click on Metamask logo
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div/div[1]/div').click()
        time.sleep(3)

        # * In case we need to login to metamask
        try:
            time.sleep(3)
            password = os.getenv('METAMASK_PASSWORD')
            print("Successfully read metamask password from .env file: ",
                  str(len(password) > 0))

            # * Switch to popup window
            signin_window_handle = None
            while not signin_window_handle:
                for handle in browser.window_handles:
                    if handle != main_window_handle:
                        signin_window_handle = handle
                        break
            browser.switch_to.window(signin_window_handle)

            # * Input Password
            tokenName = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/form/div/div/input')
            tokenName.send_keys(password)
            # * Click Unlock
            browser.find_element_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/button').click()
        except:
            print("Failed to login to metamask :(")

        time.sleep(3)
        # * Click on Metamask Next
        browser.find_element_by_xpath(
            '//*[@id = "app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
        time.sleep(2)
        # * Click on Metamask Connect
        browser.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()

    except:
        print("Failed to connect metamask...")

    # * Switch back to main window
    browser.switch_to.window(main_window_handle)
    time.sleep(3)

    # * LIST ITEM
    # * Click Art as category
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[1]/div/div[1]/a').click()

    # * Input Token Name
    tokenName = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[3]/input')
    tokenName.send_keys('Abstract Series Token ' + str(count))

    # * Input Listing Title
    listingTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[4]/input')
    listingTitle.send_keys('Abstract Series Token ' + str(count))

    # * Input Listing SubTitle
    listingSubTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[5]/input')
    listingSubTitle.send_keys(
        'Part ' + str(count) + ' in the abstract automation series by Ladons Imperium')

    # * Upload Image
    firstUploadElement = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[7]/input')  # .click()
    # browser.switchTo().frame("batchLoad:inputFile:uploadFrame")
    firstUploadElement.send_keys(os.getcwd() +
                                 "/image_downloads/automated_art_" + str(count) + ".png")
    time.sleep(2)

    secondUploadElement = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[10]/div/div/div[1]/input')
    secondUploadElement.send_keys(os.getcwd() +
                                  "/image_downloads/automated_art_" + str(count) + ".png")

    time.sleep(2)

    # * Input Metadata Title
    metadataTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[11]/div/div[1]/input')
    metadataTitle.send_keys(
        'Abstract Series Token ' + str(count))
    metadataSubTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[11]/div/div[2]/div/input')
    metadataSubTitle.send_keys(
        'Part ' + str(count) + ' in the abstract automation series by Ladons Imperium')
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[13]/div[2]/div/p').click()
    metadataDescription = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[13]/div[2]/div/p')
    metadataDescription.send_keys(
        'Part ' + str(count) + ' in the abstract automation series by Ladons Imperium. The abstract, simplistic automation of ever generalizing computers touches upon our lives in often unnoticeable aspects.')

    # browser.find_element_by_tag_name("p").innerText = 'Part ' + str(
    #     count) + ' in the abstract automation series by Ladons Imperium. The abstract, simplistic automation of ever generalizing computers touches upon our lives in often unnoticeable aspects.'

    # * Click Transfer Copyright
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[14]/div[1]/div/div/input').click()

    # * Input Item Price
    itemPrice = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[16]/div/div/input')
    itemPrice.send_keys('35')

    # * Wait for mintable verifying upload
    time.sleep(5)

    # * LIST THE ITEM
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[17]/button').click()

    time.sleep(2)
    # * Click Proceed for Metamask Signing
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[2]/div[2]/div/button').click()

    time.sleep(2)

    # * Switch to popup window
    signin_window_handle = None
    while not signin_window_handle:
        for handle in browser.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    browser.switch_to.window(signin_window_handle)

    # * Sign the item!
    browser.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[3]/div/div[4]/button[2]').click()

    time.sleep(3)

    print("Item ", art_name, " listed!")

    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/button').click()

    # * Wait for webpage to load
    time.sleep(2)

    # * Store Art name and url in db
    data = {
        "name": 'Abstract Series Token ' + str(count),
        "url": browser.current_url
    }

    db.child("users").push(data)

    browser.quit()


# * Run main, dummy!
if __name__ == "__main__":
    main()
