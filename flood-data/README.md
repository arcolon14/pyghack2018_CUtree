Converting flood.tsv to UNIQUE, STREET, CITY, STATE, ZIP
Find: `^(\d+)(?:\t[^\t]+){5}\t([^\t]+)\t(\w+)[\s\t]+(\w+)[\s\t]+(\d+).*`
Replace: `$1, $2, $3, $4, $5`

The result can be found in flood-formatted-address-batch.csv, which is conformant to the census geocding API call.

```
curl --form addressFile=@flood-formatted-address-batch.csv --form benchmark=Public_AR_Current https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output geocoderesult.csv
```
