//https://www.hackerrank.com/challenges/30-more-exceptions/problem?isFullScreen=true

class Calculator {
    public int power(int n, int p){
        int result = 1;
        if ( n < 0 || p < 0){
            throw new Exception("n and p should be non-negative");
        } else {
            for (int i=0; i<p; i++){
                result *= n;
            }
        }
        return result;
    }
}
