# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true


 public static int commonChild(string s1, string s2)
    {
        char[] first = s1.ToCharArray();
        char[] second = s2.ToCharArray();
        int n = second.Length;
        
        int[] lcs = new int[second.Length+1];
        
        for(int i=1; i<=first.Length; i++){
            int current = 0;
            for(int j=1; j<=second.Length; j++){
                int temp = lcs[j];
                if(first[i-1] == second[j-1]){
                    lcs[j] = current + 1;
                }else {
                    lcs[j] = Math.Max(lcs[j], lcs[j-1]);
                }
                current = temp;
            }
        }
        
        return lcs[n];
    }

