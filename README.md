# PyTerminal

PyTerminal is a command-line shell written in Python. It runs on top of **Makro**, a small modular kernel that handles users, modes, commands, plugins and rendering. This repository is the PyTerminal application; Makro is included as a git submodule.

> **Status:** personal project, work in progress. The `master` branch is the stable one; day-to-day work happens on `Dev`.

## Features

- **Modes**: Basic, Advanced and Safe. Basic keeps things simple, Advanced adds file editing and system tools, and Safe disables anything that touches the network or the file system.
- **Users**: per-user profiles with a stored mode and UI settings.
- **Built-in commands**:
  - Files: `ls`, `create`, `del`, `view file`, `edit file`
  - System: `time`, `clear`, `activity monitor`, `check site status`, `weather forecast`
  - Account: `create user`, `remove user`, `change password`, `change account type`
  - Utilities: `calculator`, `converter`, `countdown`, `stocks`, `gen password`, `password manager`, `browser`, `talk`
  - Type `help` for the list available in your mode.
- **Plugins**: separate scripts launched in their own window, with a permission file per plugin (filesystem, notifications, personal data).
- **Rendering**: coloured output and native macOS dialogs, with a plain-terminal fallback.
- **Error logging**: failures are recorded to a log file instead of crashing silently.

## Requirements

- Python 3.9 or newer (developed and tested on macOS with 3.9.15)
- macOS is the primary platform. Linux works for most commands; Windows support is partial.
- Optional packages used by individual features: `psutil`, `yfinance`, `playwright`, `customtkinter`, `toga`.

## Getting started

```bash
git clone --recurse-submodules https://github.com/tassosmak/PyTerminal.git
cd PyTerminal
python pyterminal.py Run
```

If you cloned without `--recurse-submodules`, run `git submodule update --init`.

### Command-line arguments

| Argument | What it does |
|---|---|
| `Run` | Start the shell |
| `ClearErrors` | Empty the error log |
| `ClearHistory` | Empty the command history |
| `FakeLogin` | Open the login screen without starting the shell |

Running `python pyterminal.py` with no argument prints this list.

## Project layout

```text
PyTerminal/
├── pyterminal.py          # Entry point and argument handling
├── Makro/                 # Kernel (git submodule)
│   ├── Boot/              # Launcher loop
│   ├── MakroCore/         # Kernel: commands, users, login, logging, renderer
│   ├── Drivers/           # Input, notifications and audio drivers
│   └── Plugins/           # Plugins and the permission layer
└── GitHub_screenshots/
```

## How it works

1. `pyterminal.py Run` checks that no other instance is running, then loads the user profile.
2. The launcher loops: read a line, pass it to the command handler, run the matching command.
3. Commands that need their own window are started as plugins.
4. Errors go to `Makro/MakroCore/ErrorLoggingKit/errors.log`.

## Known limitations

- Only one instance can run at a time.
- Some commands pass typed input to the system shell. Only use it with input you trust.

## Contributing

Issues and pull requests are welcome. Please open an issue first for larger changes.

## License

No license file is included yet. Add one before sharing the project more widely.
