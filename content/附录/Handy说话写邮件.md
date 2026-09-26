---
title: "附录 - 用 Handy 说话写邮件"
audience: 完全零基础
os: Ubuntu 24.04 LTS
tags: [appendix, handy, voice, email, ubuntu]
type: guide
difficulty: "⭐⭐"
---

# 附录 - 用 Handy 说话写邮件

打字太慢？那就说话写邮件。**Handy** 是一个免费、开源的说话变文字工具：按住快捷键说话，松开，字就出现在邮件里了。

最重要的是：它完全**离线**工作，你的声音只留在自己的电脑里，不会发到网上。

官方地址：[github.com/cjpais/handy](https://github.com/cjpais/handy)。

## 0. 我们要做什么

1. **装上**：下载 Handy，装到 Ubuntu 上。
2. **设好**：检查麦克风，下载语音模型，设置快捷键。
3. **用一次**：真正用嘴说出一封邮件，再检查一遍发出去。

成功就是：你按住快捷键说一句话，邮件框里出现了这句话。

新词预告：

- **听写（Dictation）**：你说话，电脑帮你打字。
- **快捷键（Shortcut）**：几个键一起按，比如 `Ctrl + Alt + T`。Handy 靠它知道你开始说话了。
- **麦克风（Microphone）**：收你声音的小耳朵。笔记本一般自带。
- **模型（Model）**：Handy 脑子里的一本“声音字典”，第一次用时要下载，约 1 GB，要联网。

---

## 1. 安装 Handy（10 分钟）

### 第 1 步 - 下载 `.deb` 安装包

1. 打开浏览器，去 Handy 的发布页：[github.com/cjpais/handy/releases](https://github.com/cjpais/handy/releases)。
2. 找到最新版本（数字最大的那个，比如 `Handy_0.x.x_amd64.deb`）。
3. 下载以 `.deb` 结尾的文件。它会跑到你的 `Downloads（下载）` 文件夹。

`.deb` 就是 Ubuntu 的安装包，和 Windows 的 `.exe` 差不多意思。

### 第 2 步 - 安装它

1. 按 `Ctrl + Alt + T` 打开终端。
2. 进到下载文件夹：

```bash
cd ~/Downloads
```

3. 看看文件在不在：

```bash
ls Handy*.deb
```

你应该看到一行，比如 `Handy_0.9.6_amd64.deb`（数字可能不一样，没关系）。

4. 安装（用 `apt` 装，它会自动装好需要的依赖）：

```bash
sudo apt install ./Handy_*.deb
```

`sudo` 会问你要开机密码。打密码时看不见字，正常，输完按回车。

> ⚠️ 不要用 `dpkg -i` 装，除非依赖已经装好了。用上面的 `apt` 命令最省心。如果以前用 `dpkg` 装坏过，运行 `sudo apt --fix-broken install` 修一下。

5. 看看装好了没有：

```bash
handy --help
```

你应该看到一堆英文说明（`--toggle-transcription` 之类的）。看到了就是成功了。

### 第 3 步 - 打开一次

1. 按 `Super` 键（键盘上 Windows 图标那个），输入 `Handy`，打开它。
2. 第一次打开如果没反应、闪退，先装这个小零件（Handy 在 Linux 上需要它）：

```bash
sudo apt install libgtk-layer-shell0
```

装完再打开一次 Handy。

---

## 2. 第一次设置（5 分钟）

### 第 4 步 - 检查麦克风

1. 打开 **Settings（设置）> Sound（声音）> Input（输入）**。
2. 选你的麦克风（一般叫 `Internal Microphone`，内置麦克风）。
3. 对着电脑说“你好”，看下面的小音量条会不会动。会动就是好的。

如果 Handy 问你要麦克风权限，点允许。

### 第 5 步 - 下载语音模型

1. 打开 Handy 的 **Settings（设置）**。
2. 找到 **Models（模型）** 那一页。
3. 选一个模型下载：电脑新、速度快就选大的；电脑老、怕卡就选小的（比如 Small）。
4. 等它下载完（约几百 MB 到 1 GB，保持联网）。以后用就不用联网了。

你说中文还是英文都可以，模型会自动认出来。

### 第 6 步 - 设置快捷键（最重要！）

先看一眼你是哪种显示方式。Ubuntu 有两种画画面的方式，Handy 要配不同的小帮手：

```bash
echo $XDG_SESSION_TYPE
```

- 显示 `wayland` → 你是 Wayland（Ubuntu 24.04 默认就是它）。
- 显示 `x11` → 你是 X11。

**如果是 `x11`：**

```bash
sudo apt install xdotool
```

然后直接在 Handy 的 **Settings（设置）** 里设置一个快捷键，比如 `Super + O`，就能用了。

**如果是 `wayland`（大多数人是这个）：**

1. 先装打字小帮手：

```bash
sudo apt install wtype
```

2. Handy 在 Wayland 下听不到全局快捷键，所以要在系统里手动加一个：
   - 打开 **Settings（设置）> Keyboard（键盘）> Keyboard Shortcuts（快捷键）> Custom Shortcuts（自定义快捷键）**。
   - 点 **+** 加一个。
   - **Name（名字）** 填 `Toggle Handy Transcription`。
   - **Command（命令）** 填：

```
handy --toggle-transcription
```

   - 点 **Set Shortcut（设置快捷键）**，按你想要的键，比如 `Super + O`。

3. 回到 Handy 的 **Settings > Advanced（高级）**：
   - **Overlay Position（悬浮窗位置）** 设成 **None**（关掉）。在 Linux 上这个悬浮窗会抢焦点，导致字粘贴到错的地方。
   - 打开 **Audio Feedback（声音反馈）**，这样录音时有声音提示，不用看悬浮窗也知道。

设置检查：按一下你设的快捷键，说一句话，再按一下，字应该出现在光标的地方。

---

## 3. 用说话写一封邮件（真正的用一次）

以 Ubuntu 自带的 **Thunderbird** 为例，用浏览器写 Gmail 也一模一样。

1. 打开 Thunderbird，点 **Write（写邮件）**，点一下正文框（光标在里面闪）。
2. 按下你的快捷键（比如 `Super + O`），开始说话。说慢一点，一次说一两句，比如：

> 你好，我是小武。谢谢你的来信。祝你有愉快的一天。

3. 说完再按一下快捷键，停下来。等 1–2 秒，字就出现在邮件里了。
4. **一定要自己检查一遍！** 电脑听写偶尔会听错名字和数字，错了就用键盘改一改。
5. 检查好了再点发送。

第一次成功 checklist：

- [ ] 我按快捷键时听到了录音提示音
- [ ] 松开后 1–2 秒，字出现在了邮件框里
- [ ] 我检查了一遍，改掉了听错的字
- [ ] 邮件发出去了！

---

## 4. 小技巧

- **一次说一两句**，比一口气说一大段准得多。
- **标点符号要说出来**，比如说“句号”“逗号”，不然全是没标点的一长串。
- **名字、地名、数字**最容易听错，写完重点检查这三样。
- 不想按住不放？Handy 设置里有三种模式：按住录音、按一下开始/再按一下停、只用其中一种。选你顺手的。
- 看历史记录：在 Handy 主窗口的 **History** 里，以前说过的话都在，不小心弄丢了去那里找。
- 开机自带：想让 Handy 开机就准备好，用 `handy --start-hidden`（藏起来启动）。

---

## 附录：常见问题

| 你看到的 / 遇到的 | 意思 | 怎么办 |
| --- | --- | --- |
| 按快捷键没反应（Wayland） | Wayland 下 Handy 听不到全局键 | 回去做第 6 步：在系统设置里加 Custom Shortcut，命令填 `handy --toggle-transcription` |
| 说了话，字没出现（Wayland） | 缺打字小帮手 | 运行 `sudo apt install wtype`，再试 |
| 说了话，字没出现（X11） | 缺打字小帮手 | 运行 `sudo apt install xdotool`，再试 |
| 打开就闪退 / 没窗口 | 缺 `gtk-layer-shell` | 运行 `sudo apt install libgtk-layer-shell0`，再打开 |
| 字粘贴到错的地方 | 悬浮窗抢了焦点 | Settings > Advanced 里 Overlay Position 设成 None，打开 Audio Feedback |
| 第一次用很慢 / 一直转圈 | 在下载语音模型 | 连着网等它下完（几百 MB）。网不好可以按官方 README 的手动下载法装模型 |
| 听写老是错 | 说太快、环境太吵 | 一次说一两句，离麦克风近一点，周围安静一点；名字数字手动改 |
| 想看它在干什么 | 开调试模式 | 在 Handy 窗口按 `Ctrl + Shift + D`，会多出一页 Debug 信息 |

修不好？去官方仓库提问题：[github.com/cjpais/handy/issues](https://github.com/cjpais/handy/issues)，记得写：Handy 版本、Ubuntu 24.04、Wayland 还是 X11（`echo $XDG_SESSION_TYPE` 的结果）。
