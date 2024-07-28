import random
from openai_adapter import OpenAIAdapter
class TalkSystem:
    def __init__(self):
        self.openai_adapter = OpenAIAdapter()

    def talk_monologue(self):
        # 話すテーマをランダムに決定
        theme_mode = ["思い出", "童話"]
        theme = random.choice(theme_mode)
        if theme == "思い出":
            talk = self._generate_memory_talk()
        elif theme == "童話":
            talk = self._generate_fairy_tale()
        return talk

    def _generate_memory_topic(self)->str:
       time_periods = ["幼少期", "学生時代", "最近", "小学校", "中学校", "高校"]
       locations = [ "実家", "祖父母の家", "公園", "図書館", "海", "山"]
       activities = ["勉強", "運動", "趣味", "友達との交流", "家族との時間", "旅行", "行事", "アルバイト","季節の変わり目", "記念日", "休日"]
       emotions = ["楽しい", "悲しい", "懐かしい", "驚いた", "緊張した", "安心した", "困惑した", "感動した"]
       location = random.choice(locations)
       activity = random.choice(activities)
       emotion = random.choice(emotions)
       time_period = random.choice(time_periods)

       return f"{time_period}の{location}での{activity}に関する{emotion}思い出"

    def _generate_memory_talk(self)->str:
        topic = self._generate_memory_topic()
        topic_talk_1_shot = {
            "topic":"小学校の公園での趣味に関する驚いた思い出",
            "talk":"あ、そうだ唐突に思い出したんだけどね。私って夜の散歩好きなんだ～って前に話したと思うんだけど、小学校の時から好きだったの！でも危ないから～ってお母さんに言われたから一緒に真夜中に公園まで散歩したことがあって、その時お母さんに「こういう時はお化けが出るんだよ」って言われて怖くなっちゃって、早く帰ろうって行った瞬間にセミがいきなり飛び出してきてさ！そういうことがあったから夜に散歩したとき毎回セミがいないか緊張するんだよね。いきなり思い出したから話しちゃった。"
        }
        prompt = f"以下のような思い出トークをしてください。[思い出トーク例]\n{topic_talk_1_shot['topic']}:{topic_talk_1_shot['talk']}\n[今回の思い出トーク]\n{topic}:"
        response = self.openai_adapter.create_chat(prompt)
        print(response)
        return response

    def _generate_story_elements(self):
        themes = ["冒険", "友情", "成長", "愛", "勇気", "知恵"]
        characters = ["少年", "少女", "動物", "魔法使い", "王子", "姫", "妖精"]
        settings = ["森", "城", "村", "山", "海", "空"]
        plot_elements = ["魔法のアイテム", "試練", "助けてくれる仲間", "悪役", "大きな決断", "予想外の展開","裏切り","悲しみ","バッドエンド"]

        return {
            "theme": random.choice(themes),
            "main_character": random.choice(characters),
            "setting": random.choice(settings),
            "plot_elements": random.sample(plot_elements, 3)
        }

    def _generate_fairy_tale(self)->str:
        elements = self._generate_story_elements()
        prompt = f"""
            以下の要素を使って、短い童話を作ってください：
            テーマ: {elements['theme']}
            主人公: {elements['main_character']}
            舞台設定: {elements['setting']}
            プロット要素: {', '.join(elements['plot_elements'])}

            童話は300字程度で、キャラクターの個性を反映させてください。
        """
        response = self.openai_adapter.create_chat(prompt)
        print(response)
        return response

if __name__ == "__main__":
    talk_system = TalkSystem()
    talk_system.talk_monologue()


