#!/usr/bin/env Rscript

setwd('/mnt/c/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/scripts')
# Census tracts areas
tracts <- read.delim('/mnt/c/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/Census_2017_Tract/urbana-tracts-latlong.tsv')
# Tree inventory data
inven <- read.delim('/mnt/c/Users/AngelRC/Desktop/other_datasets/tree/tree_inventory.tsv')

# Libraries
library(scales)

# Create output PDF
# pdf('./urbana_trees.pdf', 8, 8)
tiff('./urbana_tress.tiff', height=8, width=8, units='in', res=300)

# Create plot boundaries
min_x <- -88.24
max_x <- -88.16

min_x <- -88.25
max_x <- -88.1

min_y <- 40.07
max_y <- 40.15

min_y <- 40.05
max_y <- 40.15

# Create empty plot area
plot(inven$Lon, 
    inven$Lat,
    type='n',
    ylim=c(min_y,max_y),
    xlim=c(min_x,max_x),
    main='Urbana, IL Trees',
    xlab='Longitude',
    ylab='Latitude'
)
grid()

par(new=TRUE)
# Plot tree locations
points(inven$Lon, 
    inven$Lat,
    pch=19,
    col=alpha('darkgreen', 0.25)
)

geoID <- unique(tracts$tractAffGeoId)
cols = rainbow(length(geoID))

par(new=TRUE)
# Loop through all geoIDs and plot them
for (i in 1:length(geoID)){
  curr_id <- geoID[i]
  tract <- subset(tracts, tracts$tractAffGeoId == curr_id)
  
  polygon(tract$long,
          tract$lat,
          col=alpha(cols[i], 0.25),
          border=NA
  )

}



.=dev.off()

