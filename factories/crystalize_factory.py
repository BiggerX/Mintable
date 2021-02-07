import time
import os
from dotenv import load_dotenv
from selenium import webdriver
import firebase_admin
from firebase_admin import credentials, firestore
from factories.lib import crystalize
from pathlib import Path
from factories.utils import Mintable_Listing


def mint():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(
        "--user-data-dir=/Users/andreasbigger/Library/Application Support/Google/Chrome Canary/Default")

    # * Load environment variables
    try:
        load_dotenv()
        print("Successfully loaded environment variables.")
    except:
        print("Failed to load environment variables!")

    count = 1  # * Initialize to 1 if no collection in firebase
    db = {}
    collection_name = u'crystalize_series'
    main_name = 'crystalize'
    # * Load firebase database
    try:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection(collection_name)
        snapshots = list(db.collection(collection_name).get())
        for snapshot in snapshots:
            if 'art' in snapshot.to_dict().keys():
                count = len(snapshot.to_dict()['art']) + 1
        print("Successfully loaded data from firebase.")
    except:
        print("Failed to fetch from firebase!")

    # * List max_count items
    max_count = 4
    while(count <= max_count):
        # * Refresh titles with updated counts
        collection_title = 'Crystalize Series Token ' + str(count)
        collection_subtitle = ' Token Number ' + \
            str(count) + '/' + str(max_count)
        collection_description = 'Part ' + \
            str(count) + ' out of ' + str(max_count) + \
            ' in the Crystalize Series by Toxic Mushr00m.' + \
            'Nature\'s patterns present themselves everywhere in our daily lives.' + \
            'This series captures the essence of fragility demonstrated through crustalization.' + \
            'With this series, we have entered the mirror dimension'
        token_price = '36'

        # * Safely make images directory if it doesn't exist
        Path("images/" + main_name + "_series").mkdir(parents=True, exist_ok=True)

        file_name = "images/" + main_name + "_series/" + main_name + "_token_" + \
            str(count) + ".png"
        my_file = Path(file_name)

        background_image = "images/background_images/background_" + \
            str(count) + ".png"
        if not my_file.is_file():
            # * Create the art if file doesn't exist
            crystalize.main(
                file_name, background_image, main_name + " " + str(count), 1000, 1000)
        else:
            print("File already exists... proceeding to upload.")

        # * Initiate the browser
        browser = webdriver.Chrome(
            options=options, executable_path='./factories/utils/chromedriver')

        # * List art on mintable
        Mintable_Listing.Mintable_Listing(browser, count, token_price, file_name, db, collection_name,
                                          collection_title, collection_subtitle, collection_description)
        count += 1

    print("Finished uploading!")


# * Run main, dummy!
if __name__ == "__main__":
    mint()
