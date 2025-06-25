try:
    if not __name__ == '__main__':
        from Makro.MakroCore import Input_Output as IO, flags
        from Makro.MakroCore.SystemCalls import SystemCalls

    def core():
        if flags.MODE in flags.ModeList or flags.MODE == '3':
            IO.CommandAsk(Module=flags.Module)
            if not flags.MODE == '3' or flags.MODE == '9':
               SystemCalls.append_to_history(flags.LCommand)
        else:
            raise IndexError

except:
    from Makro.MakroCore.utils import Exit
    Exit.error_exit()
