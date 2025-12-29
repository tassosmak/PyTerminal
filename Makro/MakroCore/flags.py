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
safe_md = False
newuser = False
logout = False
USERNAME = str
PASSWORD = str
LCommand = str
Module = bool
jump = False
net = True
MODE = str
FTU = str
pl = str
'''
Flags End
'''

Dependecies = [
    'readline',
    'pyreadline3'
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
    'MakroCore/CryptographyKit/EncryptPassword.py',
    'MakroCore/LoginKit/two_step_verification.py',
    'MakroCore/RendererKit/WindowRenderer.py',
    'MakroCore/CryptographyKit/decryp.py',
    'MakroCore/LoginKit/login_handler.py',
    'Makro/MakroCore/users/default.json',
    'MakroCore/NetworkingKit/server.py',
    'MakroCore/RendererKit/Renderer.py',
    'MakroCore/LoginKit/user_store.py',
    'MakroCore/NetworkingKit/auth.py',
    'MakroCore/UserHandler.py',
    'MakroCore/credentials.py',
    'MakroCore/registry.py',
    'MakroPropiatery.py',
    'MakroCore/utils.py',
    'MakroCore/FTU.py',
    'pyterminal.py',
    'commands.py',
]

#CML for CommandList
_CML =[
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
'plugins',
'create user',
'remove user',
'change account type',
'change password',
'password manager',
]

_ACML = [
"activity monitor",
"chatbox install",
"makro reload",
"fake_error",
"show flags",
"infostats",
'clear gui',
"registry",
"chatbox",
"test",
"ofp",
'toquel',
]

MD2 = "!Advanced Mode! PyTerminal Beta"
MD3 = "PyTerminal | Native-Mode $ "
MD9 = "PyTerminal"
Default_text = 'Makro PyTerminal'
UserPath = f'{base_folder}/users/{USERNAME}.json'
Version = f'{Default_text} V.1'
all_variables = dir()