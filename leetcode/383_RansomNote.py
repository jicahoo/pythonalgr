class SolutionFirst(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ret = True
        sorted_randomNote = sorted(ransomNote)
        sorted_magazine = sorted(magazine)
        n = len(sorted_randomNote)
        m = len(sorted_magazine)
        last_find_start_point = 0
        for i in xrange(n):
            if i > m-1:
                ret = False
                break
            else:
                letter_in_ransom = sorted_randomNote[i]
                idx = self.find(sorted_magazine, last_find_start_point, letter_in_ransom)
                if idx is None:
                    ret = False
                    break
                else:
                    last_find_start_point = idx+1
        return ret

    def find(self, my_list, start, element):
        n = len(my_list)
        for i in xrange(start, n):
            e = my_list[i]
            if element == e:
                return i
        return None

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Just follow the most natural way: think about if how will you do it by manually,
        # how many "a" I need, how many "b" I need, then count are there enough letters in magazine.
        # Time complexity: m+n+n. Space complexity: 26*size( store "letter":[count_a,count_b] )
        dict_ransom = {}
        for letter in ransomNote:
            if letter in dict_ransom:
                dict_ransom[letter][0] += 1
            else:
                dict_ransom[letter] = [1, 0]
        for letter in magazine:
            if letter in dict_ransom:
                dict_ransom[letter][1] += 1
        for key in dict_ransom:
            item = dict_ransom[key]
            if item[0] > item[1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ransom = "a"
    mag = "b"
    assert not s.canConstruct(ransom, mag)

    ransom = "a"
    mag = "ab"
    assert s.canConstruct(ransom, mag)

    ransom = "aaa"
    mag = "abaa"
    assert s.canConstruct(ransom, mag)

    ransom = "a"
    mag = ""
    assert not s.canConstruct(ransom, mag)

    ransom = "zx"
    mag = "aaaxaeeezee"
    assert s.canConstruct(ransom, mag)

    ransom = "aa"
    mag = "ab"
    assert not s.canConstruct(ransom, mag)

    ransom = "fihjjjjei"
    mag =  "hjibagacbhadfaefdjaeaebgi"
    print sorted(ransom)
    print sorted(mag)
    assert not s.canConstruct(ransom, mag)