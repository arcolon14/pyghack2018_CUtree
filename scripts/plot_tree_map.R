#!/usr/bin/env Rscript

setwd('/mnt/c/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/scripts')
# Census tracts areas
tract <- read.delim('/mnt/c/Users/AngelRC/Desktop/other_datasets/tree/tract_005300.tsv')
# Tree inventory data
inven <- read.delim('/mnt/c/Users/AngelRC/Desktop/other_datasets/tree/tree_inventory.tsv')

# Libraries
library(scales)

# Create output PDF
pdf('./urbana_trees.pdf', 8, 8)

# Create plot boundaries
min_x <- -88.24
max_x <- -88.16
min_y <- 40.07
max_y <- 40.15

# Create empty plot area
plot(inven$Lon, 
    inven$Lat,
    type='n',
    ylim=c(min_y,max_y),
    xlim=c(min_x,max_x),
    main='Urbana, IL Trees',
    xlab='Latitude',
    ylab='Longitude'
)
grid()



par(new=TRUE)
# Plot tree locations
points(inven$Lon, 
    inven$Lat,
    pch=19,
    col=alpha('darkgreen', 0.25)
)

par(new=TRUE)
# Add tract area
polygon(tract$long,
    tract$lat,
    col=alpha('grey35', 0.5),
    border=NA
)


.=dev.off()

