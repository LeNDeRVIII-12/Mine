import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
from multiprocessing import Process
import random
import keyboard

# Загрузка изображений, которые мы будем искать и соответствующих им действий
images_and_actions = {
    'Up.jpg': 'up_arrow',  # Для первой картинки выполняем нажатие стрелочки вверх
    'D.jpg': 'D',
    'B.jpg': 'B',
    'Down.jpg': 'down_arrow',
    'F.jpg': 'F',
    'H.jpg': 'H',
    'Left.jpg': 'left_arrow',
    'Right.jpg': 'right_arrow',
    'Q.jpg': 'Q',
    'R.jpg': 'R',
    'S.jpg': 'S',
    'SHIFT.png': 'shift',
    'SPACE.jpg': 'space',
    'V.jpg': 'V',
    'W.jpg': 'W',
}

# Определение точности соответствия изображения
threshold = 0.85

# Время удерживания клавиши (в секундах)
key_hold_time = 1.1
def process_screen():
    while True:
        # Скриншот текущего экрана
        screenshot = np.array(ImageGrab.grab(bbox=(842, 737, 1075, 936)))
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        _, binary_screenshot = cv2.threshold(gray_screenshot, 200, 255, cv2.THRESH_BINARY)

        # Поиск соответствия на скриншоте
        for target_image_name, action in images_and_actions.items():
            target_image = cv2.imread(target_image_name, cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(binary_screenshot, target_image, cv2.TM_CCOEFF_NORMED)
            locations = np.where(result >= threshold)

            # Если изображение найдено, выполнить соответствующее действие
            if len(locations[0]) > 0:
                print(f"Found {target_image_name}: {action}")

                # Выполнить действие в зависимости от обнаруженного изображения
                if action == 'up_arrow':
                    pyautogui.keyDown('up')  # Зажать клавишу стрелочки вверх
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('up')  # Отпустить клавишу
                elif action == 'shift':
                    pyautogui.keyDown("shiftleft")   # Зажать клавишу "Shift"  # Зажать клавишу "Shift"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp("shiftleft")  # Отпустить клавишу
                elif action == 'down_arrow':
                    pyautogui.keyDown('down')  # Зажать клавишу стрелочки вниз
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('down')  # Отпустить клавишу
                elif action == 'D':
                    pyautogui.keyDown('d')  # Зажать клавишу "D"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('d')  # Отпустить клавишу
                elif action == 'B':
                    pyautogui.keyDown('b')  # Зажать клавишу "B"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('b')  # Отпустить клавишу
                elif action == 'F':
                    pyautogui.keyDown('f')  # Зажать клавишу "F"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('f')  # Отпустить клавишу
                elif action == 'H':
                    pyautogui.keyDown('h')  # Зажать клавишу "H"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('h')  # Отпустить клавишу
                elif action == 'left_arrow':
                    pyautogui.keyDown('left')  # Зажать клавишу стрелочки влево
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('left')  # Отпустить клавишу
                elif action == 'right_arrow':
                    pyautogui.keyDown('right')  # Зажать клавишу стрелочки вправо
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('right')  # Отпустить клавишу
                elif action == 'Q':
                    pyautogui.keyDown('q')  # Зажать клавишу "Q"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('q')  # Отпустить клавишу
                elif action == 'R':
                    pyautogui.keyDown('r')  # Зажать клавишу "R"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('r')  # Отпустить клавишу
                elif action == 'S':
                    pyautogui.keyDown('s')  # Зажать клавишу "S"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('s')  # Отпустить клавишу
                elif action == 'space':
                    pyautogui.keyDown('space')  # Зажать клавишу "Space"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('space')  # Отпустить клавишу
                elif action == 'V':
                    pyautogui.keyDown('v')  # Зажать клавишу "V"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('v')  # Отпустить клавишу
                elif action == 'W':
                    pyautogui.keyDown('w')  # Зажать клавишу "W"
                    time.sleep(key_hold_time)  # Удерживаем клавишу
                    pyautogui.keyUp('w')  # Отпустить клавишу
        # Генерация случайной задержки от 100 до 1000 миллисекунд
        random_delay = random.randint(400, 600) / 1000  # переводим в секунды

        # Использование случайной задержки
        time.sleep(random_delay)
        # Отображение результата (опционально)
        for loc in zip(*locations[::-1]):
            cv2.rectangle(screenshot, loc, (loc[0] + target_image.shape[1], loc[1] + target_image.shape[0]), (0, 255, 0), 2)
        cv2.imshow('Screen Capture', binary_screenshot)

        # Выход из цикла при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Закрытие окна
    cv2.destroyAllWindows()
if __name__ == '__main__':
    # Создаем процесс для обработки скриншотов
    screen_process = Process(target=process_screen)
    screen_process.start()

    # Основной процесс будет продолжать свое выполнение
    while True:
        # Дополнительные задачи, которые могут быть выполнены в основном процессе
        pass