#!/usr/bin/env python2.7
#coding: utf-8

def logical_lines(physical_lines,joiner=''.join):
    logical_line = []
    for line in physical_lines:
        stripped = line.rstrip()
        if stripped.endswith('\\'):
            #带有下一个物理行的逻辑行
            logical_line.append(stripped[:-1])
        else:
            logical_line.append(line)
            yield joiner(logical_line)
            logical_line = []
    if logical_line:
        #序列的结束也意味着最后一个逻辑行的结束
        yield joiner(logical_line)

if __name__ == '__main__':
    text = 'some\\\n','lines\\\n','get\n','joined\\\n','up\n'
    for line in text:
        print 'P:',repr(line)
    for line in logical_lines(text,' '.join):
        print 'L:',repr(line)
