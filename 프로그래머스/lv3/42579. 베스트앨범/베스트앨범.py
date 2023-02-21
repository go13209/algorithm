def solution(genres, plays):
    answer = []
    dict = {}
    count_dict = {}

    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [(plays[i], i)]
            count_dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += [(plays[i], i)]
            count_dict[genres[i]] += plays[i]

    for k, v in sorted(count_dict.items(), key = lambda x: x[1], reverse = True):
        if len(dict[k]) >= 2:
            for j in range(2):
                answer.append(sorted(dict[k], key = lambda x: x[0], reverse = True)[j][1])
        else:
            answer.append(dict[k][0][1])
    
    return answer
