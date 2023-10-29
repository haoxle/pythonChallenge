def permutations(letters):
    if len(letters) == 1:
        return [letters]

    perms = permutations(letters[1:])
    char = letters[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result


def permute(nums):
    results = []
    visited = set()

    def backtrack(currentPath):
        if len(currentPath) == len(nums):
            results.append(currentPath)
        
        for index in range(len(nums)):
            if index not in visited:
                visited.add(index)
                print(visited)
                # print(currentPath, 'and',[nums[index]] )
                backtrack(currentPath + [nums[index]])
                visited.remove(index)
    

    backtrack([])
    return results


print(permute([1,2,3]))
