function solution(sides) {
    let answer = 0;

    const long = Math.max(...sides);
    const short = Math.min(...sides);
    
    for (let i = long - short + 1; i < long + short; i++) {
        answer += 1;
    }
    
    return answer;
}
