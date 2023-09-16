from Kernel.RendererKit import Renderer as RD
from Kernel import utils 
from licensing.methods import Key, Helpers
from licensing.models import *

RSAPubKey = "<RSAKeyValue><Modulus>0tz0+guDm4eroHwrTC4XiwayPS2O0NZVEwDHC3LtudbMbS9lUHZFH0Yw4Fi2xailPwyDvIjRfMuU3pOn/Vr6UA+H97Bo5rWrDMosMrzoVfywEhiyj5qQ2Q2szxEPlAkGC4Ls1L3phK/v4lNQEAWx7bWiOhtWNeKPXaU6fNZWQphPk0qRxSRzmVTaJyTh/nmEQor8BmahhEoV2fNmhzSLIShDlM6PHni4UcCZuB+sBYNTCSJrNO0g7yUUGGZM6O6tGfp6SbnGax5Ys0w0O3nebyz21fDNVC0xL830dk8+KkdpnKwBRDb2LbV1CtsBZ2oN7IZdESlo8ZVJil7dflv2NQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI2MTAyOTcyNSIsImFxeUUwQm8rMHRVcE5nRHRET2haV2kwSzlQcHVxa3JQdGRoaTRMeHYiXQ=="

def authe(license):
    result = Key.activate(token=auth, rsa_pub_key=RSAPubKey, product_id=21892, key=license, machine_code=Helpers.GetMachineCode(v=2))

    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        RD.CommandShow("The license does not work: {0}".format(result[1])).Show('FAIL')
        
    else:
        # everything went fine if we are here!
        RD.CommandShow("The license is valid!").Show('BLUE')
        utils.edit_json(loc1='user_credentials', loc2='Key', content=license)
        return True
        