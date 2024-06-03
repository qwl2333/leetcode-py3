import math
'''
给一串字符串代表music playlist，判断是随机播放还是列表播放
注意列表播放 一轮轮完后下次的顺序可能不同
"ABCD CABD BCD‍‍‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌‌A" 这是列表播放
"ABACBA" 这是随机播放

1.两个methods的返回值都是boolean
2. 第一个method检测input是否有可能是random mode生成的
3. 第二个method检测input是否有可能是shuffle mode生成的
解题思路：
method1: always true，因为没有反例
method2: 没有duplicate就是true
follow-up：如果input是stream，怎么定义这两个method？
解题思路：和面试官clarify清楚，每个人可能解法不同。我这里用的是类似LFU来检测fr‍‍‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌‌equency，确定frequency在valid范围内

'''
class PlayListChecker:
    def is_shuffle(self, play_list: list[str]) -> bool:
        played_freq = {}
        i = 0
        n = len(play_list)
        while i < n and play_list[i] not in played_freq:
            played_freq[play_list[i]] = 1
            i += 1
        
        if i == n:
            return True

        num_of_uniq_songs = len(played_freq)
        # print(num_of_uniq_songs)

        while i < n:
            cur_count = math.ceil((i + 1) / num_of_uniq_songs)
            played_freq[play_list[i]] = played_freq.get(play_list[i], 0) + 1
            if played_freq[play_list[i]] != cur_count:
                return False
            i += 1
        
        return True

    def is_random(self, play_list: list[str]) -> bool:
        return True
    
    def __init__(self):
        self.num_of_songs = 3

        self.played_freq_shuffle = {}
        self.biggest_freq_shuffle = 0

        self.played_freq_random = {}
        self.count_random = 0
        self.threshold = 1000

    def is_shuffle_stream(self, song: str) -> bool:
        self.played_freq_shuffle[song] = self.played_freq_shuffle.get(song, 0) + 1
        self.biggest_freq = max(self.biggest_freq, self.played_freq_shuffle[song])
        if self.played_freq_shuffle[song] != self.biggest_freq:
            del self.played_freq_shuffle[song]
            return False
        else:
            return True
    
    def is_random_stream(self, song: str) -> bool:
        self.played_freq_random[song] = self.played_freq_random.get(song, 0) + 1
        self.count_random += 1
        if self.count_random > self.threshold:
            share = self.played_freq_random[song] / self.count_random
            if share > 1 / self.num_of_songs * 2:
                return False
            else:
                return True



s = PlayListChecker()
print(s.is_shuffle(list('abcasc')))