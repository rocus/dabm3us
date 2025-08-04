#!/usr/bin/python3
import json

def gen_m3u ( station ):
    name = station [ 'stationName' ] . rstrip () 
    sid  = station [ 'stationSId'  ]
    chn  = station [ 'channelName' ]
    print  ( name , hex(sid) , chn )
    with open ( name+'.m3u' , 'w' ) as p:
        p.write ( '#EXTM3U\n#EXTINF:-1,'+name+'\nhttp://10.0.2.162:8888/mp3/'+hex(sid)+'/'+chn+'\n' )
        p.close 

with open('stations.json') as f:
    stations = json.load(f)
    for station in stations:
        gen_m3u ( station )
