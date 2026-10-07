---
title: "附录 - 在 Ubuntu 上运行 History App"
audience: 完全零基础
os: Ubuntu 24.04 LTS
tags: [appendix, docker, git, ubuntu, web-app]
type: guide
difficulty: "⭐⭐"
---

# 附录 - 在 Ubuntu 上运行 History App

这份指南会在 Ubuntu 24.04 上安装 Docker，下载 `history_app` 程序，再启动它的网站。

**Docker** 可以把程序和它需要的小工具装在一个“盒子”里，让不同电脑更容易运行同一个程序。**Git** 是从 GitHub 下载程序源代码的工具。**Docker Compose** 会按照项目里的设置启动网站。

你需要一台能上网、可以打开图形浏览器的 Ubuntu 电脑。整个过程可能要几分钟，因为 Docker 会下载文件并编译网站。

## 一次完成安装和启动

1. 按 `Ctrl + Alt + T` 打开“终端”。
2. 把下面整段命令复制并粘贴到终端，然后按回车。
3. 如果 Ubuntu 问你密码，输入电脑的登录密码，再按回车。输入时屏幕上不会显示字符，这是正常的。

```bash
bash <<'SCRIPT'
set -Eeuo pipefail

if [[ "${EUID}" -eq 0 ]]; then
  echo "请用普通用户运行这段命令，不要先输入 sudo。"
  exit 1
fi

if [[ ! -r /etc/os-release ]]; then
  echo "找不到系统版本信息。这个指南只适用于 Ubuntu。"
  exit 1
fi

. /etc/os-release
if [[ "${ID:-}" != "ubuntu" ]]; then
  echo "检测到的系统不是 Ubuntu。这个指南只适用于 Ubuntu。"
  exit 1
fi

ubuntu_codename="${UBUNTU_CODENAME:-${VERSION_CODENAME:-}}"
if [[ -z "$ubuntu_codename" ]]; then
  echo "没有找到 Ubuntu 版本代号，无法添加 Docker 软件源。"
  exit 1
fi

echo "正在安装 Git 和 Docker……"
sudo apt-get update
sudo apt-get install -y ca-certificates curl git

sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

architecture="$(dpkg --print-architecture)"
echo "deb [arch=${architecture} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu ${ubuntu_codename} stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

app_dir="$HOME/history_app"
if [[ -d "$app_dir/.git" ]]; then
  echo "找到已有的下载目录：$app_dir"
elif [[ -e "$app_dir" ]]; then
  echo "$app_dir 已经存在，但它不是 history_app 的 Git 下载目录。请先给这个文件夹改名，再重新运行。"
  exit 1
else
  git clone https://github.com/SalmonAI99/history_app.git "$app_dir"
fi

cd "$app_dir"
echo "正在构建并启动网站。第一次启动可能需要几分钟……"
sudo docker compose up -d --build

site_url="http://localhost:3000"
echo "正在等待网站准备好……"
for attempt in $(seq 1 120); do
  if curl --fail --silent "$site_url" > /dev/null; then
    echo "网站已经启动：$site_url"
    if command -v xdg-open > /dev/null 2>&1; then
      xdg-open "$site_url" > /dev/null 2>&1 &
    else
      echo "请打开浏览器并访问 $site_url"
    fi
    exit 0
  fi
  sleep 5
done

echo "网站暂时没有回应。下面是最近的容器日志："
sudo docker compose logs --tail=80 web
echo "稍后可以再打开浏览器访问 $site_url。"
SCRIPT
```

脚本会从 Docker 官方的软件源安装 Docker Engine 和 Docker Compose 插件，从 Ubuntu 软件源安装 Git。它会把项目放在你的个人文件夹 `history_app` 里，并在里面运行 `docker compose up`。第一次构建时需要联网下载依赖，等待几分钟是正常的。

成功时，终端会显示 `网站已经启动`，浏览器会打开 History App。你也可以自己在浏览器地址栏输入：<http://localhost:3000>。

## 以后再打开网站

电脑重启后，按 `Ctrl + Alt + T` 打开终端，再运行：

```bash
cd ~/history_app
sudo docker compose up -d
```

然后打开浏览器访问 <http://localhost:3000>。

## 关闭网站

想暂时关掉网站时，在终端运行：

```bash
cd ~/history_app
sudo docker compose down
```

这会停止网站。你创建的数据会保存在 Docker 的数据卷里；再次运行上面的启动命令，就能重新打开。

## 常见问题

### 浏览器没有自动打开

在 Ubuntu 桌面浏览器里手动访问 <http://localhost:3000>。`localhost` 表示“这台电脑自己”。

### 终端说 `history_app` 文件夹已经存在

脚本不会覆盖已有文件。打开个人文件夹，找到 `history_app`，确认里面没有你要保留的文件后，把它改名，再重新运行安装脚本。

### 网站还没有启动

在终端运行下面的命令查看状态和日志：

```bash
cd ~/history_app
sudo docker compose ps
sudo docker compose logs --tail=80 web
```

构建期间需要联网。如果看到下载或构建错误，先确认网络正常，再运行 `sudo docker compose up -d --build` 重试。
