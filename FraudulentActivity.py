# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true

def activityNotifications(expenditure, d):
    # Write your code here
    v = sorted(expenditure[: d])
    count = 0
    for i, current in enumerate(expenditure[d:]):
        de = expenditure[i]
        if d%2 == 0:
            if current >= v[d//2] + v[d//2-1]:
                count += 1
        elif current >= v[d//2]*2:
                count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
    return count
