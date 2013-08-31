#!/usr/bin/env python2.7

import sys

def dictify_logline(line):
    split_line = line.split()
    return { 'remote_host': split_line[0],'status': split_line[8],'bytes_sent': split_line[9],}

def generate_log_report(logfile):
    report_dic = {}
    for line in logfile:
        line_dic = dictify_logline(line)
        #print line_dic
        try:
            bytes_sent = int(line_dic['bytes_sent'])
        except ValueError:
            continue
        report_dic.setdefault(line_dic['remote_host'],[]).append(bytes_sent)
    return report_dic

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name,'r')
    except ValueError:
        print "You must specify a valid file to parse"
        print __doc__
        sys.exit(1)
    log_report = generate_log_report(infile)
    print log_report
    infile.close()
