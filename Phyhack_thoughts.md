# Pyghack Thoughts on the Urbana Trees and Green Infrastructure dataset

## 1. Don't use .csv, use .tsv
The provided dataset entitled "tree_inventory.csv" had an issue with extra commas used in the notes section, column 3, as well as the species name column, column 8, caused the data to be split at these commas and then shift all the following data over a column or two, which ultimately, added two extra columns to the entire dataset. While the informative data was only in 60 columns, the extra commas present in the notes sections added 2 columns for 62 total columns, giving the majority of data two extra blank columns. This made working with the data difficult, in that all rows with the extra commas had incorrect data and had to be removed or corrected before any data analysis could be done. This problem can be easily fixed in two ways:
1) Use a .tsv file
Tabs are not used very often while writing notes/entering data, and thus a .tsv that is separated by tabs is much less likely to get these data shifting errors
2) Make sure that no one entering data in this dataset ever enters a comma in any field
If converting to a .tsv is not appealing, then make sure that any user who enters data in this dataset does not enter a comma as it will mess up the data for later analyses. You could use a semicolon in place of a comma when writing notes to avoid this issue as well.
