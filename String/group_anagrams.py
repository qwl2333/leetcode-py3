
'''
主要熟悉两个
1. 如何sort a str ''.join(sorted(string))
2. 如何把一个 str 变成一个 array
            key = [0] * 26
            for char in string:
                key[ord(char)-ord('a')] += 1 # ord 可以得到unicode
3. 如何把一个list/array变成可以存放在set或者dict里面的key，因为直接放array作为key 会得到 TypeError: unhashable type: list
    因为 list 不是immutable的，作为key必须是immutable，比如str, int, float, tuple
    所以必须把list变成tuple
    strs_key = tuple(key)
'''
class Solution:
    # time O(mlogm * n) m - avg size of str, n is length of list
    # space O(n * m) - for res and strs_table
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())
    
    # time could be optimized to O(26 * n)
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        strs_table = {}

        for string in strs:
            key = [0] * 26
    
            for char in string:
                key[ord(char)-ord('a')] += 1 
            strs_key = tuple(key)

            if strs_key not in strs_table:
                    strs_table[strs_key] = []

            strs_table[strs_key].append(string)

        return list(strs_table.values())