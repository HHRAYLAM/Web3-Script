import json
import time
import random
import pyautogui

# 读取 JSON 配置文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 获取屏幕分辨率的坐标配置
resolution = "1920"
sub_resolution = "1080"
coordinates = config["elementCursors"][resolution][sub_resolution]
step_wait_time = config["stepWaitTime"]
repeat_times = config["repeatTimes"]
verify = config["verify"]

def move_mouse_to_coordinates(x, y, pause_duration=1):
    pyautogui.moveTo(x, y, duration=1)
    time.sleep(pause_duration)

def click_element_by_coordinates(x, y, pause_duration=1):
    pyautogui.click(x, y)
    time.sleep(pause_duration)

def perform_operations():
    # Step 1: Move and click on wallet
    move_mouse_to_coordinates(coordinates["wallet"]["x"], coordinates["wallet"]["y"])
    click_element_by_coordinates(coordinates["wallet"]["x"], coordinates["wallet"]["y"])
    time.sleep(step_wait_time["openWallet"] / 1000)

    # Step 2: Move and click on sendBtn1
    move_mouse_to_coordinates(coordinates["sendBtn1"]["x"], coordinates["sendBtn1"]["y"])
    click_element_by_coordinates(coordinates["sendBtn1"]["x"], coordinates["sendBtn1"]["y"])
    time.sleep(step_wait_time["send"] / 1000)

    # Step 3: Move and click on addressBook
    move_mouse_to_coordinates(coordinates["addressBook"]["x"], coordinates["addressBook"]["y"])
    click_element_by_coordinates(coordinates["addressBook"]["x"], coordinates["addressBook"]["y"])
    time.sleep(step_wait_time["addressBook"] / 1000)

    # Step 4: Move and click on firstAddress
    move_mouse_to_coordinates(coordinates["firstAddress"]["x"], coordinates["firstAddress"]["y"])
    click_element_by_coordinates(coordinates["firstAddress"]["x"], coordinates["firstAddress"]["y"])
    time.sleep(step_wait_time["selectAddress"] / 1000)

    # Step 5: Move and input amount
    move_mouse_to_coordinates(coordinates["amount"]["x"], coordinates["amount"]["y"])
    click_element_by_coordinates(coordinates["amount"]["x"], coordinates["amount"]["y"])
    random_amount = round(random.uniform(0.0001, 0.0002), 7)  # Generate a random amount
    pyautogui.typewrite(str(random_amount), interval=0.1)
    time.sleep(step_wait_time["amount"] / 1000)

    # Step 6: Move and click on sendBtn2
    move_mouse_to_coordinates(coordinates["sendBtn2"]["x"], coordinates["sendBtn2"]["y"])
    click_element_by_coordinates(coordinates["sendBtn2"]["x"], coordinates["sendBtn2"]["y"])
    time.sleep(step_wait_time["send2"] / 1000)

    # Step 7: Move and click on sendBtn3
    move_mouse_to_coordinates ( coordinates [ "sendBtn3" ] [ "x" ] , coordinates [ "sendBtn3" ] [ "y" ] )
    click_element_by_coordinates ( coordinates [ "sendBtn3" ] [ "x" ] , coordinates [ "sendBtn3" ] [ "y" ] )
    time.sleep ( step_wait_time [ "send3" ] / 1000 )

    # Optional Step 8: Verify (if applicable)
    if verify:
        move_mouse_to_coordinates(coordinates["verifyBtn"]["x"], coordinates["verifyBtn"]["y"])
        click_element_by_coordinates(coordinates["verifyBtn"]["x"], coordinates["verifyBtn"]["y"])
        time.sleep(step_wait_time["verify"] / 1000)

    # Step 9: Move and click on sign
    move_mouse_to_coordinates(coordinates["sign"]["x"], coordinates["sign"]["y"])
    click_element_by_coordinates(coordinates["sign"]["x"], coordinates["sign"]["y"])
    time.sleep(step_wait_time["sign"] / 1000)

def start_automation():
    for _ in range(repeat_times):
        perform_operations()
        pyautogui.hotkey('ctrl', 'r')  # Refresh the page
        time.sleep ( 5 )  # 在刷新后等待 5 秒
        time.sleep(step_wait_time["refresh"] / 1000)

def focus_browser():
    # 这里假设浏览器在任务栏的第一个位置，你需要根据实际情况调整
	# 切换到浏览器窗口
	pyautogui.hotkey ( 'alt' , 'tab' )  # 切换到浏览器窗口

# 启动浏览器并等待手动登录
print("请手动登录并准备好后，浏览器将自动切换并开始操作。")
time.sleep(5)  # 等待 5 秒，让你有时间切换到浏览器并登录

# 切换到浏览器并开始自动化操作
focus_browser()
time.sleep(3)  # 等待 3 秒，确保浏览器完全激活
start_automation()

