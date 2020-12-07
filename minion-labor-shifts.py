def solution(data,n):
    if n == 0:
        return []
    minion_dict = {}

    
    for minion_id in data:
        if minion_id in minion_dict:
            minion_dict[minion_id] += 1
        else:
            minion_dict[minion_id] = 1

    fixed_data = []
    for minion_id in data:
        if not (minion_dict[minion_id] > n):
            fixed_data.append(minion_id)

    return fixed_data
