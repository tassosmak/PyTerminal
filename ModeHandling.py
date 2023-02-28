try:
    if not __name__ == '__main__':
        from Kernel import Input_Output as IO, flags
        import commands as cmd


    def history():
        if not cmd.LCommand == '0':
            with open('src/history.log', 'a') as f:
                f.write(str(f"{cmd.LCommand}\n"))

    def core():
        if flags.MODE == '1' or flags.MODE == '2' or flags.MODE == '3' or flags.MODE == '9':
            if not flags.MODE == '3':
                IO.CommandAsk(MD=flags.MODE, Module=cmd.CommandList)
                if flags.MODE == '1':
                    history()
            else:
                IO.CommandAsk(MD=flags.MODE, Module=cmd.CommandList, safe_mode=True)
        else:
            raise IndexError
except BaseException:
    from Kernel.utils import Exit
    Exit.error_exit()
