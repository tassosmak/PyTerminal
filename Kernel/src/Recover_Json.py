from pathlib import Path
dir = Path(__file__).parent.resolve()


with open(f'{dir}/../../Info.json', 'w') as recover:
    recover.write('''{
    "user_credentials": {
        "Name": "",
        "Password": "",
        "Mode": "",
        "Serial": "",
    },
    "FTU": {
        "Use": "0",
        "IP": "0.0.0.0"
    },
    "Internal-Software": {
        "Enable": "0"
    },
    "UI": {
        "Enable-AquaUI": "1"
    }
}''')