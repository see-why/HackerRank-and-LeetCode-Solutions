// https://www.hackerrank.com/challenges/find-the-median/problem?isFullScreen=true

    public static int findMedian(List<int> arr)
    {
        arr.Sort();
        int median_index = arr.Count/2;
        return arr[median_index];
    }
