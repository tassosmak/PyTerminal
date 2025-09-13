from Makro.Drivers.NotificationsKit.PushSender import Notifications
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.SystemCalls import SystemCalls
from Makro.MakroCore.JSONhander import JSONhandle
from Makro.MakroCore.utils import is_gui
from Makro.MakroCore import flags, SNC

def _get_propiatery(print_credentials=False):
    global UserLess_Connection, GO_TO_FTU, Fully_GUI
    
    try:
        path = f'{flags.base_folder}/../../MakroPropiatery.json'
        UserLess_Connection = JSONhandle(path).read_file('user_login', 'UserLess Connection')
        flags.UserLess_Connection = UserLess_Connection
        if print_credentials:
            RD.CommandShow(msg=("UserLess Connection:", UserLess_Connection)).Show()

        GO_TO_FTU = JSONhandle(path).read_file('user_login', 'GO TO FTU')
        flags.GO_TO_FTU = GO_TO_FTU
        if print_credentials:
            RD.CommandShow(msg=("GO_TO_FTU:", GO_TO_FTU)).Show()

        Fully_GUI = JSONhandle(path).read_file('user_login', 'Fully GUI')
        if is_gui():
            if flags.pl == '1':
                flags.Fully_GUI = Fully_GUI
            else:
                flags.Fully_GUI = False
        else:
            flags.Fully_GUI = False
            flags.Inside_Thread = True
        if print_credentials:
            RD.CommandShow(msg=("Fully_GUI:", Fully_GUI)).Show()
        
        Inside_Thread = JSONhandle(path).read_file('user_login', 'Run-Threads Inside')
        flags.Inside_Thread = Inside_Thread
        if print_credentials:
            RD.CommandShow(msg=("Run-Threads Inside:", Inside_Thread)).Show()
        
        Run_Straight_Builtin = JSONhandle(path).read_file('user_login', 'Run-Straight-Builtin')
        flags.Run_Straight_Builtin = Run_Straight_Builtin
        if print_credentials:
            RD.CommandShow(msg=("Run_Straight_Builtin:", Run_Straight_Builtin)).Show()
        
        Create_Graph = JSONhandle(path).read_file('user_login', 'Create_Graph')
        flags.Create_Graph = Create_Graph
        if print_credentials:
            RD.CommandShow(msg=("Create_Graph:", Create_Graph)).Show()
            
        Runtime_Tracer = JSONhandle(path).read_file('user_login', 'Runtime_Tracer')
        flags.Runtime_Tracer = Runtime_Tracer
        if print_credentials:
            RD.CommandShow(msg=("Runtime_Tracer:", Runtime_Tracer)).Show()

        return True
    except KeyError:
        raise FileNotFoundError


    
def get_credentials(print_credentials=False, path=None):
    SystemCalls.get_folder()
    global Name, Password, Mode, FTU, GUI, SerialNum
    

    FTU = JSONhandle(path).read_file('FTU', 'Use')
    flags.FTU = FTU
    if print_credentials:
        RD.CommandShow(msg=("FTU:", FTU)).Show()
    
    GUI = JSONhandle(path).read_file('UI', 'Enable-AquaUI')
    if GUI == "1" and flags.pl == '1':
        flags.EnableGUI = True
    if print_credentials:
        RD.CommandShow(msg=("UI:", GUI)).Show()
    
    Audio = JSONhandle(path).read_file('UI', 'Enable-Audio')
    if Audio == "1":
        flags.EnableAudio = True
    if print_credentials:
        RD.CommandShow(msg=("Audio:", GUI)).Show()

    Name = JSONhandle(path).read_file('user_credentials', 'Name')
    flags.USERNAME = Name
    if print_credentials:
        RD.CommandShow(msg=("Name:", Name)).Show()


    Password = JSONhandle(path).read_file('user_credentials', 'Password')
    flags.PASSWORD = Password
    if print_credentials:
        if flags.EnableIntSoft:
            RD.CommandShow(msg=("Password:", Password)).Show()


    Internal_Software = JSONhandle(path).read_file('Internal-Software', 'Enable')
    try:
        _get_propiatery()
        if Internal_Software == "1":
            flags.EnableIntSoft = True
            RD.CommandShow('Internal Software Enabled').Show('OKGREEN')
        else: 
            flags.EnableIntSoft = False
    except FileNotFoundError:
        flags.EnableIntSoft = False
    if print_credentials:
        if flags.EnableIntSoft:
            RD.CommandShow(msg=('Flags-Var', flags.EnableIntSoft)).Show()
            RD.CommandShow(msg=("Intenal-Software", Internal_Software)).Show()
        
    Mode = JSONhandle(path).read_file('user_credentials', 'Mode')
    if flags.EnableIntSoft == False and Mode == '9':
        flags.MODE = '2'
    else:
        flags.MODE = Mode
    if print_credentials:
        RD.CommandShow(msg=("Mode:", Mode)).Show()
        
    SerialNum = JSONhandle(path).read_file('user_credentials', 'Serial')
    try:
        snc = SNC.snc()
        snc.guid(Name)
    except IndexError:
        notif = Notifications()
        notif.Sender("The Serial number of the computer doesn't match the serial number given")
        if flags.EnableIntSoft:
            RD.CommandShow("The Serial number of the computer doesn't match the serial number given").Show('FAIL')
        SystemCalls.clear_error()
        SystemCalls.clear_history()
        from MakroCore.FTU import FTU_init
        FTU_init(True).run()
        flags.BuildReseted = True
    if print_credentials:
        RD.CommandShow(msg=("Serial:", SerialNum)).Show()