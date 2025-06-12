# pip install py2app

from setuptools import setup
APP = ['autoclicker.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pyautogui', 'keyboard'],
    'plist': {
        'CFBundleName': 'MouseTool',
        'NSAAppleScriptEnabled': 'Yes'
    }
}

setup(
    app=APP,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
)