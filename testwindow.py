from flet import Page, Text, Switch, TextField, ElevatedButton, Text, app
from Kernel import flags, UserHandler
from Kernel import Input_Output as IO
import commands as cmd
flags.Runtype='gui'

UserHandler.loader(False)
flags.MODE = '9'
async def main(page=Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    text = Text()

    def textbox_changed(e):
        text.value = textbox.value #e.control.value
        # print(text.value)
        # commands.CommandList(text.value)
        IO.CommandAsk(Module=cmd.CommandList, command=text.value)
        page.update_async()

    def always_on_top_changed(e):
        page.window_always_on_top = always_on_top.value
        print(always_on_top.value)
        page.update_async()

    always_on_top = Switch(label="Always on top", value=True, on_change=always_on_top_changed)
    textbox = TextField(label="Enter Username", password=True ,can_reveal_password=True, color='green')
    button = ElevatedButton(text="Submit", on_click=textbox_changed)
    if flags.EnableIntSoft:
        def_text = Text(f"{flags.Default_text} GUI ALPHA")
    else: def_text = Text(f'MODE: {flags.MODE}')
    
    
    if flags.MODE == '9':
        await page.add_async( 
            always_on_top,
            textbox, 
            text, 
            button,
            def_text,
            )
    else:
        await page.add_async( 
            textbox, 
            text, 
            button,
            def_text,
            )
    
app(target=main)