def solution(nums):
    distinct = set(nums)
    answer = len(nums) // 2 if len(distinct) >= len(nums) // 2 else len(distinct)

    return answer