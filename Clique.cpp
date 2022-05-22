# https://www.hackerrank.com/challenges/clique/problem?isFullScreen=true

int get_calc(int m, int n) {
    int g1 = n % m;
    int g2 = m - g1;
    int sz1 = n / m + 1;
    int sz2 = n / m;

    return g1 * sz1 * g2 * sz2 + g1 * (g1 - 1) * sz1 * sz1 / 2 + g2 * (g2 - 1) * sz2 * sz2 / 2;
}

int clique(int n, int m) {
     int lo = 1, hi = n + 1, ret = -1;
    while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;

            if (get_calc(mid, n) < m)
                lo = mid;
            else hi = mid;
        }
        
    return hi;
}
