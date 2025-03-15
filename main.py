import flet  as ft
import função_abre_excel as fae

def main(page: ft.Page):
    page.title = "Abre o excel"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 400
    page.window_resizable = False
    


    def chama_abre_excel(e):
        fae.abre_excel()

    page.add(
        ft.TextButton(text = 'Clique para abrir o excel', on_click = chama_abre_excel),
        ft.TextButton("Desabilita o Botão", disabled = True)
    )
        


ft.app(target = main)
