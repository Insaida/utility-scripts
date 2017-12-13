#!/usr/bin/env python3
import os
import re
from collections import Counter


def log_reader(logfile):
    '''
     Function to read and analyse the log file. Opens the logfile,
      assigns it to a variable, reads it and print output to stdout
     '''
    # Regex to pick out ip addresses
        regexr = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        with open(logfile) as _:
            log = _.read()
            ip_addy = re.findall(regexr, log)

            ip_addy_count = Counter(ip_addy)
            print "Total IP addresses:", len(ip_addy_count), "\n"
            print "Top 10 IP Addresses        " + "   Total Requests made\n"
            val = ip_addy_count.most_common(10)
            for key, value in val:
                print "IP Address: " + "==> " + str(key) + " | " + "Requests " + "==> " + str(value)

            urls = re.findall(
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', log)
            urls_count = Counter(urls)
            urld = urls_count.most_common(10)

            for k, vat in urld:
                if vat > 1:
                    print "Requested URLs: " + "==> " + str(k) + " | " + "Requests " + "==> " + str(vat)

        #succes_requess = os.system("cat logfile.log| grep '\" 200'")
        #successful_requests_count = Counter(succes_requess)
        # print successful_requests_count


if __name__ == "__main__":
    log_reader('logfile.log')
