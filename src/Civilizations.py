import random
import secrets

class Civilizations():
    CHINA = '中国'
    BABYLON = '巴比伦'
    BRAZIL = '巴西'
    JAPAN = '日本'
    HUNS = '匈'
    INCA = '印加'
    INDONESIA = '印尼'
    INDIA = '印度'
    ETHIOPIA = '依索比亚'
    SPAIN = '西班牙'
    GREECE = '希腊'
    SHOSHONE = '肖松尼'
    ASSYRIA = '亚述'
    IROQUOIS = '易洛魁'
    PERSIA = '波斯'
    POLAND = '波兰'
    FRANCE = '法国'
    ARABIA = '阿拉伯'
    AZTEC = '阿兹特克'
    RUSSIA = '俄罗斯'
    VENICE = '威尼斯'
    BYZANTIUM = '拜占庭'
    POLYNESIA = '波利尼西亚'
    AMERICA = '美国'
    ENGLAND = '英格兰'
    CARTHAGE = '迦太基'
    EGYPT = '埃及'
    SONGHAI = '桑海'
    ZULU = '祖鲁'
    MAYA = '玛雅'
    NETHERLANDS = '荷兰'
    CELTS = '凯尔特'
    KOREA = '朝鲜'
    OTTOMAN = '奥斯曼'
    AUSTRIA = '奥地利'
    SWEDEN = '瑞典'
    PORTUGAL = '葡萄牙'
    MONGOLIA = '蒙古'
    GERMANY = '德国'
    MORROCO = '摩洛哥'
    SIAM = '暹罗'
    DENMARK = '丹麦'
    ROME = '罗马'
    CIV_LIST = [
    '威尼斯', '匈', '肖松尼', '西班牙', '巴比伦', '中国', '巴西', '日本', '印加', '印尼', '印度', 
    '希腊', '亚述', '易洛魁', '波斯', '波兰', '法国', '阿拉伯', '阿兹特克', '俄罗斯', '依索比亚',
    '拜占庭', '波利尼西亚', '美国', '英格兰', '迦太基', '埃及', '桑海', '祖鲁', '玛雅',
    '荷兰', '凯尔特', '朝鲜', '奥斯曼', '奥地利', '瑞典', '葡萄牙', '蒙古', '德国', '摩洛哥',
    '暹罗', '丹麦', '罗马']

    def __init__(self, banned_civs=None):
        if banned_civs is not None:
            self.CIV_LIST = [civ for civ in self.CIV_LIST if civ not in banned_civs]

    def randomize(self, num_players:int, num_choices:int) -> list:
        seed = secrets.randbits(64)
        random.seed(seed)
        print("Randomizing with seed: ", seed)
        if num_players * num_choices > len(self.CIV_LIST):
            return None
        civs = self.CIV_LIST.copy()
        ret = []
        for i in range(num_players):
            ret.append(random.sample(civs, num_choices))
            civs = [civ for civ in civs if civ not in ret[i]]
        return ret
    
if __name__ == "__main__":
    civs = Civilizations()
    print(civs.randomize(3, 3))