def solution(nums):
    nums_set = set(nums)
    return min(len(nums)//2, len(nums_set))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# Java ver
# import java.util.Arrays;
# import java.util.List;
# import java.util.stream.Collectors;

# class Solution {
#     public int solution(int[] nums) {
#         List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());
#         return (int) Math.min(list.parallelStream().distinct().count(), nums.length/2);
#     }
# }