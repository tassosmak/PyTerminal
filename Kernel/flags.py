'''
Flags Start
'''

Run_Straight_Builtin = False
UserLess_Connection = False
Runtime_Tracer = False
EnableIntSoft = False
Inside_Thread = False
BuildReseted = False
Create_Graph = False
EnableAudio = False
Fully_GUI = False
GO_TO_FTU = False
EnableGUI = False
base_folder = str
sys_detect = str
logout = False
USERNAME = str
PASSWORD = str
jump = False
net = True
MODE = str
FTU = str
pl = str

'''
Flags End
'''

Dependecies = [
    'ply',
    'ffmpeg',
    'rich',
    'toga',
    'pyrad',
    'clipboard',
    'yfinance',
    'customtkinter',
    'playwright',
    'pycallgraph2',
    'ntfpy',
    'winotify',
    'maskpass',
    'easygui'
]

ModeList = [
    '1',
    '2',
    '9'
]

FtuList = [
    '1',
    '2'
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
    'Kernel/LoginKit/LoginUI.py',
    'Kernel/UserHandler.py',
    'Kernel/credentials.py',
    'Kernel/registry.py',
    'MakroPropiatery.py',
    'Kernel/utils.py',
    'Kernel/FTU.py',
    'pyterminal.py',
    'commands.py',
    'launcer.py',
    'Kernel.py',
    'Info.json',
    'pyrad.log',
]

#CML for CommandList
_CML =[
"test",
"about",
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
'show apps',
'registry',
'browser',
'help',
'ofp',
'show flags',
'converter',
'calculator',
'stocks',
'most used commands',
'fake_error',
'toquel',
'gui',
]

MD2 = "!History isn't enabled! PyTerminal Beta"
MD3 = "PyTerminal | Native-Mode $ "
MD9 = "PyTerminal"
Default_text = 'Makro PyTerminal'
Runtype= 'local'
Version = f'{Default_text} V.1'
all_variables = dir()