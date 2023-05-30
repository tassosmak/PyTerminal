from Kernel.RendererKit import Renderer as RD
from Kernel import flags, utils

def regedit():
    
    RD.CommandShow(msg=f'Registry Values \nGUI: {flags.EnableGUI}\nUse : {flags.FTU}\nAudio : {flags.EnableAudio}', header='Registry').Input()
    
        #GUI
    if RD.Quest_result == '1':
        RD.CommandShow(msg='Do You Want to Enable it or Disable it\nSelect', header='Registry').Input()
        if RD.Quest_result == 'enable' or RD.Quest_result == 'Enable':
            utils.edit_json(loc1='UI', loc2='Enable-AquaUI', content='1')
            flags.EnableGUI == True
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
        elif RD.Quest_result == 'disable' or RD.Quest_result == 'Disable':
            utils.edit_json(loc1='UI', loc2='Enable-AquaUI', content='0')
            flags.EnableGUI == False
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
    
        #USE
    elif RD.Quest_result == '2':
        RD.CommandShow(msg='How Do You Want To Use This Instanche?, Type Compact or Personal :', header='Registry').Input()
        if RD.Quest_result == "Compact" or RD.Quest_result == '2':
            utils.edit_json(loc1='FTU', loc2='Use', content='2')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.FTU == '2'
        elif RD.Quest_result == 'Personal' or RD.Quest_result == '1':
            utils.edit_json(loc1='FTU', loc2='Use', content='1')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.FTU == '1'
            
        #AUDIO
    elif RD.Quest_result == '3':
        RD.CommandShow(msg='Do You Want to Enable it or Disable it\nSelect', header='Registry').Input()
        if RD.Quest_result == "Enable" or RD.Quest_result == 'enable':
            utils.edit_json(loc1='UI', loc2='Enable-Audio', content='1')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.EnableAudio == True
        elif RD.Quest_result == 'Disable' or RD.Quest_result == 'disable':
            utils.edit_json(loc1='UI', loc2='Enable-Audio', content='0')
            RD.CommandShow('You Have to reboot to use the changes').Show('WARNING')
            flags.EnableAudio == False