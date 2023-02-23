from Kernel.RendererKit.toga import MainWindow, Box, Button, App, WebView, TextInput
from Kernel.RendererKit.toga.style.pack import CENTER, COLUMN, ROW, Pack


class Browser(App):
    def startup(self):
        self.main_window = MainWindow(title=self.name)

        self.webview = WebView(
            on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
        )
        self.url_input = TextInput(
            value="https://tassosmak.vercel.app/", style=Pack(flex=1)
        )

        box = Box(
            children=[
                Box(
                    children=[
                        self.url_input,
                        Button(
                            "Go",
                            on_press=self.load_page,
                            style=Pack(width=50, padding_left=5),
                        ),
                    ],
                    style=Pack(
                        direction=ROW,
                        alignment=CENTER,
                        padding=5,
                    ),
                ),
                self.webview,
            ],
            style=Pack(direction=COLUMN),
        )

        self.main_window.content = box
        self.webview.url = self.url_input.value

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.url_input.value

    def on_webview_loaded(self, widget):
        self.url_input.value = self.webview.url


def main():
    return Browser("PyTerminal Broswer", "makro.pyterminal.browser")


# if __name__ == "__main__":
    # main().main_loop()

def run():
    main().main_loop()