import subprocess
from pathlib import Path
import os


def get_windows_applications():
    powershell = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

    result = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-Command",
            'Get-StartApps | ForEach-Object { "$($_.Name)|$($_.AppID)" }'
        ],
        capture_output=True,
        text=True
    )

    applications = {}

    for line in result.stdout.splitlines():
        if "|" not in line:
            continue

        name, app_id = line.split("|", 1)
        applications[name.lower()] = app_id

    return applications


def get_installed_applications():
    app_locations = [
        Path(os.environ["APPDATA"]) / "Microsoft/Windows/Start Menu/Programs",
        Path(os.environ["PROGRAMDATA"]) / "Microsoft/Windows/Start Menu/Programs"
    ]

    applications = {}

    for location in app_locations:
        if not location.exists():
            continue

        for shortcut in location.rglob("*.lnk"):
            app_name = shortcut.stem.lower()
            applications[app_name] = shortcut

    return applications


def open_windows_application(app_id):
    os.startfile(f"shell:AppsFolder\\{app_id}")


def open_application(name):
    windows_applications = get_windows_applications()

    app_id = windows_applications.get(name.lower())

    if app_id:
        open_windows_application(app_id)
        return f"Opened {name}."

    installed_applications = get_installed_applications()

    app = installed_applications.get(name.lower())

    if app:
        os.startfile(app)
        return f"Opened {name}."

    return f"I couldn't find {name}."