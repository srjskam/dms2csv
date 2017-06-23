#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for a in *.gz; do gunzip --stdout $a ; done | ./dms2csv.py > output.csv

from math import asin,sin,cos,radians,degrees
import fileinput

def chop(s,n):
    return float(s[:n].strip()), s[n:]

# 1° is 1° going N-S
degreespermeterLat = degrees(asin(1/6.371e6))
# = 360/40.075e6

# but not E-W
def degreespermeterLon(lon):
    return cos(radians(lon))*degreespermeterLat
    
coords=[]
for s in fileinput.input():
    if len(s) != 176:
        continue
    _,s = chop(s, 5)
    _,s = chop(s, 5)
    latdeg,s = chop(s,4) 
    latmin,s = chop(s,6) 
    londeg,s = chop(s,4) 
    lonmin,s = chop(s,6) 
    lat = latdeg+latmin/60.0
    #print(lat)
    lon = londeg+lonmin/60.0
    speed,s = chop(s,5) 
    bearing,s = chop(s,5) 
    depths =[]
    dists = []
    for i in range(15):
        dep, s = chop(s,4)
        depths.append(dep)
    for i in range(15):
        dist, s = chop(s,5)
        dists.append(dist)
    #print(depths)
    #print( dists)
    for dep,dis in zip(depths, dists):
        coords.append((lat+dis*degreespermeterLat      *sin(radians(-bearing))
                     , lon+dis*degreespermeterLon(lon) *cos(radians(-bearing))
                     , dep))
for lat, lon, dep in coords:
    print("{},{},{}".format(lat,lon,dep))
