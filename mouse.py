import win32api, win32con, json

EVENTS = ['left_click', 'right_click', 'double_click', 'wheel_up', 'wheel_down', 'wheel_right', 'wheel_left', 'mouse_move']
MOUSEEVENTF_HWHEEL = 0x01000
STEP_X = 1
STEP_Y = 1

def do(act, data):
    if act in EVENTS:
        globals()[act](data)

def left_click(data = None):
    x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def right_click(data = None):
    x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def double_click(data = None):
    x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def wheel_up(data = None):
    x = data['x']
    y = data['y']
    if x is None and y is None:
        x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, 1, 0)


def wheel_down(data = None):
    x = data['x']
    y = data['y']
    if x is None and y is None:
        x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, -1, 0)


def wheel_right(data = None):
    x = data['x']
    y = data['y']
    if x is None and y is None:
        x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, 1, 0)


def wheel_left(data = None):
    x = data['x']
    y = data['y']
    if x is None and y is None:
        x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, -1, 0)


def mouse_move(data = None):
    x = data['x']
    y = data['y']
    cur_x, cur_y = win32api.GetCursorPos()
    new_x = int(cur_x + x * STEP_X)
    new_y = int(cur_y + y * STEP_Y)
    win32api.SetCursorPos((new_x, new_y))
