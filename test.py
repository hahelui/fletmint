import flet as ft
from fletmint.checkbox import CheckBox

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.scroll = "always"
    page.bgcolor = "#22242a"

    def checkbox_changed(e):
        print(f"Checkbox value changed to {e}")

    # Test Checkbox component
    page.add(
        ft.Text("Checkbox Component Test", size=20, weight=ft.FontWeight.BOLD),
        ft.Column([
            CheckBox(
                label="Unchecked checkbox",
                checked=False,
                on_click=checkbox_changed
            ),
            CheckBox(
                label="Checked checkbox",
                checked=True,
                on_click=checkbox_changed
            ),
            CheckBox(
                label="Disabled checkbox",
                checked=False,
                disabled=True,
                on_click=checkbox_changed
            )
        ])
    )

ft.app(target=main)
