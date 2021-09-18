import textwrap

def wrap(string, max_width):
    a=True
    for i in range(1,len(string)//max_width+1):
        if a:
            j=0
            a=False
        string=string[0:i*max_width+j]+'\n'+string[i*max_width+i-1:len(string)]
        j+=1
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)