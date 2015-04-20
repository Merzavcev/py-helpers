# -*- coding: utf-8 -*-
import csv
from datetime import datetime

csvfile = open('cookies_sorted.csv', 'r')
reader = csv.DictReader(csvfile, delimiter=';', fieldnames=['date', 'uid'])

def main():
    counter = 0
    uids = {}
    dt_tpl = '%Y-%m-%d'
    for line in reader:
        uid = int(line['uid'])
        uids.setdefault(uid, [])
        uids[uid].append(line['date'])
        # if counter > 300000:
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
    with open('cookies_lifetime.csv', 'w') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerows(zip(uniq_days, acc_count_of_uids[::-1]))


if __name__ == '__main__':
    main()