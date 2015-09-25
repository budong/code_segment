#!/usr/bin/python
#coding:utf-8

L1 = [1,2,3,4,5,100]
#L1 = [1425367801, 1425367801, 1425367802, 1425367801, 1425367801, 1425367802, 1425367501, 28800, 1425367801, 1425367801, 1425367801, 1425367801, 1425367802, 28800]
L2 = [1425367801 ,1425367801 ,1425367802 ,1425367801 ,1425367801 ,1425367802
        ,1425367501 ,28800 ,1425367801 ,1425367801 ,1425367801 ,1425367801 ,1425367802
        ,28800]
#L2 = [1,2,3,4,11,21,31,51,52,53,54]
#L2 = [1423623492,1423452755,1423623395,1423452755,1423452755,1423452755,1423452755,1423452755,1423539155,1423452755,1423452755,1423452755,1423452755]

def most_tuple_value(d):
    most = 0
    frequency = 0
    values_list = [v[1] for v in d]
    values_set = set(values_list)
    for value in values_set:
        if values_list.count(value) > frequency:
            frequency = values_list.count(value)
            most = value
    return  most

def same_tuple_value(d,v):
    l = []
    for key in d:
        if v == key[1]:
            l.append(key[0])
    return l

def remove_bad_person(l):
    d = []
    for i in range(len(l)):
        sum = 0
        for j in range(len(l)):
            if 0 <= abs(l[i] - l[j]) <= 5:
                sum += 1
            else:
                sum -= 1
        d.append((l[i],sum))
    print d
    most_value = most_tuple_value(d)
    print most_value
    same_value = same_tuple_value(d,most_value)
    print same_value

def main():
    print L1
    remove_bad_person(L1)
    print '*'*25
    print L2
    remove_bad_person(L2)

if __name__ == '__main__':
    main()
