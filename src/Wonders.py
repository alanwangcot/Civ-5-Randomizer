import random
import secrets

class Wonders():
    EARLY_WONDERS_LIST = ["兵马俑",
    "祭司神殿",
    "巴特农神庙",
    "佩特拉古城",
    "长城",
    "青铜巨像"]
    WONDERS_LIST = [
    "兵马俑",
    "祭司神殿",
    "巴特农神庙",
    "佩特拉古城",
    "长城",
    "青铜巨像",

    "圣索菲亚大教堂",
    "波罗浮屠",
    "奇琴伊察城",
    "马丘比丘",
    "吴哥窟",
    "阿兰布拉宫",
    "圣母院",
    "比萨斜塔",
    "环球剧场",
    "姬路城",
    "大报恩寺",
    "泰姬玛哈陵",
    "德里红堡",

    "勃兰登堡门",
    "新天鹅堡",
    "埃菲尔铁塔",
    "百老汇",
    "耶稣巨像"
    ]

    def __init__(self):
        pass

    def randomize(self, num_players:int) -> list:
        seed = secrets.randbits(64)
        random.seed(seed)
        print("Randomizing with seed: ", seed)
        if (num_players * 3 > len(self.WONDERS_LIST)):
            return None
        wonders = self.WONDERS_LIST.copy()
        ret = []
        for i in range(num_players):
            
            rand_wonders = random.sample(wonders, 3)
            # if more than 1 in rand_wonders is in EARLY_WONDERS_LIST, reroll
            count = 0
            while len([wonder for wonder in rand_wonders if wonder in self.EARLY_WONDERS_LIST]) > 1:
                count += 1
                if (count >= 100):
                    return self.randomize(num_players)
                rand_wonders = random.sample(wonders, 3)
            ret.append(random.sample(wonders, 3))
            wonders = [wonder for wonder in wonders if wonder not in ret[i]]
        return ret