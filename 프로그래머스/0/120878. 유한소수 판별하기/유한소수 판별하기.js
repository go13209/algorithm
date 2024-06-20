function solution(a, b) {
    let cnt = 2;
    
    while (cnt <= a) {
        if (a % cnt === 0 && b % cnt === 0) {
            a /= cnt;
            b /= cnt;
            cnt = 2;
            continue;
        }
        cnt++;
    }
    
    while (b % 2 === 0) {
        b /= 2;
    }
    while (b % 5 === 0) {
        b /= 5;
    }
    
    return b === 1 ? 1 : 2;
}