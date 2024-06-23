from collections import deque, defaultdict
class Solution:
    """
    I think its n ^ m reason is imagine you have m synonyms ["happy","joy", "cheerful"] and n string in sentence. worst case your sentence can be : happy, happy, happy, happy... so you have _ _ _ _ ... you need to fill this four blanks and each blank has 3 possibilities. 3*3*3*3 = so total (3^4) = n ^m .
Since he is using set to track the ans were every insert will be lgn then this will be in total (n^m) lg (n^m) .. Please correct me if I am wrong.


worst case scenario: O(n^m) where m is the number of words in the text, and m is the average number of synonyms for each word.
    """
    def generateSentencesBFS(self, synonyms: list[list[str]], text: str) -> list[str]:
        graph = defaultdict(list)
        for k,v in synonyms:
            graph[k].append(v)
            graph[v].append(k)
        
        queue = deque([text])
        visited = set([text])
        while queue:
            cur_t = queue.popleft()
            cur_words = cur_t.split(" ")

            for i, cur_w in enumerate(cur_words):
                if cur_w in graph:
                    for nb in graph[cur_w]:
                        new_t = " ".join(cur_words[:i] + [nb] + cur_words[i+1:])
                        if new_t not in visited:
                            queue.append(new_t)
                            visited.add(new_t)
        
        return sorted(list(visited))


    # O(number of different syn senteces * number of words in senteces)
    # For all these syn sentences, each word is a node
    # Need to go through all of the words
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        synonyms_map = {}
        for si, ti in synonyms:
            if si not in synonyms_map:
                synonyms_map[si] = []
            if ti not in synonyms_map:
                synonyms_map[ti] = []
            synonyms_map[si].append(ti)
            synonyms_map[ti].append(si)
        
        words = text.split(' ')
        n = len(words)
        res = []
        def traverse_all_words(i: int, path: list[str]):
            if i == n:
                res.append(list(path))
                return
            
            if words[i] not in synonyms_map:
                path.append(words[i])
                traverse_all_words(i + 1, path)
                path.pop()
            else:
                visited = set()
                find_all_synonyms(synonyms_map, words[i], visited)
                all_synonyms = list(visited)
                for w in all_synonyms:
                    path.append(w)
                    traverse_all_words(i + 1, path)
                    path.pop()
        
        def find_all_synonyms(synonyms_map: dict, cur: str, visited: set):
            visited.add(cur)
            for nb in synonyms_map[cur]:
                if nb in synonyms_map and nb not in visited:
                    find_all_synonyms(synonyms_map, nb, visited)


        traverse_all_words(0, [])
        all_syn_sentence = [" ".join(arr) for arr in res]
        all_syn_sentence.sort()
        return all_syn_sentence