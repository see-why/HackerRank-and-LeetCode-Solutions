
# https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true

minutes = ['zero','one','two','three','four','five',
           'six','seven','eight','nine','ten',
           'eleven','twelve','thirteen','fourteen',
           'fifteen','sixteen','seventeen','eighteen',
           'nineteen','twenty','twenty one', 'twenty two',
           'twenty three','twenty four','twenty five',
           'twenty six','twenty seven','twenty eight',
           'twenty nine', 'thirty']
hours = ['zero','one','two','three','four','five',
         'six','seven','eight','nine','ten','eleven','twelve']
         
def timeInWords(h, m):
    # Write your code here
    if m == 0:
        return hours[h] + " o' clock"
    elif m == 15:
        return "quarter past " + hours[h]
    elif m == 30:
        return "half past " + hours[h] 
    elif m == 45:
        if h == 12:
            return "quarter to " + hours[1]
        else:
            return "quarter to " + hours[h+1]
    elif m > 0 and m < 30:
        if m == 1:
            return minutes[m] + " minute past " + hours[h]
        else:
            return minutes[m] + " minutes past " + hours[h]
    elif m > 30 and m < 60:
        if h == 12:
            return minutes[60-m] + " minutes to " + hours[1]
        else:
            return minutes[60-m] + " minutes to " + hours[h+1]
