//https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

class Solution
{
    public static void Main(string[] args)
    {
        string S = Console.ReadLine();
        try{
            int result = int.Parse(S);
            Console.WriteLine(result);
        } catch {
            Console.WriteLine("Bad String");
        }
    }
}
