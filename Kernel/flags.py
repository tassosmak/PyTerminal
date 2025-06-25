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
    'Kernel/CryptographyKit/DecryptPassword.py',
    'Kernel/CryptographyKit/EncryptPassword.py',
    'Kernel/LoginKit/two_step_verification.py',
    'Kernel/RendererKit/WindowRenderer.py',
    'Kernel/LoginKit/login_handler.py',
    'Kernel/NetworkingKit/server.py',
    'Kernel/RendererKit/Renderer.py',
    'Kernel/LoginKit/user_store.py',
    'Kernel/NetworkingKit/auth.py',
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
"kernel reload",
"fake_error",
"show flags",
"infostats",
"registry",
"devices",
"chatbox",
"ofp",
"gui",
]

MD2 = "!Advanched Mode! PyTerminal Beta"
MD3 = "PyTerminal | Native-Mode $ "
MD9 = "PyTerminal"
Default_text = 'Makro PyTerminal'
UserPath = f'{base_folder}/users/{USERNAME}.json'
Runtype = 'local'
Version = f'{Default_text} V.1'
all_variables = dir()