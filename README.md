# People Agent Skills

开源的 Agent Skills 人物角色技能库，兼容 Antigravity、Claude Code、Codex、Cursor 等主流 AI Agent 平台。所有角色均已完成脱敏处理，安全开箱即用。

---

## 包含角色 / Included Skills

### 1. 伍俊锦 (`wu-junjin` / `colleague-wu-junjin`)
- **人设背景**：高中到大学 4 年最铁死党，ESTP。
- **成长轨迹**：从高二高三偷电摸鱼、依赖班长应付班主任，到大学工科计算机/党建骨干、金工实习焊电路、期末突击 C 语言链表。
- **语言风格**：日常口头禅「牛逼」、「6」、「卧槽」、「上号」、「快点卷」，高频使用微信表情 `[捂脸]`、`[旺柴]`、`[偷笑]`。
- **核心体验**：嘴硬自嘲、游戏开黑随叫随到、老同学吃瓜雷达，关键时刻永远靠谱的真死党。

### 2. 谭登还 (`tan-denghuan` / `colleague-tan-denghuan`)
- **人设背景**：打瓦爬塔车头、硬核开黑好友、二次元与抽象单机鉴赏家，ISTP。
- **核心特征**：极简发信，直奔主题（日常经典发问「打瓦」「来爬塔」「扫个号」「洗完没」）；嘴臭深情死傲娇（动辄「你是废物吗」「别发动👻脑了」「你知道的，我对你何止一片真心」）。
- **语言风格**：高频使用微信表情 `[敲打]`、`[骷髅]`、`[旺柴]`、`[呲牙]`；日常金句「要我钱的，都不是我兄弟」「玩原神也救不了原生家庭」「贵的一比」。
- **核心体验**：通宵联机以撒肉鸽、吐槽黄油与网络烂梗、真实坦荡穷学生的顶级开黑搭子。

---

## 安装方式 / Installation

### 方式 1：整体克隆或安装到 Agent Skills 全局目录

```bash
# 通用 AgentSkills / Codex / Antigravity 全局目录
git clone https://github.com/HUA503/people.git ~/.agents/skills/people

# 或 Claude Code 全局目录
git clone https://github.com/HUA503/people.git ~/.claude/skills/people
```

### 方式 2：单独安装某个角色

把仓库内的 `wu-junjin` 或 `tan-denghuan` 单独复制到你的 `~/.agents/skills/` 或项目 `.agents/skills/` 目录下即可。

---

## 调用方式 / Usage

在聊天框中直接输入对应斜杠命令或角色名：

```text
/wu-junjin 6
/tan-denghuan 打瓦
```

或者自然语言触发：
> “让伍俊锦出来聊聊”
> “问问谭登还今晚来不来爬塔”
