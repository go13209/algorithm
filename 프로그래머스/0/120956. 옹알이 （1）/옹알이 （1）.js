function solution(babbling) {
    var answer = 0;
    const possibleWords = ["aya", "ye", "woo", "ma"];
    
    for (const babble of babbling) {
        let i = 0;
        let isValid = true;
        let lastWord = ""; // 마지막으로 사용한 단어를 저장하는 변수
        
        while (i < babble.length) {
            let found = false;
            for (const word of possibleWords) {
                if (babble.slice(i, i + word.length) === word) {
                    if (lastWord === word) { // 이전에 사용된 단어와 같은 경우
                        isValid = false;
                        break;
                    }
                    i += word.length;
                    lastWord = word; // 현재 단어를 lastWord로 업데이트
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
