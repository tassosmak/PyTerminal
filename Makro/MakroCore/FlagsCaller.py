from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags

class CallHandler:
    def get_mode():
        return flags.MODE
    
    def get_username():
        return flags.USERNAME
    
    def get_pl():
        return flags.pl
    
    def get_ftu():
        return flags.FTU
    
    def get_base_folder():
        if flags.EnableIntSoft:
            return flags.base_folder
        else: RD.CommandShow(msg='Call Not Allowed').Show('WARNING')
    
    def get_module():
        if flags.EnableIntSoft:
            return flags.Module
        else: RD.CommandShow(msg='Call Not Allowed').Show('WARNING')
        
    def IntSoft():
        if flags.EnableIntSoft:
            return True
        else:
            RD.CommandShow(msg='Call Not Allowed').Show('WARNING')
            return False