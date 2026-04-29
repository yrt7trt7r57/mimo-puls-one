
import random
import pandas as pd
from datetime import datetime, timedelta

accounts = [
    {"name": "情感号01", "type": "情感"},
    {"name": "创业号01", "type": "创业"},
    {"name": "搞笑号01", "type": "搞笑"},
    {"name": "成长号01", "type": "成长"},
]

hot_topics = [
    "普通人如何翻身","成年人最大的清醒","为什么你总是赚不到钱",
    "穷人思维的3个陷阱","让女生上头的细节","为什么年轻人越来越焦虑",
    "真正厉害的人都很安静","搞钱才是成年人顶级浪漫"
]

viral_hooks = [
    "99%的人都没意识到","越早知道越好","这是普通人逆袭最快的方法",
    "很多人30岁才明白","别再傻傻努力了","看懂的人已经开始行动"
]

class ShortVideoMatrixAgent:
    def __init__(self):
        self.contents = []
        self.report = []

    def fetch_hot_topics(self):
        return random.sample(hot_topics, 5)

    def generate_title(self, topic):
        return f"{random.choice(viral_hooks)}：{topic}"

    def generate_script(self, topic):
        return f"""开头3秒：你知道吗？{topic}

中段：很多人一直没发现这个问题，所以每天都在低质量重复努力。

结尾：如果你现在才明白，还不算晚。关注我。"""

    def create_content(self):
        for topic in self.fetch_hot_topics():
            self.contents.append({
                "topic": topic,
                "title": self.generate_title(topic),
                "script": self.generate_script(topic)
            })

    def distribute(self):
        now = datetime.now()
        for i, c in enumerate(self.contents):
            acc = accounts[i % len(accounts)]
            self.report.append({
                "账号": acc["name"],
                "赛道": acc["type"],
                "发布时间": (now + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M"),
                "标题": c["title"],
                "播放量": random.randint(5000,500000),
                "点赞": random.randint(500,30000),
                "评论": random.randint(50,5000),
                "转发": random.randint(20,3000),
            })

    def export(self):
        df = pd.DataFrame(self.report)
        df.to_csv("短视频矩阵运营报表.csv", index=False, encoding="utf-8-sig")
        print(df)

    def run(self):
        self.create_content()
        self.distribute()
        self.export()

if __name__ == "__main__":
    ShortVideoMatrixAgent().run()
