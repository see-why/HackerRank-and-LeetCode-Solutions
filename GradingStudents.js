//Hackerank challenge...https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
function gradingStudents(grades) {
    // Write your code here
    const newArray = grades.map((item) => {
        if(item  >= 38 ){
            const quotient = Math.floor(item / 5);   
            const nextMultiple = (quotient + 1) * 5;
            item = (nextMultiple - item) < 3 ? nextMultiple : item;
        } 
        return item   
    })
    
    return newArray
}
