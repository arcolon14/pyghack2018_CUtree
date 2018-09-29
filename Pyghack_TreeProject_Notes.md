# Pyghack Notes

## Goals and Ideas
Combine different datasets (tree location, flood complaints, and census data) to achieve better urban forest and stormwater outcomes.

# Info
Our contact: Scott Tess (srtess@urbanaillinois.us) Environmental Sustainability Manager for City of Urbana, Urbana Public Works

The PIN number in the flood data is a parcel number ID. We can look that up we can look up in the Urbana
  - [Champaign County Property Search Page](http://www.co.champaign.il.us/propsearch)
  - [Property Search by Map](http://ccgisc.maps.arcgis.com/apps/webappviewer/index.html)
city properties to get addresses/location

## To Do List:
1. Angel and Kira: Take a subset of variables to see which ones are informative
2. (ALL) Decide if we use flooding data: if yes, we need to get the addresses
  2a. Check how easy it is to get addresses (go to champaign county property lookup)
    - It's more informative to use the map to look up PIN (Permanent ) rather than the straight DB lookup:
    - http://ccgisc.maps.arcgis.com/apps/webappviewer/index.html
      - George: "Scrape" the values from these parcels using Python & BeautifulSoup

- Get each dataset to a point where we can heatmap it (roughly by priority)
  1. Trees
  2. Census
  3. Flood/Storm

#Census Data Ideas
Census variables we want to work with:
-Median income
-Property value
-Ethnicity
We want to combine these with:
-Tree density
-Flooding (complaints?)
