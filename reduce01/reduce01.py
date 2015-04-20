# -*- coding: utf-8 -*-
import csv, sys
from datetime import datetime

def main(input_file, output_file):
    csvfile = open(input_file, 'r')
    reader = csv.DictReader(csvfile, delimiter=';', fieldnames=['date', 'uid'])

    counter = 0
    uids = {}
    dt_tpl = '%Y-%m-%d'
    for line in reader:
        uid = int(line['uid'])
        uids.setdefault(uid, [])
        uids[uid].append(line['date'])
        # if counter > 3000:
        #     break
        counter += 1

    summary = [(datetime.strptime(dates[-1], dt_tpl) - datetime.strptime(dates[0], dt_tpl)).days for dates in uids.values()]
    uniq_days = list(set(summary))
    count_of_uids = [summary.count(i) for i in uniq_days]
    # print uids
    # print summary
    # print zip(uniq_days, count_of_uids)

    acc_count_of_uids = count_of_uids[::-1]
    sum = 0
    for index, val in enumerate(count_of_uids):
        acc_count_of_uids[index] += sum
        sum = acc_count_of_uids[index]

    # print zip(uniq_days, acc_count_of_uids[::-1])
    with open(output_file, 'w') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerows(zip(uniq_days, acc_count_of_uids[::-1]))
    print 'input file: ' + input_file
    print 'output file: ' + output_file

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file, output_file = sys.argv[1:]
    else:
        input_file = 'cookies_sorted.csv'
        output_file = 'cookies_lifetime.csv'

    main(input_file, output_file)