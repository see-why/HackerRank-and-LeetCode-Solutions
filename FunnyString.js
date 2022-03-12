// https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

    public static string funnyString(string s)
    {
        string reverse = new string(s.ToCharArray().Reverse().ToArray());
        Console.WriteLine(reverse);
        string response = "Funny";
        
        for (int i=0; i<s.Length-1; i++){
            if(Math.Abs(s[i] - s[i+1]) != Math.Abs(reverse[i] - reverse[i+1])){
                response = "Not Funny";
                break;
            }
        }
        
        return response;
    }
