This repository describes an easy way to make the radio stations you can receive by a rtl-SDR dongle available in the form
of many m3u files a streamer might understand. In my repository welle-cli I describe a DAB radio receiver/server on a raspberry pi.

With welle-io you can do a radio scan of available radio stations. Welle-io can be installed on your PC or an a raspberry pi.
After a radio scan the results are saved in a configuration file. On linux this file might be in the ~/.config/welle.io directory as 
welle.io.conf. This file contains the radio stations you can receive with your dongle at your place.

First do the following:

grep stationListSerialize welle.io.conf | sed 's/stationListSerialize=\"// ; s/]\"/]/ ; s/\\//g'  > stations.json

Then run the welle.py program. This will generate many m3u files that your audio streamer clients can use.

In my case my radio server is a raspberry pi at 10.0.2.162:8888
You can ofcourse make changes in welle.py for your personal situation.
