import win32clipboard
from keyboard import ctrlPress


def print_str(clip_str):
    temp_clip = clip_get()
    clip_set(clip_str)
    ctrlPress('v')
    clip_set(temp_clip)


def clip_set(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()


def clip_get():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data
