'''
Write a function that will take a string, and return a run length encoded string, 
where a 'run' is an uninterrupted sequence of the same character.

In the output string the following rules are applied :
    A run of length 1 is encoded as just the character on it's own
    A run of length 2 is encoded as two of the same characters
    A run of length 3 or more and less than 10 is encoded as a single character, followed by a a single digits from 3 to 9
    A run of length more than or equal to 10 are encoded as if they are one or more runs of length 9 and then a smaller run for the remainder

Example
    Input string : aabbbbccd
    Output string : aab4ccd

Example
    Input string : hhgggggiiippp
    Output string : hhg5i3p3

Example
    Input string : aaaggggggggggggvvvvhhh
    Output string : a3g9g3v4h3
'''
def run_length_encoder(string):
    count=0
    string1=""
    for i in range (0,len(string)):  # 0-a, 1-a ,2-b ,3-b , 4-b, 5-b, 6-c, 7-c, 8-c  len=9
        temp_str=string[i]
        if i != len(string)-1:
            if string[i]==string[i+1]:
                count+=1
            else:
                count+=1
                if count==1:
                    string1+=string[i]
                elif count==2:
                    string1+=string[i]*int(count)
                elif count>=3 and count <=9:
                    string1+=string[i]+str(count)
                else:
                    string1+=string[i]+str(9)+string[i]+str(count-9)
                count=0
        else:
            if string[i]==string[i-1]:
                count+=1
                if count==1:
                    string1+=string[i]
                elif count==2:
                    string1+=string[i]*int(count)
                elif count>=3 and count <=9:
                    string1+=string[i]+str(count)
                else:
                    string1+=string[i]+str(9)+string[i]+str(count-9)
                count=0
            else:
                string1+=string[i]
            
    return string1

print(run_length_encoder("aaaggggggggggggvvvvhhh"))

