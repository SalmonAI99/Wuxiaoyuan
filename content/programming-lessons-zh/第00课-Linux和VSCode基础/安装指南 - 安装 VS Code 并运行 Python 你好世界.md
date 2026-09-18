---
id: "安装指南 - 安装 VS Code 并运行 Python 你好世界"
aliases: []
tags:
  - setup
  - vscode
  - python
  - hello-world
lesson: 0
difficulty: "⭐⭐⭐"
os: "Ubuntu 24.04 LTS"
title: "安装指南 - 安装 VS Code 并运行 Python 你好世界"
type: setup-guide
---

# 安装指南 - 安装 VS Code 并运行 Python 你好世界

这是给 Ubuntu 24.04 用的。按顺序做，不要跳步。

它是 [[第00课 - Linux 和 VS Code 基础]] 的下一步。

## 第 1 步 - 安装 VS Code

我们去微软官网把它下载下来，再装上。

1. 按 `Ctrl + Alt + T` 打开终端。
2. 先去下载文件夹：
   ```bash
   cd ~/Downloads
   ```
   `cd` 就是走进一个文件夹。`~/Downloads` 就是你的“下载”文件夹。
3. 下载 VS Code：
   ```bash
   wget -O vscode.deb "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
   ```
   `wget` 就是从网上下载文件。`-O vscode.deb` 就是把下载的东西存成 `vscode.deb` 这个名字。
4. 安装它：
   ```bash
   sudo apt update
   sudo apt install ./vscode.deb -y
   ```
   `sudo` 就是用老大身份做事，它会问你要密码。`apt update` 是刷新一下软件名单。`apt install` 是安装。`./vscode.deb` 就是这里的这个文件。`-y` 就是“好的，直接装吧”。
5. 看看装好了没有：
   ```bash
   code --version
   ```
   你会看到 3 行带数字的东西，比如 `1.9x.x`，那就是装好了。
6. 去所有应用里打开一次 VS Code，看看能不能打开。

检查：`code --version` 能打出数字，VS Code 能打开看到欢迎页面，就是成功了。
> 只能从上面这个官网下载。不要去网上随便抄命令。如果它问你要 `sudo` 密码，就输入你的开机密码再按回车。打密码的时候看不见字，这是正常的，别怕。

## 第 2 步 - 检查 Python

Ubuntu 24.04 自带 Python，我们看一眼就行。

1. 按 `Ctrl + Alt + T` 打开终端。
2. 运行：
   ```bash
   python3 --version
   ```
3. 你会看到像这样的一行：
   ```
   Python 3.12.3
   ```
   只要是 3.10 或者更大，都可以。

如果它说 `command not found`，停下来问哥哥。

## 第 3 步 - 让 VS Code 支持 Python

1. 打开 VS Code。
2. 点左边 5 个小方块的图标（Extensions，扩展）。
![extension for python](https://code.visualstudio.com/assets/docs/python/shared/python-debugger-extension.png)
3. 搜索 `Python`，装微软做的那个 **Python**。
4. 关掉 VS Code，再重新打开。

## 第 4 步 - 运行你好世界

1. 打开文件，看看 Home 里有没有 `my-first-code` 这个文件夹。没有就新建一个。
2. 在 VS Code 里点 **File > Open Folder（文件 > 打开文件夹）** > 选 `my-first-code` > 点 **Open（打开）**。

![vscode](https://code.visualstudio.com/assets/docs/python/tutorial/toolbar-new-file.png)
3. 点 **New File（新建文件）**，输入：
   ```python
   print("Hello world")
   ```
4. 保存：按 `Ctrl + S`，名字叫 `hello.py`。一定要以 `.py` 结尾。
5. 运行：按 `Ctrl + F5`，或者点 **Run > Run Without Debugging（运行 > 不调试运行）**，问你选什么就选 **Python**。
6. 看下面的小窗口（终端），你应该会看到：
   ```
   Hello world
   ```

你成功啦！看到这行字，就说明 Python 看了你的文件，还跟你打了招呼。

如果你想自己再练几下，去这里：

[[练习/你好世界练习]]

## 如果失败了

- 没看到 `Hello world`？看看文件是不是叫 `hello.py`，保存了没有，是不是打开了文件夹，而不只是打开了一个文件。
- 红色报错说找不到 Python？回去重做第 B 步和第 C 步。
- 它让你输入 `sudo` 密码？输入你在装操作系统时设置过的密码
