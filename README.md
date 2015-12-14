# automate_patch_arista_switch
This python script uses ssh2, a hostlist CSV and an ftp server to patch arista switches automatically

This script has two options:

For a unique IP - only one switch is affected
For a group of IPs - all switches are going to be patched

Make sure to comment and uncomment the right option inside the .py file
The default is a group of switches

Setting the environment
===========
- Install Virtual Environments 

    http://docs.python-guide.org/en/latest/dev/virtualenvs/
- Activate the venv

    **$ source .venv/bin/activate**
- Install the requeriments

    **$ pip install -r requirements.txt**

Running the script
===========
- Execute to patch only one host

    **$ python autopatch.py --hostname 10.0.1.139 --username khyron --password
$(cat /tmp/key) --ftpserver ftpserver.local

- Execute to patch multiple using hostlist.csv list

    **$ python autopatch.py --username khyron --password $(cat
/tmp/key) --hostlist hostlist.csv --ftpserver ftpserver.local

Script help
===========

<pre>
$ python autopatch.py -h
usage: autopatch.py [-h] [--hostname HOSTNAME] --ftpserver FTPSERVER
                    [--port PORT] --username USERNAME --password PASSWORD
                    [--hostlist HOSTLIST]

Using a hostlist and an ftp server patch ARISTA switches.

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   Single switch to path (ignored if --hostlist is used)
  --ftpserver FTPSERVER
                        FTP server where path file is stored
  --port PORT           port where sshd is running (default 22)
  --username USERNAME   Username to connec to switch
  --password PASSWORD   Password to connect to switch
  --hostlist HOSTLIST   Path to hostlist in CSV format
</pre>
