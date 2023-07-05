try:
    if not __name__ == '__main__':
        from Kernel import Input_Output as IO, flags
        from Kernel.SystemCalls import SystemCalls
        import commands as cmd

    def core():
        if flags.MODE == '1' or flags.MODE == '2' or flags.MODE == '3' or flags.MODE == '9':
            IO.CommandAsk(Module=cmd.CommandList)
            if flags.MODE == '1':
               SystemCalls.append_to_history(cmd.LCommand)
        else:
            raise IndexError

except:
    from Kernel.utils import Exit
    Exit.error_exit()
