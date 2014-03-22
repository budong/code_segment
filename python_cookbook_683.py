#!/usr/bin/env python2.7
#coding: utf-8

def paragraphs(lines,is_separator=str.isspace,joiner=''.join):
    paragraph = []
    for line in lines:
        if is_separator(line):
            if paragraph:
                yield joiner(paragraph)
                paragraph = []
        else:
            paragraph.append(line)
    if paragraph:
        yield joiner(paragraph)

if __name__ == '__main__':
    #text = 'a first\nparagraph\n\nand a\nsecond one\n\n'
    #for p in paragraphs(text.splitlines(True)): print repr(p)

    import operator
    numbers = [1,2,3,0,0,6,5,3,0,12]
    bunch_up = paragraphs
    for s in bunch_up(numbers,operator.not_,sum):print 'S',s
    for l in bunch_up(numbers,bool,len):print 'L',l
