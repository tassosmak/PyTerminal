from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags, utils

def regedit():
    """Registry Editor"""
    RD.CommandShow('Select the option you want to change:\n1. GUI\n2. Use\n3. Audio', header='Registry').Choice('Audio', 'Use', 'GUI')
    
        #GUI
    if RD.Quest_result == '1' or RD.Quest_result.lower() == 'gui':
        RD.CommandShow(msg='Do You Want to Enable it or Disable it\nSelect', header='Registry').Input()
        if RD.Quest_result.lower() == 'enable':
            utils.edit_user_config(flags.USERNAME, Loc1='UI', Loc2='Enable-AquaUI', Content='1')
            flags.EnableGUI == True
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
        elif RD.Quest_result.lower() == 'disable':
            utils.edit_user_config(flags.USERNAME, Loc1='UI', Loc2='Enable-AquaUI', Content='0')
            flags.EnableGUI == False
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
    
        #USE
    elif RD.Quest_result == '2' or RD.Quest_result.lower() == 'use':
        RD.CommandShow(msg='How Do You Want To Use This Instanche?, Type Compact or Personal :', header='Registry').Input()
        if RD.Quest_result.lower() == "compact" or RD.Quest_result == '2':
            utils.edit_user_config(flags.USERNAME, Loc1='FTU', Loc2='Use', Content='2')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.FTU == '2'
        elif RD.Quest_result.lower() == 'personal' or RD.Quest_result == '1':
            utils.edit_user_config(flags.USERNAME, Loc1='FTU', Loc2='Use', Content='1')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.FTU == '1'
            
        #AUDIO
    elif RD.Quest_result == '3' or RD.Quest_result.lower() == 'audio':
        RD.CommandShow(msg='Do You Want to Enable it or Disable it\nSelect', header='Registry').Input()
        if RD.Quest_result.lower() == 'enable':
            utils.edit_user_config(flags.USERNAME, Loc1='UI', Loc2='Enable-Audio', Content='1')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.EnableAudio == True
        elif RD.Quest_result.lower() == 'disable':
            utils.edit_user_config(flags.USERNAME, Loc1='UI', Loc2='Enable-Audio', Content='0')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.EnableAudio == False