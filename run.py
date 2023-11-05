import time
from aituber_system import AITuberSystem
import traceback
aituber_system = AITuberSystem()
while True:
    try:
        aituber_system.talk_with_comment()
        time.sleep(5)
    except Exception as e:
        print("エラーが発生しました")
        print(traceback.format_exc())
        print(e)
        exit(200)