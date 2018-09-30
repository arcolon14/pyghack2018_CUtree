library(ggplot2)
library(ggmap)
library(scales)
setwd("C:/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/scripts")
# Google Maps API Key
myKey <- 'AIzaSyDBUGfU7ktCj1IQE6Cf31JOiPKYiU1NL9E'
# Tree Inventory Data
inven <- read.delim("C:/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/cleaned_tree_data/tree_inventory.tsv")
# Census tract area
tracts <- read.delim("C:/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/Census_2017_Tract/urbana-tracts-latlong.tsv",
                     stringsAsFactors = FALSE)
 
# Get map data from Google maps
map <- get_googlemap(center = c(lon=-88.208770, lat=40.110711), zoom=13, scale = 2, key=myKey)
ggmap(map) +
  geom_point(data = inven, aes(x=Lon, y=Lat), col=alpha('darkgreen', 0.5), size=3)
