#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

def kaprekarNumbers(p, q):
    # Write your code here
    count = ''
    for i in range(p, q+1):
        i_s = len(str(i))
        i_p = i*i
        if (len(str(i_p)) == 2*i_s) or (len(str(i_p)) == (2*i_s) - 1):
            ii_s = len(str(i_p))
            f_s = str(i_p)[ii_s - i_s:]
            l_s = str(i_p)[:ii_s - i_s]
            l_s = '0' if l_s == '' else l_s
            f_s = '0' if f_s == '' else f_s
            if (int(f_s) + int(l_s)) == i:
                count += str(i) + ' '
    if len(count) > 0:
        print (count)
    else:
        print "INVALID RANGE" 
