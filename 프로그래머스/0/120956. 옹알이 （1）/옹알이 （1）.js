function solution(babbling) {
    var answer = 0;
    const possibleWords = ["aya", "ye", "woo", "ma"]
    
    for (const babble of babbling) {
        let i = 0;
        let isValid = true;
        
        while (i < babble.length) {
            let found = false;
            for (const word of possibleWords) {
                if (babble.slice(i, i + word.length) === word) {
                    i += word.length;
                    found = true;
                    break;
                }
            }
            if (!found) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            answer += 1;
        }
    }
    return answer;
}