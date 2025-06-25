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
newuser = False
logout = False
USERNAME = str
PASSWORD = str
LCommand = str
Module = str
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
    'easygui',
    'pygments'
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

ForbidenUsername = [
    'default'
]


file_list = [
    'Makro/CryptographyKit/DecryptPassword.py',
    'Makro/CryptographyKit/EncryptPassword.py',
    'Makro/LoginKit/two_step_verification.py',
    'Makro/RendererKit/WindowRenderer.py',
    'Makro/LoginKit/login_handler.py',
    'Makro/NetworkingKit/server.py',
    'Makro/RendererKit/Renderer.py',
    'Makro/LoginKit/user_store.py',
    'Makro/NetworkingKit/auth.py',
    'Makro/UserHandler.py',
    'Makro/credentials.py',
    'Makro/registry.py',
    'MakroPropiatery.py',
    'Makro/utils.py',
    'Makro/FTU.py',
    'pyterminal.py',
    'commands.py',
    'launcer.py',
    'Makro.py',
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
"create",
"edit file",
"view file",
"gen password",
"latest",
"talk",
"check site status",
"weather forecast",
"clear",
'show cmd',
'show apps',
'browser',
'help',
'converter',
'calculator',
'stocks',
'most used commands',
'toquel',
'plugins',
'create user',
'remove user',
'change account type',
'change password',
]

ACML = [
"activity monitor",
"chatbox install",
"Makro reload",
"fake_error",
"show flags",
"infostats",
"registry",
"devices",
"chatbox",
"ofp",
"gui",
]

MD2 = "!Advanced Mode! PyTerminal Beta"
MD3 = "PyTerminal | Native-Mode $ "
MD9 = "PyTerminal"
Default_text = 'Makro PyTerminal'
UserPath = f'{base_folder}/users/{USERNAME}.json'
Version = f'{Default_text} V.1'
all_variables = dir()