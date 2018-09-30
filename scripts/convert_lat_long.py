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


# Take cleaned tree inventory file and add Lat and Lon data
old_tree = '/mnt/c/Users/AngelRC/Desktop/other_datasets/tree/tree_inventory.tsv'
new_tree = '/mnt/c/Users/AngelRC/Desktop/pyghack2018/pyghack2018_CUtree/cleaned_tree_data/tree_inventory.tsv'
new_file = open(new_tree, 'w')
for i, line in enumerate(open(old_tree)):
    fields = line.strip('\n').split('\t')
    # Modify header
    if i == 0:
        fields.append('Lat')
        fields.append('Lon')
    else:
        # Calculate new Lat and Lon values
        fields.append(str(get_lat_from_Y(float(fields[59]))))
        fields.append(str(get_lon_from_X(float(fields[58]))))
    # format and write to file
    new_file.write('{}\n'.format('\t'.join(fields)))


new_file.close()