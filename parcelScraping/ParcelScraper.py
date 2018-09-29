#!/usr/bin/python

import ParcelParser

import sys
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
driverLocation = ChromeDriverManager().install()
chrome_options = Options()
# chrome_options.add_argument("--headless")

def scrapeEsriPopup(pin):
    global driverLocation
    global chrome_options

    driver = webdriver.Chrome(executable_path=driverLocation, chrome_options=chrome_options)
    driver.get("http://ccgisc.maps.arcgis.com/apps/webappviewer/index.html?id=2b6f95344c3f4116a262c48b5497eda8")
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.jimu-btn"))
        ).click()

        searchBar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".searchInputGroup input")))
        searchBar.send_keys(pin)
        # searchBar.send_keys(Keys.RETURN)
        searchBar.submit()

        esriPopup = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".esriPopup.esriPopupVisible")))
        esriPopupOuterHtml = esriPopup.get_attribute("outerHTML")
        return esriPopupOuterHtml

    finally:
        driver.quit()

debugParcelPinList = [
    912108328014,
    912107276030,
    922117184001,
    932121103031,
    932120476035,
    912107426015,
    932122402012,
    932117383010,
    932120281011,
    922117261010,
    912108153035,
    932117451011,
    932117451010,
    932120401019,
    912105477019,
    932120281005,
    912103101004,
    912108504003,
    922116128024,
    932121181006,
    932121178005,
    912107279022,
    912115355028,
    912108459007,
    922116104027,
    932121182005,
    932120476008,
    922117130016,
    922117233003,
    912108305003,
    932122304010,
    932120477004,
    912107204001,
    932121306011,
    932120451035,
    932120432007,
    932117451007,
    932121307002,
    932121356007,
    932121355004,
    922117157001,
    912108504003,
    922117102024,
    922116382024,
    922116380001,
    932120226001,
    932121201014,
    932121181011,
    932117357022,
    922117135014,
    922117234004,
    922116477006,
    922116327005
]

def breakApartStringyArgsIntoList(stringyArgs):
    return re.findall(r"[^,\s]+", stringyArgs)

def main():

    parcelPinList = []
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Usage: ParcelScraper.py")
            print("\tParcelScraper.py PIN [PINs...]")
            print("\tParcelScraper.py -f pinFile")
            print("\tpipe PIN numbers into | ParcelScraper.py")
            print()
            print("Pins can be separated by comma and/or whitespace (including newline).")
            quit()
        elif sys.argv[1] == "-f":
            # Read in a file of the PINs
            with open(sys.argv[2], 'r') as pinFile:
                parcelPinList.extend(breakApartStringyArgsIntoList(pinFile.read()))
        elif sys.argv[1] == "-d":
            # Use debug list of given PINS
            global debugParcelPinList
            parcelPinList = debugParcelPinList
        elif re.search(r"[,\s]+", sys.argv[1]):
            # Provided as a string list
            for stringyArgs in sys.argv[1:]:
                parcelPinList.extend(breakApartStringyArgsIntoList(stringyArgs))

        else:
            parcelPinList.extend(sys.argv[1:])
    else:
        print("Usage: ParcelScraper.py")
        print("\tParcelScraper.py PIN [PINs...]")
        print("\tParcelScraper.py -f pinFile")
        print("\tpipe PIN numbers into | ParcelScraper.py")
        print()
        print("Pins can be separated by comma and/or whitespace (including newline).")
        print()
        print("TODO accept STDIN piping")

    for pin in parcelPinList:
        esriPopupHtml = scrapeEsriPopup(pin)
        names, values = ParcelParser.parseParcelEsriPopup(esriPopupHtml)
        ParcelParser.addToDataset(names, values)

    print(ParcelParser.outputDatasetAsTsv())

if __name__== "__main__":
  main()
