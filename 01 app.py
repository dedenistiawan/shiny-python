from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello dedennnnn!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

app = App(app_ui, server)

#jika menggunkan spyder harus menambahkan library ini
import nest_asyncio
nest_asyncio.apply()

app.run()