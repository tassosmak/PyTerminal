from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags
import json, os


class JSONhandle:
    def __init__(self, file_path):
        self.file_path = file_path

    def edit_json(self, loc1="", loc2="", content=""):
        with open(self.file_path, 'r+') as f:
            data = json.load(f)
            if not loc2 == "":
                data[loc1][loc2] = content
            else:
                data[loc1] = content
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        
    def read_file(self, array, object):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as recover:
                try:
                    self._data = json.load(recover)
                    # if flags.EnableIntSoft:
                        # RD.CommandShow(msg=f"Reading file contents: {self._data}").Show('BLUE')
                    _object_content = self._data[array][object]
                
                    return _object_content
                except json.JSONDecodeError:
                    if flags.EnableIntSoft:
                        RD.CommandShow("Error reading file").Info()
        else:
            if flags.EnableIntSoft:
                RD.CommandShow("No file found.").Info()



    def del_contents(self, array):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        if array in data:
            del data[array]
        else: raise KeyError

        with open(self.file_path, 'w') as recover:
            json.dump(data, recover, indent=4)