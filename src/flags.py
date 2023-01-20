import platform

'''
Flags Start
'''

MODE = 0
USERNAME = 0
PASSWORD = 0
FTU = 0
EnableIntSoft = False
pl = 0
EnableGUI = False
UserLess_Connection = "0"
GO_TO_FTU = False
sys_detect = platform.uname()

'''
Flags End
'''


ModeList = [
    '1',
    '2',
    '9'
]

ArgsList = [
    "Run",
    "ClearErrors",
    "ClearHistory",
    "FakeLogin",
    "NoThread"
]


file_list = [
    'commands.py',
    'Info.json',
    'Kernel.py',
    'launcer.py',
    'MakroPropiatery.py',
    'pyrad.log',
    'UserHandler.py',
    'Boot.py',
    'CryptographyKit/DecryptPassword.py',
    'CryptographyKit/EncryptPassword.py',
    'NetworkingKit/server.py',
    'NetworkingKit/auth.py',
    'RendererKit/Renderer.py',
    'RendererKit/WindowRenderer.py',
    'UserHandlingKit/credentials.py',
    'UserHandlingKit/FTU.py',
    'UserHandlingKit/utils.py',
    'UserHandlingKit/UserHandler.py'
]

CML =[
"test",
"about",
"ABOUT",
"time",
"exit",
"version",
"jump",
"logout",
"ls",
"del",
"print md",
"countdown",
"devices",
"chatbox",
"chatbox install",
"activity monitor",
"create",
"edit file",
"view file",
"gen password",
"latest",
"edit parameters",
"talk",
"check site status",
"weather forecast",
"clear"
]

Default_text = 'Makro PyTerminal Beta'