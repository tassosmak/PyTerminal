from pathlib import Path
from Makro.MakroCore import flags
dir = Path(__file__).parent.resolve()

def gen_file(username=str):
    with open(f'{flags.base_folder}/users/{username}.json', 'w+') as recover:
        recover.write('''{
        "user_credentials": {
            "Name": "",
            "Password": "",
            "Mode": "",
            "Serial": ""
        },
        "FTU": {
            "Use": ""
        },
        "Internal-Software": {
            "Enable": "0"
        },
        "UI": {
            "Enable-AquaUI": "",
            "Enable-Audio": ""
        }
    }''')