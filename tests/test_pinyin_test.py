# -*- coding: utf-8 -*-
import os
import time

from pypinyin import lazy_pinyin, Style

from pypinyin_g2pw import G2PWPinyin

model_dir = os.getenv('MODEL_DIR', 'G2PWModel/')
model_source = os.getenv('MODEL_SOURCE', 'bert-base-chinese/')

# 测试包括：
# 网络用语、轻音。数字与特殊字符、古汉语诗词。多音字、儿化音。方言词汇和口语表达。

def test_lazy_pinyin():
    han = ('小明最近迷上了‘吃鸡’，每天晚上都得熬夜到很晚。他常说：‘这局我要稳赢，绝不能翻车！他的朋友们有时会打趣儿说他是夜猫子，他自己则自称是电竞选手。'
    '最近网上流行起了‘云养猫’，就是在网上看别人分享的猫咪视频。每天下班后，我都会点开几个猫咪视频，看着那些毛茸茸的小家伙们做着各种憨态可掬的动作，感觉萌萌哒，于是压力减小了很多。'
    '亲爱的听众朋友们，大家好！欢迎来到我们的节目《文化之旅》，我是主持人小李。今天是2024年12月8日星期日，农历十一月廿六，今天我们要一起探索唐诗宋词中的情感表达。比如李白的‘朝辞白帝彩云间’，杜甫的‘国破山河在’，这些诗句不仅体现了诗人个人的情感世界，也反映了当时的社会风貌。今天的直播将于北京时间晚上7点准时开始，持续大约两个小时。如果您有任何问题或想法，请随时通过微博@文化之旅官方账号与我们互动交流。期待您的参与和支持！'
    '我参加了这次会议，会上介绍了一种珍贵的人参，这种人参对健康有着特殊的价值。走出会议室后，我们一行人参观了植物园，那里的树木参差不齐地排列着，形成了一道独特的风景线。'
    '她有一头美丽的黑发，显得格外迷人。今天，她发了一封邮件给我，邮件中提到，因为最近的努力工作得到一些奖赏。邮件最后叮嘱我，经济发展得很迅速，各行各业都在快速变化，得早点儿做准备。'
    '你食咗饭未呀？这个串串香简直了，又辣又麻，巴适得板！'
    '侬今朝去哪能浪？我今儿个要去趟超市，买点日用品。'
    )
    g2pw = G2PWPinyin(model_dir=model_dir, model_source=model_source)

    now = time.time()
    p1 = lazy_pinyin(han, style=Style.TONE3)
    t1 = time.time() - now

    now = time.time()
    p2 = g2pw.lazy_pinyin(han, style=Style.TONE3)
    t2 = time.time() - now

    print('han: \n{}'.format(han))

    print('pypinyin {}s: \n{}'.format(t1, ' '.join(p1)))

    print('pypinyin_g2pw {}s: \n{}'.format(t2, ' '.join(p2)))


if __name__ == '__main__':
    test_lazy_pinyin()
