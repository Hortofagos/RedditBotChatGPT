import cv2
import numpy as np
import random
import openai
import pyautogui
import time
import keyboard
import pyperclip

openai.api_key = 'YOUR_OPENAI_KEY'
list_of_subreddits = ['r/ProgrammerHumor', 'r/python', 'r/learnprogramming']


def copy_text(button_loc_1):
    time.sleep(1)
    pyautogui.scroll(20)
    time.sleep(0.3)
    button_x, button_y = button_loc_1
    x = button_x + random.randrange(20, 60)
    y = button_y
    pyautogui.moveTo(button_x, button_y, duration=0.3)
    time.sleep(0.5)
    for _ in range(3):
        pyautogui.click(x, y)
        time.sleep(0.1)
    time.sleep(1)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    # Print the copied textly agree! A
    print("Copied Text:", copied_text)
    return copied_text


describe_chatgpt_mission = "Reply to this reddit comment: "

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate GPT-3 model
        messages=[
            {"role": "user", "content": describe_chatgpt_mission + prompt}
        ],
        max_tokens=80  # Adjust as needed
    )
    return response.choices[0].message['content'].strip()


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
    button_loc = locate_image_on_screen(template_path, threshold=0.85)
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
    pyautogui.click(button_center_x, button_center_y)
    time.sleep(random.uniform(0.7, 3.2))
    pyautogui.write(sub, interval=0.1)
    pyautogui.moveTo(button_center_x, button_center_y + 110, duration=random.uniform(0.8, 2.5))
    pyautogui.click()
    time.sleep(2)

def write_comment():

    time.sleep(3)
    for x in range(2):
        pyautogui.scroll(-abs(random.randrange(500, 1000)))

    while True:
        time.sleep(random.uniform(0.5, 9.5))
        bottom_of_page = locate_button('img/bottom_post.png')
        if bottom_of_page is not None:
            break
        def random_mouse_movement():
            random_x = random.randint(180, 200)
            random_y = random.randint(500, 600)
            pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.5))
            pyautogui.click()

        def move_to_button(button_loc):
            button_x, button_y = button_loc
            button_center_x = button_x + random.randrange(20, 60)
            button_center_y = button_y + random.randrange(10, 15)
            pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 1.5))
            pyautogui.click(button_center_x, button_center_y)
            time.sleep(random.uniform(0.7, 3.2))
            print("Button clicked")

        button_location = locate_button('img/button.png')
        if button_location is not None:
            extracted_text = copy_text(button_location)
            if extracted_text:
                response = generate_response(extracted_text)
                print("Response:", response)
                random_mouse_movement()
                pyautogui.scroll(-20)
                time.sleep(0.4)
                move_to_button(button_location)
                text_to_type = response
                pyautogui.write(text_to_type, interval=0.1)
                time.sleep(random.uniform(0.4, 1.6))
                pyautogui.scroll(-100)
                time.sleep(0.5)
                button_location_2 = locate_button('img/button_reply.png')
                if button_location_2 is not None:
                    move_to_button(button_location_2)
                print("comment typed")
                time.sleep(1)
                bottom_of_page = locate_button('img/bottom_post.png')
                if bottom_of_page is not None:
                    break
            else:
                print("No text extracted from the screen.")
        else:
            print('no button')
        for x in range(3):
            pyautogui.scroll(-abs(random.randrange(300, 500)))

def scroll_subreddit():
    time.sleep(10)
    for s in list_of_subreddits:
        num_of_posts_to_reply_to_inside_sub = 4
        for x in range(num_of_posts_to_reply_to_inside_sub):
            time.sleep(1)
            for c in range(2):
                pyautogui.scroll(-abs(random.randrange(500, 600)))
                time.sleep(0.3)
            button_loc = locate_button('img/reddit_post.png')
            if button_loc is not None:
                button_x, button_y = button_loc
                button_center_x = button_x - random.randrange(20, 40)
                button_center_y = button_y - random.randrange(40, 70)
                pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 1.5))
                pyautogui.click(button_center_x, button_center_y)
                time.sleep(random.randrange(3, 5))
                write_comment()
                pyautogui.hotkey('alt', 'left')
                time.sleep(2)
                pyautogui.hotkey('enter')
        new_subreddit(s)


if __name__ == '__main__':
    scroll_subreddit()
