# https://www.hackerrank.com/challenges/fair-cut/problem?isFullScreen=true



function fairCut(n, k, arr) {
    arr.sort((a, b) => a - b);
    if (2 * k > n) k = n - k;
    const s = (n - 2 * k) >> 1;
    const e = s + 2 * k;
    let ans = 0;
    let sum1 = 0, cnt1 = 0;
    let sum2 = 0, cnt2 = 0;
    for (let i = 0; i < n; ++i) {
        const x = arr[i];
        if (s <= i && i < e && (i & 1)) {
            sum1 += x;
            cnt1 += 1;
            ans += cnt2 * x - sum2;
        } else {
            sum2 += x;
            cnt2 += 1;
            ans += cnt1 * x - sum1;
        }
    }
    return ans;
}
