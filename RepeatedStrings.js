//https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

function repeatedString(s, n) {
    // Write your code here
    let a_count = 0;
    let remaining_a_counter = 0;
    
    s.split('').forEach((item) => item === 'a' && a_count++);
    const size = s.length;
    const repeated_string_count = Math.floor(n/size);
    const remaining_characters_count = n % size;

    if (remaining_characters_count !== 0){
        const last_s = s.substring(0,remaining_characters_count);        
        last_s.split('').forEach((item) => item === 'a' && remaining_a_counter++);
    }
  
    return ((a_count * repeated_string_count) + remaining_a_counter)
}
