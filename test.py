import flet as ft
from fletmint.checkbox import CheckBox
from fletmint.radio import Radio

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.scroll = "always"


    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()
    def checkbox_changed(e):
        print(f"Checkbox value changed to {e}")

    # Test components
    page.add(
        # Theme Switch
        ft.ElevatedButton(
            text="Change Theme",
            on_click=change_theme
        ),
        # Checkbox Tests
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
        ]),

        # Spacing
        ft.Container(height=40),

        # Radio Tests
        ft.Text("Radio Component Test", size=20, weight=ft.FontWeight.BOLD),
        ft.RadioGroup(
            content=ft.Column([
                Radio(
                    value="option1",
                    label="Option 1"
                ),
                Radio(
                    value="option2",
                    label="Option 2"
                ),
                Radio(
                    value="option3",
                    label="Option 3",
                    disabled=True
                ),
            ]),
            on_change=lambda e: print(f"Selected radio value: {e.control.value}")
        )
    )

ft.app(target=main)
