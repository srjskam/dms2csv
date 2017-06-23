# dms2csv

Convert multiband sonar data into latitude/longitude/depth points.

[NOAA](https://maps.ngdc.noaa.gov/viewers/bathymetry/) (probably among others) provides their multiband
sonar bathymetry data in .dms format, which is a simpleish fixed field width text file. 
This script converts it into a comma-separated list (latitude, longitude, depth), which should be easy to import
into any GIS program.

Requirements: Python >3.0

Usage: Provide a file name or pipe the data to stdin, .csv is printed to stdout.

`./dms2csv.py path/to/data.dms > output.csv`

NOAA data comes zipped, so you might do something like

`for a in path/to/data/*.gz; do gunzip --stdout $a ; done | ./dms2csv.py > output.csv`


