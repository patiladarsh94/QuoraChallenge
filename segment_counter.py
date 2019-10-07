'''  The challenge name is ‘segment_counter’ (you will need this for the framework).
You need to write a single function which takes a string as a positional argument, and counts the total number of ‘segments’ 
within the string. A segment is simply defined as a uninterrupted sequence of the same characters.

Example :
    Input string : abbccbbba
    Segments : a, bb, cc, bbb, a
    Segment Count : 5

Example:
    Input string : abca
    Segments : a, b, c, a
    Segment Count : 4 '''


def segment_counter(string):
    count=0
    for i in range (0,len(string)):
        temp_str=string[i]
        if i==len(string)-1:
            if string[i]!=string[i-1]:
                count+=1
            else:
                count+=1
        else:
            if string[i]==string[i+1]:
                temp_str+=string[i+1]
            else:
                count+=1 
                temp_str=" "
    return count

