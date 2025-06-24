from flet import Page, Text, Switch, TextField, ElevatedButton, Text, app, MainAxisAlignment, KeyboardEvent, ScrollMode, ResponsiveRow, Column
from Kernel import flags, UserHandler, SystemCalls
from Kernel import Input_Output as IO
import commands as cmd



async def main(page=Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = MainAxisAlignment.SPACE_EVENLY
    text = Text()

    def on_keyboard(e: KeyboardEvent):
        if e.key == 'Enter':
            # print("Enter is pressed")
            textbox_changed(e)
            
    def textbox_changed(e):
        text.value = textbox.value #e.control.value
        # print(text.value)
        
        IO.CommandAsk(Module=cmd.CommandList, command=text.value)
        page.update_async()
        textbox.value = ''
        
    textbox = TextField(label="Input Box")
    page.on_keyboard_event = on_keyboard
    
    
    if flags.EnableIntSoft:
        def_text = Text(f"{flags.Default_text} GUI ALPHA")
        top_text = Text(SystemCalls.SystemCalls.show_flags(False))
    else: 
        def_text = Text(f'MODE: {flags.MODE}')
        top_text = Text('Makro', color='GREEN')

    if flags.MODE == '9':
        await page.add_async( 
            # ResponsiveRow(top_text),
            ResponsiveRow([Column(col=10, controls=[top_text]),
                          Column(col=10, controls=[textbox])]
                          ),
            # textbox, 
            text, 
            def_text,
            )
    else:
        await page.add_async( 
            textbox, 
            text, 
            def_text,
            )
    
def open_window():
    app(target=main)
    
if __name__ == '__main__':
    flags.Runtype='gui'
    UserHandler.loader(False)
    flags.MODE = '9'
    flags.EnableIntSoft = True
    app(main)
    