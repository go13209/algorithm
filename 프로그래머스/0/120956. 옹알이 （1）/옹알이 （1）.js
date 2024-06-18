function solution(babbling) {
    var answer = 0;
    const possibleWords = ["aya", "ye", "woo", "ma"];
    
    for (const babble of babbling) {
        let i = 0;
        let isValid = true;
        let usedWords = new Set(); // 사용된 단어를 저장하는 집합
        
        while (i < babble.length) {
            let found = false;
            for (const word of possibleWords) {
                if (babble.slice(i, i + word.length) === word) {
                    if (usedWords.has(word)) { // 이전에 사용된 단어와 같은 경우
                        isValid = false;
                        break;
                    }
                    i += word.length;
                    usedWords.add(word); // 현재 단어를 사용된 단어로 추가
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
