# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 解释：

# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
# 示例 2:

# 输入: strs = [""]

# 输出: [[""]]

# 示例 3:

# 输入: strs = ["a"]

# 输出: [["a"]]

 

# 提示：

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母

def groupAnagrams(strs):
    hash_map = {}
        # {
        #     "aet": ["eat", "tea", "ate"],
        #     "ant": ["tan", "nat"]
        # }

    for s in strs:
        #字符排序后拼接为字符串，作为hash-key
        #sorted()是python内置函数，会把字符串s变成单独字符，按升序排列，返回字符列表
        #‘’。join是将字符合在一起，然后去对比
        key = ''.join(sorted(s))
        #key = ''.join(sorted(s.reverse(True)))反转成倒序排列
        
        #若相同，则放进同一个key
        if key in hash_map:
            #字典取值语法：`字典[索引key]` → 拿到对应的 value
            hash_map[key].append(s)
        else:
            #字符串s,[s]是列表，列表可以。append（），后续可以加不同词
            #把这个 key 加入字典，并且给它绑定上值 `[s]`
            hash_map[key] = [s]
    #返回values()，即hash_map的value值，返回的是一个list
    return list(hash_map.values())
