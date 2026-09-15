---
title: "Lesson 00 - Linux and VS Code Basics"
lesson: 0
audience: complete beginner
os: Ubuntu 24.04 LTS
tags: [lesson, linux, vscode, beginner]
---

# Lesson 00 - Linux and VS Code Basics

Welcome! This lesson is just to look around. You don't need to remember everything. You just need to know: where are my files, what is the Terminal, and what is VS Code.

Next step when ready: [[Setup - Install VS Code and Run Python Hello World]].

## 1. What is Ubuntu Linux?

Think of your computer like a house.

- **Ubuntu** is the house itself. Windows and macOS are different houses. Ubuntu is free and very popular for programming.
- **Files** are like clothes. **Folders** are like drawers. One drawer can hold clothes and smaller boxes.
- Everything lives in one big closet that starts at `/`. Your stuff lives in `/home/your-name`, also called `Home`.

You already know how to use it: you can click, open folders, and move files. That's Linux too.

Try it:
1. Open **Files** from the left bar.
2. Go to **Home**.
3. Make a new folder: right-click > New Folder, name it `my-first-code`.

That's it. You just did Linux.

## 2. What is the Terminal?

The **Terminal** is a way to talk to the computer by typing instead of clicking.

Think of it like texting your computer. You write a short message, press Enter, it answers.

Don't be scared of it. Programmers use it because typing is sometimes faster than clicking.

Try it safe:
1. Press `Ctrl + Alt + T`. A black window opens. That's the Terminal.
2. Type this and press Enter:
   ```bash
   pwd
   ```
   It answers with where you are, like `/home/your-name`. `pwd` means "where am I?"
3. Type this and press Enter:
   ```bash
   ls
   ```
   It lists what is in this folder, like opening the drawer and looking inside.
4. Type this to move into your new folder and look again:
   ```bash
   cd my-first-code
   pwd
   ls
   ```
5. If the screen gets messy, type `clear` and press Enter. It just cleans the window.

Only 4 words to remember for now: `pwd`, `ls`, `cd`, `clear`.

> Rule: if a command asks for your password with `sudo`, stop and ask for help first.

## 3. What is VS Code?

**VS Code** is like a super notebook for code.

- Normal notebook = for homework.
- VS Code = for code. It colors the words, finds mistakes, and can run what you wrote.

You will use it like this:
1. You type code on the left.
2. You press Run.
3. You see the result on the right or at the bottom.

You don't need to learn all buttons now. You only need: open folder, make new file, type, save, run.

## 4. How do they fit together?

Simple picture:

- **Ubuntu** = the house.
- **Files** = your drawers.
- **Terminal** = texting the house.
- **VS Code** = your notebook on the table.
- **Python** = a helper who reads your notebook and does what you wrote.

Next you will install the notebook and ask Python to say hello. Go here:

[[Setup - Install VS Code and Run Python Hello World]]

## 5. Mini check

You are ready for setup if you can:
- [ ] Open Files and find your Home
- [ ] Open Terminal with `Ctrl + Alt + T`
- [ ] Run `pwd` and `ls` without fear

If something looks scary or red, just close the window and ask. You cannot break anything with what we did today.
