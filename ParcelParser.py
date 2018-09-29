#!/usr/bin/python

import sys
from lxml import etree
import numpy


##############
# A parser for the esriPopup (CSS Selector .esriPopup) when searching at
# http://ccgisc.maps.arcgis.com/apps/webappviewer/index.html?id=2b6f95344c3f4116a262c48b5497eda8
# by PIN.

# Get the string, or the empty string if the input is None
def sanitizeNone(s):
  if s is None:
    return ''
  return str(s)

def main():
  print("Running Pracel parser")
  print("Usage: ParcelParser.py htmlFilename [htmlFilename...]")

  datasetColumnTitles = []
  dataset = []

  for parcelHtmlFileName in sys.argv[1:]:

    with open(parcelHtmlFileName, "r") as parcelHtmlFile:
      parcelEtree = etree.HTML(parcelHtmlFile.read())

    nameElements = parcelEtree.xpath("""//td[@class="attrName"]""")
    names = [element.text for element in nameElements]

    if not datasetColumnTitles:
      datasetColumnTitles = names
    elif not numpy.array_equals(names):
      print(f"WARNING - UNEQUAL ARRAYS: {datasetColumnTitles} \nvs {names}")

    valueElements = parcelEtree.xpath("""//td[@class="attrValue"]""")
    values = [element.text for element in valueElements]
    dataset.append(values)

    # keyPairList = [
    #   (parcelKeyPair[0].text, parcelKeyPair[1].text)
    #   for parcelKeyPair in zip(nameElements, valueElements)
    # ]

  print ("Debug section")
  print(datasetColumnTitles)
  print(dataset)

  print("Dataset munging complete.")
  print('\t'.join(datasetColumnTitles))
  for row in dataset:
    print('\t'.join([sanitizeNone(item) for item in row]))

if __name__== "__main__":
  main()
