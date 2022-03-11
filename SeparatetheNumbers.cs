// https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true

class Result
{

    /*
     * Complete the 'separateNumbers' function below.
     *
     * The function accepts STRING s as parameter.
     */

    private static bool Beautiful(long A, string S)
    {
        if (string.IsNullOrEmpty(S)) return true;
        string A1 = (A + 1).ToString();
        if (S.StartsWith(A1)) return Beautiful(A + 1, S.Substring(A1.Length));
        return false;
    }
    
    public static void separateNumbers(string s)
    {
         bool b = false;
        long A = 0;
          for (int i = 1; i <= s.Length / 2; i++)
            {
                A = long.Parse(s.Substring(0, i));
                if (Beautiful(A, s.Substring(i)))
                {
                    b = true;
                    break;
                }
            }
            Console.WriteLine(b ? string.Format("YES {0}", A) : "NO");
    }

}
