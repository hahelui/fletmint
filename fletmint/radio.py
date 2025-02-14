from flet import (
    CupertinoRadio as FletRadio,
    ThemeMode,
    Row,
    FontWeight,
    TextStyle,
)
from dataclasses import dataclass

@dataclass
class RadioColors:
    active_color: str
    inactive_color: str
    disabled_color: str
    label_color: str

    @staticmethod
    def dark():
        return RadioColors(
            active_color="#5a76f7",
            inactive_color="#26283c",
            disabled_color="#193fa0",
            label_color="#ffffff"
        )

    @staticmethod
    def light():
        return RadioColors(
            active_color="#1f5eff",
            inactive_color="#c1c9e0",
            disabled_color="#5282fe",
            label_color="#000000"
        )

class Radio(Row):
    def __init__(
        self,
        value: str,
        label: str = "",
        font_size: int = 16,
        theme: ThemeMode | str = ThemeMode.DARK,
        disabled: bool = False,
    ):
        super().__init__(
            expand=False,
            spacing=0,
        )

        self.colors = RadioColors.dark() if theme == ThemeMode.DARK else RadioColors.light()
        self.disabled = disabled

        self.radio_button = FletRadio(
            value=value,
            disabled=disabled,
            fill_color=self.colors.active_color if not disabled else self.colors.disabled_color,
            label=label,
            scale=0.9,
        )

        if label:
            self.radio_button.label = "  " + label  # Add spacing before label

        self.controls = [self.radio_button]
