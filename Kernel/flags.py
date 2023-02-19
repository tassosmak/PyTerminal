'''
Flags Start
'''

UserLess_Connection = False
ThreadActivated = True
EnableIntSoft = False
Inside_Thread = False
BuildReseted = False
EnableAudio = False
Fully_GUI = False
GO_TO_FTU = False
EnableGUI = False
base_folder = ''
sys_detect = ''
logout = False
USERNAME = ''
PASSWORD = ''
jump = False
net = True
MODE = ''
FTU = ''
pl = ''

'''
Flags End
'''

Dependecies = [
    'customtkinter',
    'rich',
    'playwright',
    'pyrad',
    'clipboard',
    'ffmpeg',
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
"talk",
"check site status",
"weather forecast",
"clear",
"infostats",
'show cmd',
'registry',
]

MD2 = "!History isn't enabled! PyTerminal Beta"
MD3 = "PyTerminal | Safe-Mode $ "
MD9 = "PyTerminal"
Default_text = 'Makro PyTerminal Beta'