# MIKEMELD

Tracker system

## Name

MIKEMELD

## Description
This tool will help you track collection of IPs (see trackers), malicious or not, to build dynamic lists for your IPS systems. This project focus on making an output for PALOALTO Format but can be easily adapted after all.

## Installation

python3.10 is required since I added a switch case operator.

#Mariadb
yum install 'whaterver'

#requests: pip library for curl requests
python3.10 -m pip install requests

#mysql-connector-python: pip library for mysql requests
python3.10 -m pip install mysql-connector-python

#Database
see mysql_tables.txt to load the correct database scheme. 

#Secret
Secret file must be filled (secret.py)

dbuser="yourdbuser"
dbpass="yourdbpass"

## Usage

You can add trackers: with -a flag and -c flag (to name the category).
Then you can run: with -r flag.
Then you can output to your httpd root folder with -o.
```
$ python3 mikemeld.py -h
usage: mikemeld.py [options]

EDL process automation.

optional arguments:
  -h, --help            show this help message and exit
  -a https://somelist.com/ips.txt -c FEODOTRACKER, --addurl https://somelist.com/ips.txt -c FEODOTRACKER
                        Add an url, Category name is required
  -c FEODOTRACKER, --category FEODOTRACKER
                        Category name
  -r, --run             run database automated filling
  -t, --testrun         DEBUG Purpose
  -o /var/www/html/, --output /var/www/html/
                        Output to file, destination is required
```
## Support
You can contact me on my linkedin: https://linkedin.com/in/michaël-vandycke-0a453b3a/

## Trackers

Here is a list of trackers:

```
python3.10 mikemeld.py -a https://feodotracker.abuse.ch/downloads/ipblocklist_recommended_paloalto.txt -c FEODOTRACKER      
python3.10 mikemeld.py -a https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.txt               -c SSLBLACKLIST      
python3.10 mikemeld.py -a https://spamhaus.org/drop/drop.txt                                           -c SPAMHAUSDROP      
python3.10 mikemeld.py -a https://opendbl.net/lists/dshield.list                                       -c DSHIELD           
python3.10 mikemeld.py -a https://opendbl.net/lists/bruteforce.list                                    -c DSHIELDBRUTEFORCE 
python3.10 mikemeld.py -a https://opendbl.net/lists/blocklistde-all.list                               -c DSHIELDBLDE       
python3.10 mikemeld.py -a https://opendbl.net/lists/talos.list                                         -c DSHIELDTALOS      
python3.10 mikemeld.py -a https://opendbl.net/lists/sslblock.list                                      -c DSHIELDSSLABUSE   
python3.10 mikemeld.py -a https://reputation.alienvault.com/reputation.data                            -c ALIENVAULTREPDATA 
```


## Contributing
Feel free to contribute.

## Authors and acknowledgment
ASCO Industries - Michaël Vandycke

## License
    Mikemeld IP trackers
    Copyright (C) 2022  ASCO Industries - Michaël Vandycke

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Project status
It's doing well, some features could be added such as formatting options for other network appliances, header/footers for output, the possibility to whitelist some addresses if needed. Or something I haven't thought about.
