function decryptPassword(s) {
    // Write your code here    
    let find= '*';
    let replace = '';
    
    while( s.indexOf(find) > -1)
    {
       var s = s.replace(find, replace);
    }
    
    let index = s.split('').findIndex(item => /[A-Z|a-z]/i.test(item));
    
    let i=0, r = s.slice(0,index);
    r = r.split('')
    s = s.slice(index, s.length).split('')
    
    while( s.indexOf('0') > -1){
        let post =  s.indexOf('0')
        s[post] =  r.pop() 
    }
    
    
    let pattern = /[A-Z]/
    let pattern_lower = /[a-z]/
    
    
     for (let i=s.length-1; i<=0 ; i--){
        if(isNaN(s[i])){
            if((i+1) < s.length && pattern.test(s[i]) && pattern_lower.test(s[i-1])){
                let temp = s[i]
                s[i] = s[i-1]
                s[i-1] = temp
                i -= 1
            }
        }
    }
    
    return s.join('')

}
