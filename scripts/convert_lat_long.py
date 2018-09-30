#!/usr/bin/env python3

#
# function to generate latitude from the Y coordinate value
# Y vals are obtained from the `tree_inventory` file
# Latitude vals are in the Y axis. limits obtained from TreeKeeper
# Follows basic y = mx+b formula
def get_lat_from_Y(y_val):
    # Limits in `tree_inventory` coordinates
    x1 = 1240536.45
    x2 = 1265544.09
    # Limits in TreeKeeper coords
    y1 = 40.073002
    y2 = 40.14166
    # y=mx+b; lat = y; y_val = x
    m = (y2 - y1)/(x2 - x1)
    b = -1*(m*x1) + y1
    lat = (m * y_val) + b
    return lat

#
# function to generate longitude from the x coordinate value
# X vals are obtained from the `tree_inventory` file
# Longitude vals are in the Y axis. limits obtained from TreeKeeper
# Follows basic y = mx+b formula
def get_lon_from_X(x_val):
    # Limits in `tree_inventory` coordinates
    x1 = 1013422.66
    x2 = 1031994.86
    # Limits in TreeKeeper coords
    y1 = -88.229036
    y2 = -88.162682
    # y=mx+b; lon = y; x_val = x
    m = (y2 - y1)/(x2 - x1)
    b = -1*(m*x1) + y1
    lon = (m * x_val) + b
    return lon



X = 1016282.71
Y = 1255615.13

print( '{} - {}'.format( get_lat_from_Y(Y), get_lon_from_X(X) ) )