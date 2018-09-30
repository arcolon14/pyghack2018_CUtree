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
# Parse the tracts to get per-tract polygons
geoID <- unique(tracts$tractAffGeoId)
cols = rainbow(length(geoID))
t1 <- subset(tracts, tracts$tractAffGeoId == geoID[1])
t2 <- subset(tracts, tracts$tractAffGeoId == geoID[2])
t3 <- subset(tracts, tracts$tractAffGeoId == geoID[3])
t4 <- subset(tracts, tracts$tractAffGeoId == geoID[4])
t5 <- subset(tracts, tracts$tractAffGeoId == geoID[5])
t6 <- subset(tracts, tracts$tractAffGeoId == geoID[6])
t7 <- subset(tracts, tracts$tractAffGeoId == geoID[7])
t8 <- subset(tracts, tracts$tractAffGeoId == geoID[8])
t9 <- subset(tracts, tracts$tractAffGeoId == geoID[9])
t10 <- subset(tracts, tracts$tractAffGeoId == geoID[10])
t11 <- subset(tracts, tracts$tractAffGeoId == geoID[11])
t12 <- subset(tracts, tracts$tractAffGeoId == geoID[12])
t13 <- subset(tracts, tracts$tractAffGeoId == geoID[13])


tiff("C:/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/UrbanaTreesTracts.tiff", 10, 10, units='in', res=300)
# Get map data from Google maps
map <- get_googlemap(center = c(lon=-88.208770, lat=40.110711), zoom=13, scale = 2, key=myKey)
ggmap(map, 
      extent='panel') +
  # Add tree coordinates
  geom_point(data = inven, aes(x=Lon, y=Lat), 
             col='darkgreen',
             alpha=0.35,
             shape=18,
             size=1.5) +
  # Add labels and title
  labs(x='Longitude', y='Latitude') +
  ggtitle('Urbana, IL Tree Inventory') +
  # Add tract polygons
  geom_polygon(data=t1, aes(long, lat), alpha=0.2, fill=cols[1]) +
  geom_polygon(data=t2, aes(long, lat), alpha=0.2, fill=cols[2]) +
  geom_polygon(data=t3, aes(long, lat), alpha=0.2, fill=cols[3]) +
  geom_polygon(data=t4, aes(long, lat), alpha=0.2, fill=cols[4]) +
  geom_polygon(data=t5, aes(long, lat), alpha=0.2, fill=cols[5]) +
  geom_polygon(data=t6, aes(long, lat), alpha=0.2, fill=cols[6]) +
  geom_polygon(data=t7, aes(long, lat), alpha=0.2, fill=cols[7]) +
  geom_polygon(data=t8, aes(long, lat), alpha=0.2, fill=cols[8]) +
  geom_polygon(data=t9, aes(long, lat), alpha=0.2, fill=cols[9]) +
  geom_polygon(data=t10, aes(long, lat), alpha=0.2, fill=cols[10]) +
  geom_polygon(data=t11, aes(long, lat), alpha=0.2, fill=cols[11]) +
  geom_polygon(data=t12, aes(long, lat), alpha=0.2, fill=cols[12]) +
  geom_polygon(data=t13, aes(long, lat), alpha=0.2, fill=cols[13])

.=dev.off()
