import ctypes
import pyautogui
import tkinter as tk
from tkinter import font
import time
import threading
import queue
import random
from PIL import Image, ImageTk
import sys
from pynput.keyboard import Key, Controller

temp=0

communication_queue = queue.Queue()# 队列用于线程间通信

def update_text(text):#更新文本推送
    global text_widget
    text_widget.config(state='normal')# 设置text widget为可编辑状态
    text_widget.insert(tk.END, text + '\n')# 插入新文本
    text_widget.config(state='disabled')
    text_widget.see(tk.END)# 滚动到文本末尾

def clear_text():
    # 清空文本
    text_widget.config(state='normal')  # 设置为可编辑状态以允许删除
    text_widget.delete(1.0, tk.END)  # 删除从文本开始到末尾的所有内容
    text_widget.config(state='disabled')  # 如果需要，重新设置为不可编辑

def find_pic_move_click(pic_name):#找到图片移动点击
    # communicate_to_main_thread("正在寻找图片1...")
    # communicate_to_main_thread(pic_name)

    try:
        image2 = Image.open(pic_name)
        # 可以在这里添加更多的检查，比如检查image2.mode或image2.size
        # communicate_to_main_thread("图片成功读取。")
    except FileNotFoundError:
        communicate_to_main_thread("文件未找到，请检查路径是否正确。")
    except IOError:
        # 注意：在较新版本的Python和Pillow中，IOError可能已被OSError替代
        communicate_to_main_thread("读取图片时发生错误，可能是文件损坏或不可读。")
    except Exception as e:
        pass
        # communicate_to_main_thread("发生了一个未预料的错误")
        # 捕获其他可能发生的异常

    i=0
    while i<9000 :
        time.sleep(0.2+ random.uniform(-0.1, 0.1))
        # communicate_to_main_thread(i)
        i+=1
        try:
            enter_pos = pyautogui.locateOnScreen(pic_name, confidence=0.85)
            time.sleep(1 + random.uniform(-0.1, 0.1))
            communicate_to_main_thread(enter_pos)
            if enter_pos:
                center_pos = pyautogui.center(enter_pos)
                # communicate_to_main_thread(f"找到图片，位置：{center_pos}")
                pyautogui.moveTo(center_pos, duration=0.1)
                time.sleep(0.1)
                pyautogui.click(clicks=3, interval=0.05)
                # communicate_to_main_thread("找到图像并点击成功")
                # clear_text()
                break
        except Exception as e:
            print(f"发生错误：{e}")
            communicate_to_main_thread(e)

    else:
        communicate_to_main_thread("找不到图像")

def find_pic_move_click1(pic_name):#找到图片移动点击
    # communicate_to_main_thread("正在寻找图片1...")
    # communicate_to_main_thread(pic_name)

    try:
        image2 = Image.open(pic_name)
        # 可以在这里添加更多的检查，比如检查image2.mode或image2.size
        # communicate_to_main_thread("图片成功读取。")
    except FileNotFoundError:
        communicate_to_main_thread("文件未找到，请检查路径是否正确。")
    except IOError:
        # 注意：在较新版本的Python和Pillow中，IOError可能已被OSError替代
        communicate_to_main_thread("读取图片时发生错误，可能是文件损坏或不可读。")
    except Exception as e:
        pass
        # communicate_to_main_thread("发生了一个未预料的错误")
        # 捕获其他可能发生的异常

    i=0
    while i<9000 :
        time.sleep(0.2+ random.uniform(-0.1, 0.1))
        # communicate_to_main_thread(i)
        i+=1
        try:
            enter_pos = pyautogui.locateOnScreen(pic_name, confidence=0.85)
            time.sleep(1 + random.uniform(-0.1, 0.1))
            # communicate_to_main_thread(enter_pos)
            if enter_pos:
                center_pos = pyautogui.center(enter_pos)
                # communicate_to_main_thread(f"找到图片，位置：{center_pos}")
                pyautogui.moveTo(center_pos, duration=0.1)
                pyautogui.click(clicks=1, interval=0.2)
                # communicate_to_main_thread("找到图像并点击成功")
                break
        except Exception as e:
            pass
            # print(f"发生错误：{e}")
            # communicate_to_main_thread(e)

    else:
        communicate_to_main_thread("找不到图像")


def communicate_to_main_thread(message):#将消息发送到主线程以更新UI
    communication_queue.put(message)
    root.after(10, check_queue)

def check_queue():#检查队列中的消息并更新UI
    if not communication_queue.empty():
        message = communication_queue.get()
        update_text(str(message))

    root.after(10, check_queue)

def on_start_clicked():#开始按钮的回调函数，启动一个新线程来运行游戏
    threading.Thread(target=start_game).start()

def on_quit_clicked():#退出按钮的回调函数，销毁Tkinter窗口
    root.destroy()

def on_backspace_pressed(event):#Escape键被按下的回调函数，销毁Tkinter窗口
    root.destroy()

def check_admin_privileges():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    if is_admin != 1:
        update_text("不是管理员 正在重新启动")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        root.destroy()


def center_click():
    screenWidth, screenHeight = pyautogui.size()

    # 计算屏幕中心的x和y坐标
    centerX = screenWidth // 2
    centerY = screenHeight // 2

    # 打印屏幕中心的坐标
    # update_text("中心坐标")
    # communicate_to_main_thread(centerX)
    # communicate_to_main_thread(centerY)
    time.sleep(0.1 + random.uniform(-0.1, 0.1))
    # 点击屏幕中心
    pyautogui.click(centerX, centerY)


def final_click(pic_name):
    screenWidth, screenHeight = pyautogui.size()
    # 计算屏幕中心的x和y坐标
    centerX = screenWidth // 2
    centerY = screenHeight * 0.88625

    # 打印屏幕中心的坐标
    # update_text("中心坐标")
    # communicate_to_main_thread(centerX)
    # communicate_to_main_thread(centerY)
    time.sleep(0.2)
    # 点击屏幕中心
    try:
        image2 = Image.open(pic_name)
        # 可以在这里添加更多的检查，比如检查image2.mode或image2.size
        communicate_to_main_thread("图片成功读取。")
    except FileNotFoundError:
        communicate_to_main_thread("文件未找到，请检查路径是否正确。")
    except IOError:
        # 注意：在较新版本的Python和Pillow中，IOError可能已被OSError替代
        communicate_to_main_thread("读取图片时发生错误，可能是文件损坏或不可读。")
    except Exception as e:
        pass
        # communicate_to_main_thread("发生了一个未预料的错误")
        # 捕获其他可能发生的异常

    i=0
    while i<9000 :
        time.sleep(0.2+ random.uniform(-0.1, 0.1))
        # communicate_to_main_thread(i)
        i+=1
        try:
            enter_pos = pyautogui.locateOnScreen(pic_name, confidence=0.85)
            time.sleep(1 + random.uniform(-0.1, 0.1))
            # communicate_to_main_thread(enter_pos)
            if enter_pos:
                pyautogui.click(centerX, centerY)
                pyautogui.click(centerX, centerY)
                # communicate_to_main_thread("找到图像并点击成功")
                # clear_text()
                break
        except Exception as e:
            pass
            # print(f"发生错误：{e}")
            # communicate_to_main_thread(e)

    else:
        communicate_to_main_thread("找不到图像")
def w_forward():
    keyboard = Controller()
    communicate_to_main_thread("keyboard_success")
    keyboard.press('w')
    # 等待指定时间
    time.sleep(3)
    # 释放w键
    keyboard.release('w')

def w_forward_while_check(pic_name):
    keyboard = Controller()
    # communicate_to_main_thread("keyboard_success")
    keyboard.press('w')

    i=0
    while i<9000 :
        time.sleep(0.2+ random.uniform(-0.1, 0.1))
        # communicate_to_main_thread(i)
        i+=1
        try:
            enter_pos = pyautogui.locateOnScreen(pic_name, confidence=0.9)
            time.sleep(1 + random.uniform(-0.1, 0.1))
            # communicate_to_main_thread(enter_pos)
            if enter_pos:
                center_pos = pyautogui.center(enter_pos)
                # communicate_to_main_thread(f"找到图片，位置：{center_pos}")
                keyboard.release('w')
                keyboard.press('f')
                time.sleep(0.2)
                keyboard.release('f')
                break
        except Exception as e:
            pass
            # print(f"发生错误：{e}")
            # communicate_to_main_thread(e)

    else:
        communicate_to_main_thread("找不到图像")



def find_pic_press(pic_name):
    # communicate_to_main_thread("正在寻找图片1...")
    # communicate_to_main_thread(pic_name)
    try:
        image2 = Image.open(pic_name)
        # 可以在这里添加更多的检查，比如检查image2.mode或image2.size
        # communicate_to_main_thread("图片成功读取。")
    except FileNotFoundError:
        communicate_to_main_thread("文件未找到，请检查路径是否正确。")
    except IOError:
        # 注意：在较新版本的Python和Pillow中，IOError可能已被OSError替代
        communicate_to_main_thread("读取图片时发生错误，可能是文件损坏或不可读。")
    except Exception as e:
        pass
        # communicate_to_main_thread("发生了一个未预料的错误")
        # 捕获其他可能发生的异常
    i=0
    while i<9000 :
        time.sleep(0.2+ random.uniform(-0.1, 0.1))
        # communicate_to_main_thread(i)
        i+=1
        try:
            enter_pos = pyautogui.locateOnScreen(pic_name, confidence=0.9)
            time.sleep(1 + random.uniform(-0.1, 0.1))
            # communicate_to_main_thread(enter_pos)
            if enter_pos:
                center_pos = pyautogui.center(enter_pos)
                # communicate_to_main_thread(f"找到图片，位置：{center_pos}")
                keyboard = Controller()
                # communicate_to_main_thread("keyboard_success")
                keyboard.press(Key.esc)
                # 等待指定时间
                time.sleep(0.2)
                # 释放w键
                keyboard.release(Key.esc)
                # communicate_to_main_thread("找到图像并按下esc成功")
                break
        except Exception as e:
            print(f"发生错误：{e}")
            communicate_to_main_thread(e)

    else:
        communicate_to_main_thread("找不到图像")

def start_game():#主入口
    check_admin_privileges()
    time.sleep(0.3 + random.uniform(-0.1, 0.1))
    i=0
    while i<170:
        i=i+1
        communicate_to_main_thread(i)
        # clear_text()
        find_pic_move_click("img/11.png")
        # update_text("开始游戏")
        # clear_text()
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/12.png")
        # update_text("常规演算")
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/13.png")
        # update_text("4级")
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/14.png")
        # update_text("启动")
        time.sleep(11 + random.uniform(-0.1, 0.1))
        center_click()
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        # update_text("确认")
        time.sleep(3 + random.uniform(-0.1, 0.1))
        center_click()
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/16.png")
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/16.png")
        time.sleep(0.3 + random.uniform(-0.1, 0.1))
        w_forward()
        time.sleep(10 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/17.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/17.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/17.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/17.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/15.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_press("img/18.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click1("img/19.png")
        time.sleep(0.5 + random.uniform(-0.1, 0.1))
        find_pic_move_click("img/20.png")
        time.sleep(0.5)
        # find_pic_move_click("img/24.png")
        final_click("img/24.png")
        # clear_text()
        # 执行清理命令
        # subprocess.run(['cmd', '/c', 'ipconfig', '/flushdns'])
        # subprocess.run(['cmd', '/c', 'del', '/f', '/s', '/q', '%temp%\\*.*'])
        # subprocess.run(['cmd', '/c', 'cleanmgr', '/sagerun:1'], shell=True)
        time.sleep(0.3 + random.uniform(-0.1, 0.1))


root = tk.Tk()# 初始化Tkinter窗口和其他组件
root.wm_attributes('-topmost', True)
root.title("星铁自动化工具")
width,height=pyautogui.size()

window_width = int(width / 7)
window_height = int(height / 3.5)

y_offset = int (2.7*(height/ 4))
x_offset =0

# 设置窗口尺寸和位置
root.geometry(f"{window_width}x{window_height}+{int(x_offset)}+{int(y_offset)}")

root.bind('<BackSpace>', on_backspace_pressed)

image_path = 'img/0.png'
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
root.tk.call('wm', 'iconphoto', root._w, photo)

text_widget_font = font.Font(size=16)
text_widget = tk.Text(root, height=5, wrap=tk.WORD, state='disabled', font=text_widget_font)
text_widget.pack(expand=True, fill=tk.BOTH)

start_button = tk.Button(root, text="开始", command=on_start_clicked,font=('细行楷',14,'bold'))
start_button.pack(pady=5)

quit_button = tk.Button(root, text="退出/(backspace按键)", command=on_quit_clicked,font=('细行楷',14,'bold'))
quit_button.pack(pady=5)

update_text("星铁自动化工具 V2.0")
update_text("请保证默认队伍为打本队伍")
update_text("请保证开启自动打怪,可以在设置中找到")
update_text("请阅读说明文档 避免事故")
root.after(10, check_queue)
width, height = pyautogui.size()
root.mainloop()

