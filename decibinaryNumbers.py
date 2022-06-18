# https://www.hackerrank.com/challenges/decibinary-numbers/problem?isFullScreen=true

def log(fmt, *args, **kwds):
    if not log.verbose:
        return
    print(fmt.format(*args, **kwds), file=sys.stderr)
log.verbose = False


def makeTable(dmax):
    bits = math.ceil(math.log2(dmax))
    table = [[0]*dmax for _ in range(bits)]
    for ii in range(10):
        table[0][ii] = 1
    for bit in range(1, bits):
        m2 = 1 << bit
        t0 = table[bit]
        t1 = table[bit-1]
        # Limit line to number of possible values that can be represented with
        # the current number of decibits
        maxlen = 10**(bit+1)
        if maxlen > dmax:
            maxlen = dmax
        for ii in range(maxlen):
            # NB: min() is slower than a conditional
            pmax = ii//m2
            if pmax > 9:
                pmax = 9
            # NB: sum() is slower than a for loop
            total = 0
            for pos in range(ii - pmax*m2, ii + m2, m2):
                total += t1[pos]
            t0[ii] = total
    return table

lookup = makeTable(287000)
agg = lookup[-1][:]
for ii in range(1, len(agg)):
    agg[ii] += agg[ii-1]
#print(lookup[-1], file=sys.stderr)
#print(agg, file=sys.stderr)

def decibinaryHelper(num, x):
    pos = 0
    result = 0
    for bit in range(len(lookup)-1, 0, -1):
        #log('num={} bits={}', num, bit)
        digit = 1 << bit
        tl = lookup[bit-1]
        for kk in range(0, (num//digit) + 1):
            remain = num - kk*digit
            #log('d={} r={}', kk*digit, remain)
            count = tl[remain]
            #log('p={} k={} c={}', pos, kk, count)
            if (pos + count) <= x:
                pos += count
            else:
                # Found the correct digit
                result = (result * 10) + kk
                #log('d={} r={} rem={}', kk, result, remain)
                num = remain
                break
    result = (result * 10) + num
    return result

def findNum(x):
    start = 1
    end = len(agg) - 1
    while start != end:
        num = (start + end) // 2
        if agg[num] == x:
            return num
        elif agg[num] > x:
            end = num
        else:
            start = num + 1
    return start

def decibinaryNumbers(x):
    if x == 1:
        return 0
    if x > agg[-1]:
        raise ValueError(x)
    # for num in range(1, len(agg)):
    #     if agg[num] >= x:
    #         break
    num = findNum(x)
    pos = agg[num-1] + 1
    result = decibinaryHelper(num, x-pos)
    return result
