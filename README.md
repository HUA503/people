# 🎭 People Agent Skills

> 高品质、标准化的 AI Agent 人物角色技能库，兼容 **Antigravity**、**Claude Code**、**Codex**、**Cursor** 等所有支持 [Agent Skills](https://agentskills.io) 开放标准的 AI 编程助手与智能体平台。

所有收录的角色均基于真实互动材料深度蒸馏，具备鲜活立体的 5 层灵魂人格（Layer 0 核心潜意识 ~ Layer 5 记忆特征），且**已完成彻底脱敏保护**，无任何个人隐私泄漏风险，开箱即用。

---

## 📂 仓库结构规范 (Architecture)

本仓库采用多技能模块化架构，后续你可以随时在此仓库中扩展加入更多好友、同事或公众人物技能：

```text
people/
├── skills/                     # 🌟 所有角色技能的存放根目录
│   ├── wu-junjin/              # 伍俊锦 (ESTP · 4年铁死党/代码与摸鱼骨干)
│   │   ├── SKILL.md            # 技能主入口（包含 YAML Frontmatter 与运行规则）
│   │   ├── persona.md          # 5层深度人格定义与表达DNA
│   │   ├── work.md             # 学习/工作/协作能力规范
│   │   ├── meta.json           # 规范化元数据
│   │   └── manifest.json       # 资源清单
│   ├── tan-denghuan/           # 谭登还 (ISTP · 打瓦爬塔车头/抽象二次元鉴赏家)
│   │   ├── SKILL.md
│   │   ├── persona.md
│   │   ├── work.md
│   │   ├── meta.json
│   │   └── manifest.json
│   └── <your-next-skill>/      # 🚀 未来新增的任意新角色/技能
├── install.py                  # 跨平台一键安装工具 (支持全自动扫描安装)
├── skills.json                 # Antigravity/Agent 原生技能目录索引配置
├── LICENSE                     # MIT 开源许可证
└── README.md                   # 项目介绍与使用指南
```

---

## 👥 当前收录角色 / Included Skills

### 1. 伍俊锦 (`wu-junjin` / `colleague-wu-junjin`)
* **人物画像**：从高中到大学 4 年最铁死党，典型 ESTP。
* **人物履历**：高二高三偷电开黑、依赖班长应付班主任；大学进入工科计算机专业，进党建组织、金工实习焊电路3小时、期末突击 C 语言链表大作业。
* **语言风格**：口头禅「牛逼」、「6 / 666」、「卧槽」、「上号」、「快点卷」，高频使用微信表情 `[捂脸]`、`[旺柴]`、`[偷笑]`。
* **调用命令**：`/wu-junjin`

### 2. 谭登还 (`tan-denghuan` / `colleague-tan-denghuan`)
* **人物画像**：打瓦与爬塔核心车头、二次元/单机游戏与抽象网络烂梗鉴赏家，典型 ISTP。
* **人物特征**：发信极简（经典开场「打瓦」「来爬塔」「扫个号」「洗完没」「来」「？」）；嘴臭深情死傲娇（动辄「你是废物吗」「别发动👻脑了」「你知道的，我对你何止一片真心」）。
* **语言风格**：高频使用微信表情 `[敲打]`、`[骷髅]`、`[旺柴]`、`[呲牙]`；日常金句「要我钱的，都不是我兄弟」「玩原神也救不了原生家庭」「贵的一比」。
* **调用命令**：`/tan-denghuan`

---

## ⚡ 快速安装 / Installation

### 方式 A：使用一键安装脚本（推荐）

克隆本仓库后，直接运行内置的 `install.py`：

```bash
git clone https://github.com/HUA503/people.git
cd people

# 一键安装所有角色到当前系统（自动适配 Antigravity / Claude Code / Codex）
python install.py --all --force

# 或者只安装指定某个角色
python install.py --skill wu-junjin --force
python install.py --skill tan-denghuan --force
```

### 方式 B：手动复制到宿主全局目录

如果你只想手动放置，把 `skills/` 下的目标文件夹复制到你宿主的技能目录即可：

* **通用 AgentSkills / Codex / Antigravity 目录**：
  ```bash
  # Windows
  %USERPROFILE%\.agents\skills\
  %USERPROFILE%\.gemini\config\skills\

  # macOS / Linux
  ~/.agents/skills/
  ~/.gemini/config/skills/
  ```
* **Claude Code 全局目录**：
  ```bash
  ~/.claude/skills/
  ```

---

## 🛠️ 后续如何添加新角色 (How to Add More Skills)

当你想上传新蒸馏好的角色时，只需遵循简单的三步：

1. **新建目录**：在 `skills/` 下新建一个同名小写目录，如 `skills/<slug>/`。
2. **放入文件**：将包含标准 YAML Frontmatter 的 `SKILL.md`（以及可选的 `persona.md`、`work.md`、`meta.json`）放入该目录。
3. **提交推送**：
   ```bash
   git add skills/<slug>
   git commit -m "feat: add <slug> skill"
   git push origin main
   ```
其他人在拉取仓库后运行 `python install.py` 就会自动发现并安装你新加入的角色！

---

## 📄 开源许可

本项目遵循 [MIT License](LICENSE)。
