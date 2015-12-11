#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Exscript.protocols import SSH2
from Exscript import Account
from time import sleep
import argparse
import csv
import sys
import re


def patch(hostname, ftpserver, username, password, sleep):
    try:
        print "[+] Patching host => IP: %s" % (repr(hostname))
        account = Account(username, password)
        conn = SSH2()
        conn.connect("%s" % hostname)
        conn.login(account)
        conn.execute("copy ftp://%s/secAdvisory0015.swix flash:" % ftpserver)
        sleep(sleep)
        conn.execute('copy flash:secAdvisory0015.swix extension:')
        sleep(sleep)
        conn.execute('extension secAdvisory0015.swix')
        sleep(sleep)
        conn.execute('copy installed-extensions boot-extensions')
        sleep(sleep)
        conn.execute('delete secAdvisory0015.swix')
        print "[+] Patching host OK => IP: %s\n" % (repr(hostname))
        conn.send('exit\r')
        conn.close()
    except Exception as e:
        if conn:
            conn.close()
        print e
        print "[-] Error patching host => IP: %s" % (repr(hostname))


def csv_read(path, switches):
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                switch = {}
                switch["description"] = row[0]
                switch["hostname"] = row[1]
                switch["ip"] = row[2]
                switches.append(switch)
        except csv.Error as e:
            exit('[-] File %s, line %d: %s' % (filename, reader.line_num, e))
    return switches


def args_parse():
    parser = argparse.ArgumentParser(description='Using a hostlist and an\
            ftp server patch ARISTA switches.')
    parser.add_argument("--hostname", type=str, help='Single switch to path\
            (ignored if --hostlist is used)')
    parser.add_argument("--ftpserver", type=str, required=True, help='FTP server\
            where path file is stored')
    parser.add_argument("--port", default="22", type=str, help='port where sshd\
            is running (default 22)')
    parser.add_argument("--username", type=str, required=True, help='Username \
            to connec to switch')
    parser.add_argument("--password", type=str, required=True, help='Password \
            to connect to switch')
    parser.add_argument("--hostlist", type=str, help='Path to hostlist in \
            CSV format')
    args = parser.parse_args()

    return args


def main():
    switches = []
    args = args_parse()

    if args.hostlist:
        switches = csv_read(args.hostlist, switches)
        for switch in switches:
            patch(switch["ip"], args.ftpserver, args.username, args.password, 2)
    elif args.hostname:
        patch(args.hostname, args.ftpserver, args.username, args.password, 2)


# Start program
if __name__ == "__main__":
    main()
