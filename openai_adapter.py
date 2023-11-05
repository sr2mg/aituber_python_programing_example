import openai
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

class OpenAIAdapter:
    SAVE_PREVIOUS_CHAT_NUM = 5
    def __init__(self):
        # system_promptはsystem_prompt.txtから読み込む
        with open("system_prompt.txt","r",encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.chat_log = []
        pass
    def _create_message(self,role,message):
        return {
            "role":role,
            "content":message
        }

    def create_chat(self,question):
        # 過去のチャットログを追加する
        messages = self._get_messages()
        user_message = self._create_message("user",question)
        messages.append(user_message)

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        answer = res["choices"][0]["message"]["content"]
        self._update_messages(question,answer)

        return answer
    
    def _get_messages(self):
        system_message = self._create_message("system",self.system_prompt)
        messages = [system_message]
        for chat in self.chat_log:
            messages.append(self._create_message("user",chat["question"]))
            messages.append(self._create_message("assistant",chat["answer"]))
        return messages
    
    def _update_messages(self,question,answer):
        # チャットログを保存する
        self.chat_log.append({
            "question":question,
            "answer":answer
        })
        # チャットログがSAVE_PREVIOUS_CHAT_NUMを超えたら古いログを削除する
        if len(self.chat_log)>self.SAVE_PREVIOUS_CHAT_NUM:
            self.chat_log.pop(0)
        return True

    

if __name__ == "__main__":
    adapter = OpenAIAdapter()
    while True:
        question = input("質問を入力してください:")
        response_text = adapter.create_chat(question)
        print(response_text)
        print(adapter.chat_log)