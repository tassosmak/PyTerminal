'''
Flags Start
'''

UserLess_Connection = False
BuildReseted = False
ThreadActivated = True
EnableIntSoft = False
Fully_GUI = False
GO_TO_FTU = False
EnableGUI = False
base_folder = 0
sys_detect = 0
USERNAME = 0
PASSWORD = 0
net = True
MODE = 0
FTU = 0
pl = 0

'''
Flags End
'''

Dependecies = [
    'customtkinter',
    'rich',
    'playwright',
    'pyrad',
    'clipboard',
]

ModeList = [
    '1',
    '2',
    '9'
]

ArgsList = [
    "Run",
    "ClearErrors",
    "ClearHistory",
    "FakeLogin"
]


file_list = [
    'Kernel/CryptographyKit/DecryptPassword.py',
    'Kernel/CryptographyKit/EncryptPassword.py',
    'Kernel/RendererKit/WindowRenderer.py',
    'Kernel/NetworkingKit/server.py',
    'Kernel/RendererKit/Renderer.py',
    'Kernel/NetworkingKit/auth.py',
    'Kernel/UserHandler.py',
    'Kernel/credentials.py',
    'MakroPropiatery.py',
    'Kernel/utils.py',
    'UserHandler.py',
    'Kernel/FTU.py',
    'commands.py',
    'launcer.py',
    'Kernel.py',
    'Info.json',
    'pyrad.log',
    'Boot.py',
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
"clear",
"infostats",
'show cmd'
]

Default_text = 'Makro PyTerminal Beta'