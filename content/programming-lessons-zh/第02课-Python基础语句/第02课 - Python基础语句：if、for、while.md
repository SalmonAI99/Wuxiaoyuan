---
title: "第02课 - Python基础语句：if、for、while"
lesson: 2
audience: 完全零基础
os: Ubuntu 24.04 LTS
tags: [lesson, python, if, for, while, beginner]
type: lesson
difficulty: "⭐⭐"
---

# 第02课 - Python基础语句：if、for、while

还记得贪吃蛇吗？里面有三句话你当时没细看：

```python
if move == "q":
while True:
for row in game_map:
```

这三句话就是 Python 最厉害的三个本领：**做判断、重复做事**。今天我们正式学它们，还要做一个新游戏：猜数字。

如果你还没玩过贪吃蛇，先去：[[programming-lessons-zh/第01课-贪吃蛇挑战/第01课 - 贪吃蛇大挑战|第01课：贪吃蛇大挑战]]。

## 0. 我们要做什么

1. **跑起来**：打开 `guess.py`，运行它，猜中一次数字。
2. **看明白**：知道 `if` 怎么做判断，`for` 和 `while` 怎么重复。
3. **改一改**：接受大挑战，把猜数字变成你自己的游戏。

成功就是：你能说出 `==` 和 `=` 有什么不同，还改了至少 1 个挑战。

新词预告（第一次见，记住它们）：

- **条件（Condition）**：一道是非题，只能回答“对”或“错”。比如“你猜的比答案大吗？”
- **缩进（Indent）**：每行前面空出的格子。Python 靠它认出谁和谁是一伙的。
- **范围（Range）**：一组 numbers，比如 `range(5)` 就是 0、1、2、3、4。

---

## A. 轻松上手（5 步，10 分钟）

目标只有一个：运行猜数字游戏，猜中一次。

### 第 1 步 - 打开你的文件夹

1. 打开 VS Code。
2. 点 **File > Open Folder（文件 > 打开文件夹）**，选 `my-first-code`。

### 第 2 步 - 建一个 `guess.py`

1. 在 VS Code 里点 **New File（新建文件）**。
2. 把下面这份完整代码粘进去（一字不改）：

```python
from random import randint

secret = randint(1, 20)
print("I am thinking of a number between 1 and 20!")

tries = 0
while True:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess == secret:
        print("You got it!")
        print("Tries:", tries)
        break
    elif guess < secret:
        print("Too small, go bigger!")
    else:
        print("Too big, go smaller!")
```

3. 按 `Ctrl + S` 保存，名字叫 `guess.py`。

> 如果你的文件夹里已经有老师给的 `guess.py`，直接打开它用。

### 第 3 步 - 运行它

1. 按 `Ctrl + Alt + T` 打开终端。
2. 输入完整命令，按回车：

```bash
python3 guess.py
```

3. 你应该看到：

```
I am thinking of a number between 1 and 20!
Your guess:
```

电脑心里想了一个 1 到 20 的数字，等你来猜。

### 第 4 步 - 玩一局

随便输一个数字，比如 `10`，按回车。电脑会给你提示：

| 看到的 | 意思 | 下一步 |
| --- | --- | --- |
| `Too small, go bigger!` | 猜小了 | 试个更大的 |
| `Too big, go smaller!` | 猜大了 | 试个更小的 |
| `You got it!` | 猜中啦！ | 看看你用了几次 |

一直猜到 `You got it!` 为止。下面还会告诉你猜了几次，比如 `Tries: 4`。

小窍门：每次猜中间的数。比如知道在 1 到 20 之间，先猜 `10`，最多 5 次就能猜中！

### 第 5 步 - 上手检查

- [ ] 我能用 `python3 guess.py` 打开游戏
- [ ] 我知道 `Too small` 是猜小了，`Too big` 是猜大了
- [ ] 我猜中过至少 1 次，看到了 `You got it!`
- [ ] 我敢乱输、输错，不害怕（输错了重来就行）

都打勾了，就去下一部分：看懂它。

---

## B. 它是怎么工作的？（详细拆解）

猜数字只有 3 个本领：**记住答案、问你猜什么、判断给提示**。我们一段一段看。

### B1. `if`：如果……就……（第 11–13 行）

```python
if guess == secret:
    print("You got it!")
    print("Tries:", tries)
    break
```

- `if` 就是“如果”。如果后面的是非题答“对”，就做下面的事；答“错”，就跳过。
- `guess == secret` 是一道是非题：“你猜的和答案一样吗？”注意是**两个**等号 `==`，表示“一样吗？”。
- 行尾的冒号 `:` 意思是“下面就是要做的事”。
- 下面两行前面都空了 4 个格子，这叫**缩进**。有缩进的才算 `if` 的小跟班，`if` 答“对”时才会做。

生活例子：妈妈说“**如果**你写完作业，**就**可以吃冰淇淋”。没写完？那就没有。

> ⚠️ 新手最容易错：`=` 和 `==` 不一样！
>
> - `secret = randint(1, 20)`：一个等号，是“把右边的东西装进左边的盒子”。
> - `guess == secret`：两个等号，是“左边和右边一样吗？”。
>
> 一个是装东西，一个是问问题。千万别混了。

### B2. `elif` 和 `else`：否则如果……否则……（第 14–18 行）

```python
elif guess < secret:
    print("Too small, go bigger!")
else:
    print("Too big, go smaller!")
```

- `elif` 是 `else if` 的缩写，意思是“上面没中，那**否则如果**……”。只有上面的 `if` 答“错”，才会轮到它。
- `else` 是“**否则**”，前面的全答“错”，就做它。不用再写条件，也不用加是非题。
- 三句话连起来就是：猜中了 → 欢呼；没中但是猜小了 → 说小了；剩下的情况（猜大了）→ 说大了。

比较符号全家福（都会用了）：

| 符号 | 意思 | 例子（`guess` 是 10） |
| --- | --- | --- |
| `==` | 等于吗？ | `guess == 10` → 对 |
| `!=` | 不等于吗？ | `guess != 10` → 错 |
| `<` | 小于吗？ | `guess < 20` → 对 |
| `>` | 大于吗？ | `guess > 20` → 错 |
| `<=` | 小于等于吗？ | `guess <= 10` → 对 |
| `>=` | 大于等于吗？ | `guess >= 10` → 对 |

### B3. `while`：条件复读机（第 9–10 行）

```python
while True:
    guess = int(input("Your guess: "))
```

- `while` 也是复读机，但它每复读一次都要先问一道是非题。答“对”就再来一遍，答“错”就停。
- `True` 是“对”，所以 `while True:` 就是“永远是‘对’，一直重复”。和贪吃蛇里的 `while True:` 一模一样！
- 那它什么时候停？靠里面的 `break`（下一节讲）。猜中了就 `break`，跳出循环。

生活例子：**上课举手**。老师说“没猜中的同学继续猜”，举手的就一直猜，猜中的放下手，不用再猜了。

### B4. `for`：数数复读机（贪吃蛇里见过）

贪吃蛇里有这句，还记得吗？

```python
for row in game_map:
    print("".join(row))
```

- `for` 是“把一堆东西一个一个拿出来，每个都做一遍”。堆里有几个，就做几次，做完自动停。
- `range(5)` 会变出 5 个数：0、1、2、3、4。注意是从 **0** 开始的！
- 所以下面这段会打印 5 次：

```python
for i in range(5):
    print("Hello!")
```

```
Hello!
Hello!
Hello!
Hello!
Hello!
```

`i` 是一个小盒子，第一次装 0，第二次装 1……每次自动换下一个。不用你管，`for` 帮你数。

### B5. `for` 和 `while` 怎么选？

记住一句话：

- **知道要做几次 → 用 `for`**。比如“打印 5 次”“6 次机会”。
- **不知道要做几次 → 用 `while`**。比如“一直猜到猜中为止”“游戏一直跑到撞墙为止”。

| | `for` | `while` |
| --- | --- | --- |
| 像什么 | 点名册，一个一个点 | 站队，没轮到的继续等 |
| 什么时候停 | 名单点完自动停 | 条件变“错”才停 |
| 例子 | `for i in range(6)` | `while True` + `break` |

### B6. `break`：喊停！

```python
if guess == secret:
    print("You got it!")
    break
```

- `break` 就是“跳出循环，不玩了”。复读机立刻停。
- 它一般躲在 `if` 里面：**如果**满足条件，**就**停。猜中了就停，撞墙了就停，按 `q` 了就停。
- 贪吃蛇里有 3 个 `break`：撞墙、咬到自己、按 `q`。你现在能回去找出来了吗？

### 一句话总结

- `if / elif / else` 是三岔路口：条件答“对”走哪条，答“错”走哪条。
- `for` 是点名册：有几个点几个，点完收工。
- `while` 是站队：条件一天是“对”，就一直等，`break` 一喊就散。

---

## C. 大挑战（从 ⭐ 到 🚀）

规则：一次只改一点点，改完马上运行。每次运行都用：

```bash
python3 guess.py
```

### ⭐ 挑战 1 - 换范围（必做，2 分钟）

把 1 到 20 改成 1 到 100，变成真正的“百里挑一”。

- 要改哪里：两处。`randint(1, 20)` 改成 `randint(1, 100)`，`print` 里那句英文也改成 `1 and 100`。
- 成功：提示变成 1 到 100，还能正常玩。用中间数去猜，最多 7 次猜中。
- 提示：漏改一处会怎样？试试看，电脑的提示和实际不一样，好玩吧。

### ⭐⭐ 挑战 2 - 只有 6 次机会（推荐，学 `for`）

现在可以无限猜，太简单了。改成只有 6 次机会，用完就公布答案。

把 `while True:` 那整段换成：

```python
secret = randint(1, 20)
for tries in range(1, 7):
    guess = int(input("Your guess: "))
    if guess == secret:
        print("You got it!")
        break
    elif guess < secret:
        print("Too small, go bigger!")
    else:
        print("Too big, go smaller!")
else:
    print("No more tries! The number was:", secret)
```

新东西只有两样：

1. `range(1, 7)` 变出 1、2、3、4、5、6，正好 6 次。`tries` 自动从 1 数到 6。
2. `for...else`：`for` 点完名、一次都没 `break`（一次都没猜中），就做 `else` 的事，公布答案。猜中过（`break` 过），`else` 就不做了。

成功：6 次内猜中就欢呼，用完 6 次就看到答案。可以故意输一次，看看答案那句。

### ⭐⭐⭐ 挑战 3 - 难度选择（练 `if`）

开局让玩家选难度：简单（1–20，无限次）、困难（1–100，6 次）。

开头加这几行：

```python
level = input("Easy or hard? (e/h): ")
if level == "h":
    secret = randint(1, 100)
else:
    secret = randint(1, 20)
print("Secret number is ready!")
```

- 成功：输 `h` 就是 1–100，输别的都是 1–20。两种都能玩。
- 想一想：为什么这里用 `if...else` 就够了，不用 `elif`？（只有两种情况！）

### ⭐⭐⭐ 挑战 4 - “很接近了！”提示（练 `and`）

猜得差一点点时（差 2 以内），多给一句鼓励。需要一个新符号：`and`（并且）。

在 `elif` 和 `else` 之间加：

```python
elif guess < secret and secret - guess <= 2:
    print("Very close! A little bigger!")
elif guess > secret and guess - secret <= 2:
    print("Very close! A little smaller!")
```

- `and` 两边都得答“对”，整句才是“对”。比如猜 8、答案 10：`8 < 10` 对，`10 - 8 <= 2` 对，所以提示“很接近”。
- 成功：差 1、2 的时候看到新提示，差得多还是老提示。
- 注意顺序：这两句要放在普通的 `Too small / Too big` **前面**，不然轮不到它们（前面的先中了）。

### ⭐⭐⭐⭐ 挑战 5 - 倒数和加油（练 `for` 打印）

开局倒数 3、2、1，猜错时显示还剩几次。用 `for` + `range` 写，不许一个一个 `print`。

```python
for n in range(3, 0, -1):
    print(n)
print("Go!")
```

- `range(3, 0, -1)` 是“从 3 数到 1，每次数完减 1”。第三个数 `-1` 是步子（往反方向走）。
- 成功：开局看到 3、2、1、Go!，猜错时能看到剩余次数。
- 再进一步：把这个倒数加进挑战 2 的 6 次机会版里。

### 🚀 终极挑战 6 - 回到贪吃蛇：给分数配一句话（选做）

打开第 1 课的 `snake.py`，在打印分数后面加判断：

```python
score = len(snake_body) - 1
print("Score:", score)
if score >= 5:
    print("You are a snake master!")
elif score >= 2:
    print("Nice! Keep going!")
else:
    print("Good start!")
```

- 成功：0–1 分看到鼓励，2–4 分看到表扬，5 分以上看到“大师”称号。玩一局验证三种都出现过。
- 意义：你把今天学的 `if` 用回了真正的游戏里。这就是程序员每天做的事。

---

## 怎么做算成功

- [ ] A 部分：我能自己运行 `guess.py` 并猜中一次
- [ ] B 部分：我能说出 `=` 和 `==` 的区别，`for` 和 `while` 分别什么时候用
- [ ] B 部分：我能在 `snake.py` 里指出 1 个 `if`、1 个 `for`、1 个 `while`
- [ ] C 部分：我至少完成了挑战 1 + 任意 1 个（推荐挑战 2）
- [ ] 我只改了一点点就运行一次，没有一次改 10 处

全部打勾？太厉害了！判断和循环是编程的一半，你已经拿下一半了。

## 下一步

- 想练手感，把 [[programming-lessons-zh/第00课-Linux和VSCode基础/练习/你好世界练习|你好世界练习]] 里的 `print` 改成 `for` 打印 3 遍。
- 想继续改游戏，去做挑战 6，把新本领用回贪吃蛇。
- 下一课我们学**盒子（变量）和字（字符串）**：名字、分数、血条是怎么存的。

## 附录：常见报错

| 你看到的 | 意思 | 怎么办 |
| --- | --- | --- |
| `IndentationError: expected an indented block` | `if` 后面没缩进 | 冒号下一行前面空 4 个格子（按 `Tab` 或 4 下空格），整课统一用一种 |
| `SyntaxError: invalid syntax` 指着 `if` 那行 | 忘记冒号 `:` | `if...`、`elif...`、`else`、`for...`、`while...` 行尾都要有 `:` |
| 程序好像没反应，一直等输入 | `input()` 在等你打字 | 输个数字按回车，不是死机 |
| 猜了很多次都不停，停不下来 | 死循环（`break` 没写或条件永远是“对”） | 按 `Ctrl + C` 强制停，再检查 `break` 在不在 `if` 里面 |
| `ValueError: invalid literal for int()` | 在 `Your guess:` 输入了字母 | 只输数字，比如 `10` |
| `NameError: name ... is not defined` | 盒子名字打错了 | 把报错的名字和你定义的地方一个字母一个字母对一遍 |
| 6 次机会版直接公布答案 | `for...else` 的缩进错了，`else` 对齐了 `if` | `else` 要和 `for` 对齐（顶格），不是和 `if` 对齐 |
