import flet as ft

def main(page: ft.Page):
    def clicou(e):
        page.add(
            ft.Text(f"Clicou no Container: {e.control.content.value}")
        )

    def passou(e):
        page.add(
            ft.Text(f"Passou sobre o Container")
        )

    page.title = "Aula 6- Container"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(
        ft.Container(
            content=ft.Text(
                "Container com Padding, Margin e Borda.",
                color="white",
                weight="bold"
                ),
            bgcolor="lightblue",
            padding=20,
            margin=15,
            border=ft.border.all(8, ft.Colors.BLACK),
            border_radius=10,
            width=200,
            height=200,
            on_click=clicou,
            on_hover=passou
        )
    )

ft.run(main)