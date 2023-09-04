import cv2
import numpy as np
import random
import pyautogui
import time
import keyboard
import pyperclip

pyautogui.FAILSAFE = False

first_message = [
    "I noticed your comment. Are you a Python developer?",
    "I read your comment. Do you work with Python programming?",
    "I've seen your comment. Are you proficient in Python coding?",
    "Having read your comment, do you write code in Python?",
    "After reading your comment, are you familiar with Python development?",
    "I've seen your comment. Is Python one of your programming languages?",
    "I read your comment. Have you ever written Python scripts?",
    "I noticed your comment. Are you experienced in Python scripting?",
    "I've seen your comment. Do you use Python for software development?",
    "After reading your comment, have you dabbled in Python programming?",
    "I noticed your comment. Are you skilled in Python coding?",
    "After reading your comment, is Python part of your coding toolkit?",
    "I've seen your comment. Have you ever worked on Python projects?",
    "I read your comment. Do you build applications using Python?",
    "I noticed your comment. Are you involved in Python software development?",
    "I've seen your comment. Do you write Python code professionally?",
    "Having read your comment, have you developed anything in Python?",
    "I read your comment. Are you well-versed in Python development?",
    "I noticed your comment. Do you specialize in Python programming?",
    "I've seen your comment. Have you used Python for coding tasks?",
    "After reading your comment, are you a Python enthusiast?",
    "I've seen your comment. Do you program primarily in Python?",
    "I noticed your comment. Are you a Python coder?",
    "I read your comment. Have you ever created Python applications?",
    "After reading your comment, are you knowledgeable in Python programming?",
    "I noticed your comment. Do you use Python for coding challenges?",
    "I've seen your comment. Are you a Python software engineer?",
    "I read your comment. Have you developed software with Python?",
    "I noticed your comment. Do you have experience with Python scripting?",
    "After reading your comment, are you proficient in Python application development?",
    "I've seen your comment. Do you write Python scripts for automation?",
    "I read your comment. Have you built projects using Python?",
    "I noticed your comment. Are you a Python scripter?",
    "After reading your comment, do you code with Python regularly?",
    "I read your comment. Are you well-acquainted with Python programming?",
    "I noticed your comment. Have you ever contributed to Python projects?",
    "I've seen your comment. Do you work on Python-related tasks?",
    "I read your comment. Are you skilled in Python software development?",
    "I've noticed your comment. Do you utilize Python for coding purposes?",
    "I read your comment. Have you used Python in your coding projects?",
    "I noticed your comment. Are you involved in Python coding challenges?",
    "I've seen your comment. Do you have expertise in Python development?",
    "I read your comment. Are you a Python coding enthusiast?",
    "I noticed your comment. Have you ever undertaken Python development projects?",
    "I've read your comment. Do you specialize in Python application development?",
    "After reading your comment, are you a Python coding professional?",
    "I noticed your comment. Have you created software using Python?",
    "I read your comment. Are you familiar with Python coding practices?",
    "I've seen your comment. Do you have a background in Python development?",
    "After reading your comment, are you active in the Python programming community?"
]
list_of_subreddits = ['r/ProgrammerHumor', 'r/python', 'r/ChatGPT', 'r/Bitcoin', 'r/Cryptocurrency', 'r/learnprogramming']

def locate_button(template_path):
    def locate_image_on_screen(tp, threshold=0.8):
        template = cv2.imread(tp, cv2.IMREAD_GRAYSCALE)
        screenshot = pyautogui.screenshot()
        screenshot_gray = cv2.cvtColor(cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            return max_loc
        else:
            return None
    button_loc = locate_image_on_screen(template_path, threshold=0.95)
    return button_loc

def new_subreddit(sub):
    go_home = locate_button('img/home.png')
    button_x, button_y = go_home
    button_center_x = button_x + random.randrange(30, 40)
    button_center_y = button_y + random.randrange(15, 20)
    pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.8, 2.5))
    pyautogui.click()
    search_bar = locate_button('img/search_sub.png')
    button_x, button_y = search_bar
    button_center_x = button_x + random.randrange(90, 100)
    button_center_y = button_y + random.randrange(15, 20)
    pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.8, 2.5))
    pyautogui.click()
    time.sleep(random.uniform(0.7, 3.2))
    pyautogui.write(sub, interval=0.1)
    pyautogui.moveTo(button_center_x, button_center_y + 110, duration=random.uniform(0.8, 2.5))
    pyautogui.click()
    time.sleep(2)

def write_user():
    time.sleep(4)
    for x in range(2):
        pyautogui.scroll(-abs(random.randrange(500, 1000)))
    time.sleep(4)
    def chat():
        start_chat = locate_button('img/start_chat.png')
        try:
            button_x, button_y = start_chat
            button_center_x = button_x + random.randrange(10, 20)
            button_center_y = button_y + random.randrange(10, 15)
            pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 0.5))
            pyautogui.click()
            time.sleep(4)
            chats_name = locate_button('img/chats.png')
            button_x, button_y = chats_name
            button_center_x = button_x + random.randrange(290, 300)
            pyautogui.moveTo(button_center_x, button_y, duration=random.uniform(0.2, 0.5))
            for _ in range(3):
                pyautogui.click()
                time.sleep(0.1)
            time.sleep(1)
            keyboard.press_and_release('ctrl+c')
            time.sleep(0.5)
            copied_name = pyperclip.paste()
            with open('already_messaged.txt', 'r+') as am:
                all_messaged = am.read()
                if copied_name not in all_messaged:
                    am.write(copied_name + ' ')
                    message = locate_button('img/message.png')
                    button_x, button_y = message
                    pyautogui.moveTo(button_x, button_y, duration=random.uniform(0.2, 0.5))
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.write(random.choice(first_message), interval=0.1)
                    time.sleep(0.5)
                    pyautogui.hotkey('enter')
        except Exception as error:
            print(f"An error occurred: {error}")
    comments = 0
    while comments < 10:
        comments += 1
        time.sleep(0.5)
        pyautogui.moveTo(400, 500, duration=random.uniform(0.2, 0.5))
        pyautogui.scroll(-abs(random.randrange(300, 400)))
        chat()
        user_acc = locate_button('img/reddit_account.png')
        try:
            button_x, button_y = user_acc
            print('account found')
            button_center_x = button_x + 10
            button_center_y = button_y - 20
            pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 0.5))
            time.sleep(5)
            chat()
            pyautogui.moveTo(300, 600, duration=random.uniform(0.2, 0.5))
            bottom_of_page = locate_button('img/bottom_post.png')
            if bottom_of_page is not None:
                break
        except:
            print('no reddit account')
    close_chat = locate_button('img/close_chat.png')
    try:
        button_x, button_y = close_chat
        pyautogui.moveTo(button_x + 5, button_y + 5, duration=random.uniform(0.2, 0.5))
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(1)
    except:
        pass



def scroll_subreddit():
    time.sleep(10)
    for s in list_of_subreddits:
        num_of_posts_to_reply_to_inside_sub = 7
        for x in range(num_of_posts_to_reply_to_inside_sub):
            pyautogui.moveTo(300, 600, duration=random.uniform(0.2, 0.5))
            time.sleep(4)
            for c in range(2):
                pyautogui.scroll(-abs(random.randrange(500, 600)))
                time.sleep(0.3)
            button_loc = locate_button('img/reddit_post.png')
            if button_loc is not None:
                button_x, button_y = button_loc
                button_center_x = button_x + random.randrange(40, 80)
                button_center_y = button_y + random.randrange(0, 5)
                pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 1.5))
                pyautogui.click()
                time.sleep(random.randrange(3, 5))
                write_user()
                pyautogui.moveTo(300, 600, duration=random.uniform(0.2, 0.5))
                pyautogui.hotkey('alt', 'left')
        new_subreddit(s)

if __name__ == '__main__':
    scroll_subreddit()
