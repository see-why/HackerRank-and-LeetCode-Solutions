//https://www.hackerrank.com/challenges/countingsort1/problem?isFullScreen=true

class Result
{

    /*
     * Complete the 'countingSort' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static List<int> countingSort(List<int> arr)
    {
        int[] array = new int[100];
        
        for (int i=0; i<arr.Count; i++){
            array[arr[i]] += 1;
        }
        
        return array.ToList();
    }

}
