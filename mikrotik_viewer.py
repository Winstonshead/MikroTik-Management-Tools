"""
MikroTik Support Tool: the technical support's window onto what the scanner found.

It reads the same MikroTikTool.json (and the same Backups folder) as
mikrotik_scanner.py and shows the table with its filters, colours, search,
«Подробная информация» and the installer's tasks (right click on a problem).
It cannot scan, update, send commands, make backups, import or export, and it
writes no log files. Left: Winbox (login, password, port), «Подтвердить»,
«★ Избранное», «Открыть бэкапы» and «Удалить».

It keeps its own login / column settings in its own sections of MikroTikTool.json
("viewer_settings", "viewer_ui"), so the scanner's saved login and password are never
read here. Before the file is handed over, untick «Запомнить настройки» in the
scanner: that removes the scanner's saved password from the file.
"""

from __future__ import annotations

from tkinter import Tk

from mikrotik_scanner import AUTHOR, VERSION, ScannerApp


class ViewerApp(ScannerApp):
    VIEWER = True
    TITLE = f"MikroTik Support Tool ({VERSION}) by {AUTHOR}"
    ICON_TILE = (30, 132, 73)     # the support tool's icon: a white M on a green tile
    ICON_LED = (255, 255, 255)    # white lights: green ones would vanish on the tile
    SETTINGS_SECTION = "viewer_settings"
    UI_SECTION = "viewer_ui"


def main() -> None:
    root = Tk()
    ViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
