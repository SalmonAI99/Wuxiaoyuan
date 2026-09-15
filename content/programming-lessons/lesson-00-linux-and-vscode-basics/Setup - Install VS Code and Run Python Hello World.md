---
id: "Setup - Install VS Code and Run Python Hello World"
aliases: []
tags:
  - setup
  - vscode
  - python
  - hello-world
lesson: 0
os: "Ubuntu 24.04 LTS"
title: "Setup - Install VS Code and Run Python Hello World"
type: setup-guide
---

# Setup - Install VS Code and Run Python Hello World

For Ubuntu 24.04 LTS. Follow in order. No skipping.

Part of: [[Lesson 00 - Linux and VS Code Basics]].

## Part A - Install VS Code

Use the App Center. This is the easiest way.

1. Open **App Center** from the left bar.
2. Search for `Visual Studio Code`.
3. Click the one made by Microsoft, click **Install**, wait until it says Installed.
4. Open VS Code once from the app grid to check it starts.

Check: VS Code opens with a welcome window.

> If App Center does not work, ask for help. Do not copy random install commands from the internet.

## Part B - Check Python

Ubuntu 24.04 already has Python. Just check it.

1. Press `Ctrl + Alt + T` to open Terminal.
2. Run:
   ```bash
   python3 --version
   ```
3. You should see something like:
   ```
   Python 3.12.3
   ```
   Any 3.10 or higher is fine.

If you see `command not found`, stop and ask for help.

## Part C - Add Python support to VS Code

1. Open VS Code.
2. Click the 4-squares icon on the left (Extensions).
3. Search for `Python`, install the one by Microsoft called **Python**.
4. Close and reopen VS Code.

## Part D - Run Hello World

1. In Files, make sure you have a folder `my-first-code` in Home. If not, make it.
2. In VS Code: **File > Open Folder** > pick `my-first-code` > click **Open**.
3. Click **New File**, type:
   ```python
   print("Hello world")
   ```
4. Save: `Ctrl + S`, name it `hello.py`. Make sure it ends with `.py`.
5. Run it: press `Ctrl + F5` or click **Run > Run Without Debugging**, pick **Python** if asked.
6. Look at the bottom panel (Terminal). You should see:
   ```
   Hello world
   ```

You did it. That line means Python read your file and printed your message.

## If it fails

- No `Hello world`? Check file is named `hello.py`, saved, and you opened the folder, not just the file.
- Red error about Python not found? Repeat Part B and C.
- Anything asks for `sudo` password? Stop and ask for help.
