function solution(n) {
    let answer = 0;
    let cnt = 0;
    
    while (cnt < n) {
        answer++;
        
        if (answer % 3 === 0 || String(answer).includes('3')) {
            continue;
        }
        
        cnt++;
    }
    
    return answer;
}