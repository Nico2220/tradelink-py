class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def searchWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfWord
    

    def searchConcatenations(self, query):
        result = []
        for i in range(1, len(query)):
            prefix = query[:i]
            suffix = query[i:]

            if self.searchWord(prefix) and self.searchWord(suffix):
                result.append(f"{prefix}:{suffix}")

        return result


# O(N*L * KS^2) time | O(N * L) space
# N is the number of words in the vocabulary 
# L -average length of a word
# K- number of queries
# S- Average length of query string

def findConcatanations(N, vocabulary, K, queries):
    trie = Trie()

    for word in vocabulary:
        trie.insert(word)

    results = []
    for query in queries:
        concatOptions = trie.searchConcatenations(query)
        results.append((len(concatOptions), concatOptions))

    return results



N = 5
vocabulary = ["abcd", "cdef", "ab", "ef", "ffff"]
K = 2
queries = ["abcdef", "ffff"]

result = findConcatanations(N, vocabulary, K, queries)


for count, options in result:
    print(count)
    for option in options:
        print(option)