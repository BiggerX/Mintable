import time
import os
from dotenv import load_dotenv


def Mintable_Listing(browser, count, token_price, file_name, db, collection_name, collection_title, collection_subtitle, collection_description):
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

        print("Successfully logged into Mintable! :)")
    except:
        # * If failure, we are already logged in
        # print("Failed to login to Mintable! :(")
        time.sleep(3)

    main_window_handle = browser.current_window_handle

    # * Try to Connect Metamask
    try:
        browser.refresh()
        time.sleep(5)
        # browser.get('https://mintable.app/gasless')
        # * Click on Connect a Wallet
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div/div[2]/button').click()
        time.sleep(3)
        # * Click on Metamask logo
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div/div[1]/div/div/img').click()
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
            print("Successfully logged into Metamask :)")
        except:
            print("Failed to login to Metamask :(")

        time.sleep(3)
        # * Click on Metamask Next
        browser.find_element_by_xpath(
            '//*[@id = "app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
        time.sleep(2)
        # * Click on Metamask Connect
        browser.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    except:
        pass
        # print("Failed to connect Metamask...")

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
    tokenName.send_keys(collection_title)

    # * Input Listing Title
    listingTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[4]/input')
    listingTitle.send_keys(collection_title)

    # * Input Listing SubTitle
    listingSubTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[5]/input')
    listingSubTitle.send_keys(collection_subtitle)

    # * Upload Image
    firstUploadElement = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[7]/input')  # .click()
    # browser.switchTo().frame("batchLoad:inputFile:uploadFrame")
    firstUploadElement.send_keys(os.getcwd() + '/' + file_name)
    time.sleep(20)

    secondUploadElement = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[10]/div/div/div[1]/input')
    secondUploadElement.send_keys(os.getcwd() + '/' + file_name)

    time.sleep(300)

    # * Input Metadata Title
    metadataTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[11]/div/div[1]/input')
    metadataTitle.send_keys(collection_title)
    metadataSubTitle = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[11]/div/div[2]/div/input')
    metadataSubTitle.send_keys(collection_subtitle)
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[13]/div[2]/div/p').click()
    metadataDescription = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[13]/div[2]/div/p')
    metadataDescription.send_keys(collection_description)

    # browser.find_element_by_tag_name("p").innerText = 'Part ' + str(
    #     count) + ' in the abstract automation series by Ladons Imperium. The abstract, simplistic automation of ever generalizing computers touches upon our lives in often unnoticeable aspects.'

    # * Click Transfer Copyright
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/form/div[14]/div[1]/div/div/input').click()

    # * Input Item Price
    itemPrice = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/form/div[16]/div/div/input')
    itemPrice.send_keys(token_price)

    # * Wait for mintable verifying upload
    time.sleep(5)

    try:
        # * LIST THE ITEM
        browser.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div/form/div[17]/button').click()
        time.sleep(2)
        print("Successfully listed item!")
    except:
        print("Failed to list item!")

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
    browser.switch_to.window(main_window_handle)

    print("Item ", file_name, " listed!")

    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/button').click()

    # * Wait for webpage to load
    time.sleep(2)

    # * Store Art name and url in db
    data = {
        "name": collection_title,
        "url": browser.current_url
    }

    snapshots = list(db.collection(collection_name).get())
    prev_array = []
    for snapshot in snapshots:
        if 'art' in snapshot.to_dict().keys():
            prev_array = snapshot.to_dict()['art']

    doc_ref = db.collection(collection_name).document(u'art_list')

    doc_ref.update({
        'art': prev_array + [data],
    }, {merge: true})

    print("Successfully uploaded data to firebase!")

    # * Give time for database to asynchronously update
    time.sleep(5)

    browser.quit()

    time.sleep(2)
