import sounddevice as sd
from typing import TypedDict
class PlaySound:
    def __init__(self, output_device_name= "CABLE Input") -> None:
        # 指定された出力デバイス名に基づいてデバイスIDを取得
        output_device_id = self._search_output_device_id(output_device_name)
        # 入力デバイスIDは使用しないため、デフォルトの0を設定
        input_device_id = 0
        # デフォルトのデバイス設定を更新
        sd.default.device = [input_device_id, output_device_id]

    def _search_output_device_id(self, output_device_name, output_device_host_api=0) -> int:
        # 利用可能なデバイスの情報を取得
        devices = sd.query_devices()
        output_device_id = None
        # 指定された出力デバイス名とホストAPIに合致するデバイスIDを検索
        for device in devices:
            is_output_device_name = output_device_name in device["name"]
            is_output_device_host_api = device["hostapi"] == output_device_host_api
            if is_output_device_name and is_output_device_host_api:
                output_device_id = device["index"]
                break

        # 合致するデバイスが見つからなかった場合の処理
        if output_device_id is None:
            print("output_deviceが見つかりませんでした")
            exit()
        return output_device_id
    def play_sound(self, data, rate) -> bool:
        # 音声データを再生
        sd.play(data, rate)
        # 再生が完了するまで待機
        sd.wait()
        return True