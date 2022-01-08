# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

# Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

# Sample input:

# user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
# user2 = ["a", "/one", "/two"]
# user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
# user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
# user5 = ["a"]
# user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

# Sample output:

# findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
# findContiguousHistory(user0, user2) => [] (empty)
# findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# findContiguousHistory(user2, user1) => ["a"]
# findContiguousHistory(user5, user2) => ["a"]
# findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

# n: length of the first user's browsing history
# m: length of the second user's browsing history
user0 = ["/start", "/green", "/blue", "/pink",
         "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber",
         "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan",
         "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink", "/orange", "/six", "/plum",
         "/seven", "/tan", "/red", "/amber"]


def commonUrlI(user1, user2):
    i = 0
    ans = []
    mn = min(len(user1), len(user2))
    while (i < mn) and (user1[i] == user2[i]):
        ans.append(user1[i])
        i += 1
    return ans


def commonUrl(user1, user2):
    if len(user1) == 0 or len(user2) == 0:
        return []
    if user1[0] != user2[0]:
        ans1 = commonUrl(user1[1:], user2)
        ans2 = commonUrl(user1, user2[1:])
        if len(ans1) >= len(ans2):
            return ans1
        else:
            return ans2
    else:
        ans3 = []
        ans1 = commonUrl(user1[1:], user2)
        ans2 = commonUrl(user1, user2[1:])
        ans3.append(user1[0])
        ans3.extend(commonUrlI(user1[1:], user2[1:]))
        if len(ans3) >= max(len(ans1), len(ans2)):
            return ans3
        elif len(ans1) >= len(ans2):
            return ans1
        else:
            return ans2


print(commonUrl(user0, user1))
