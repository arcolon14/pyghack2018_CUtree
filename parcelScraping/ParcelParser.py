#!/usr/bin/python

import sys
from lxml import etree
import numpy

##############
# A parser for the esriPopup (CSS Selector .esriPopup) when searching at
# http://ccgisc.maps.arcgis.com/apps/webappviewer/index.html?id=2b6f95344c3f4116a262c48b5497eda8
# by PIN.

datasetColumnTitles = []
dataset = []

# Get the string, or the empty string if the input is None
def convertNoneToEmptyString(s):
  if s is None:
    return ''
  return str(s)

def checkColumnNames(names):
  global datasetColumnTitles

  if not datasetColumnTitles:
    datasetColumnTitles = names
  elif not numpy.array_equal(names, datasetColumnTitles):
    print(f"WARNING - UNEQUAL ARRAYS: {datasetColumnTitles} \nvs {names}")

def parseParcelEsriPopup(html):
  parcelEtree = etree.HTML(html)
  nameElements = parcelEtree.xpath("""//td[@class="attrName"]""")
  names = [element.text for element in nameElements]

  checkColumnNames(names)

  valueElements = parcelEtree.xpath("""//td[@class="attrValue"]""")
  values = [element.text for element in valueElements]

  return names, values

def outputDatasetAsTsv():
  global datasetColumnTitles
  global dataset
  headerRow = '\t'.join(datasetColumnTitles)
  return headerRow + '\n' + '\n'.join(
    ['\t'.join(
      [convertNoneToEmptyString(item) for item in row]
    ) for row in dataset]
  )

def addToDataset(names, values):
  global dataset
  checkColumnNames(names)
  dataset.append(values)

def main():
  if len(sys.argv) <= 1:
    print("Usage: [python] ParcelParser.py htmlFilename [htmlFilenames...]")
    quit()

  for parcelHtmlFileName in sys.argv[1:]:
    with open(parcelHtmlFileName, "r") as parcelHtmlFile:
      names, values = parseParcelEsriPopup(parcelHtmlFile.read())
    addToDataset(names, values)

  print(outputDatasetAsTsv())

if __name__== "__main__":
  main()
