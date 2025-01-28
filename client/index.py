import keyboard
import requests
import time

# 定义请求的接口 URL
API_BASE_URL = "http://192.168.2.50:5000"  # 这里替换为实际的 API 基础 URL

# 定义控制方法，通过 HTTP 请求调用接口
def move_forward():
    response = requests.get(f"{API_BASE_URL}/move/up")
    print("Moved forward. Response:", response.text)

def move_backward():
    response = requests.get(f"{API_BASE_URL}/move/down")
    print("Moved backward. Response:", response.text)

def turn_left():
    response = requests.get(f"{API_BASE_URL}/move/left")
    print("Turned left. Response:", response.text)

def turn_right():
    response = requests.get(f"{API_BASE_URL}/move/right")
    print("Turned right. Response:", response.text)

def stop():
    response = requests.get(f"{API_BASE_URL}/move/stop")
    print("Stopped. Response:", response.text)

# 创建按键映射
key_map = {
    'up': move_forward,
    'down': move_backward,
    'left': turn_left,
    'right': turn_right,
}

# 用于记录按键状态，防止重复触发
key_state = {
    'up': False,
    'down': False,
    'left': False,
    'right': False,
}

# 监听按键事件并发送请求
def listen_keys():
    while True:
        event = keyboard.read_event()

        # 按键按下事件
        if event.event_type == keyboard.KEY_DOWN:
            if event.name in key_map and not key_state[event.name]:
                print(f"Key {event.name} pressed")
                key_map[event.name]()  # 调用对应的移动方法
                key_state[event.name] = True  # 更新按键状态为按下

        # 按键抬起事件
        elif event.event_type == keyboard.KEY_UP:
            time.sleep(0.2)
            print('target')
            stop()  # 任何按键抬起时停止
            key_state[event.name] = False  # 更新按键状态为抬起
            print(f"Key {event.name} released")

        # time.sleep(0.1)  # 稍微延时，避免CPU过高

# 启动监听
if __name__ == "__main__":
    print("Starting key listener...")
    listen_keys()
