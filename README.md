# AIStart: Start fast. Drift less.

> 给独立开发者和小团队的 AI-native 全栈冷启动母版仓库。  
> 它不只是帮你起一个项目，而是从第一天开始统一上下文、边界、任务和迭代记录。

[快速开始](#快速开始) | [给 AI 的读取顺序](#给-ai-的读取顺序) | [为什么不是普通 Starter](#为什么不是另一个普通-starter) | [English Summary](#english-summary)

如果你经常用 Claude、Codex、Cursor 或其他 AI 工具开新项目，AIStart 解决的不是“怎么再多生成几百行代码”，而是“怎么别把项目越写越歪”。

## 为什么不是另一个普通 Starter

AI 写代码越来越快，但新项目还是常死在四件事上：

- 第一轮 prompt 就开始散，项目目标和边界没人持续校准
- 不同 AI 工具读到的不是同一套事实，越协作越冲突
- 项目跑几轮后，任务、实现、决策记录开始脱节
- 普通 starter 只帮你生成目录和依赖，不帮你管理项目纪律

AIStart 的核心不是“多一个模板”，而是把 **canonical context** 变成仓库的一等公民。  
你拿到的不只是代码骨架，还有一套让人和 AI 读同一份项目真相的起盘方式。

| 普通 starter | AIStart |
| --- | --- |
| 起目录、起依赖 | 起目录、起依赖，同时起 canonical context |
| 每个工具各读各的 prompt | 多个工具统一从 [`.ai/`](.ai/) 读取 source of truth |
| 做完改动容易没人记账 | task / iteration / ADR 都有固定落点 |
| 代码能起，但项目容易漂 | 用 mission / scope / non-goals 做硬护栏 |

## 你实际拿到什么

### 1. Canonical context

[`.ai/`](.ai/) 是整个仓库唯一可信的项目事实源，里面已经分好了层：

- [`.ai/project/`](.ai/project/)：mission、scope、non-goals、success criteria、current phase
- [`.ai/context/`](.ai/context/)：产品背景、技术约束、角色画像、技术栈决策
- [`.ai/memory/`](.ai/memory/)：稳定事实、anti-drift 规则、开放问题
- [`.ai/tasks/`](.ai/tasks/)：当前任务、backlog、done
- [`.ai/iterations/`](.ai/iterations/)：每次有意义的迭代记录
- [`.ai/decisions/`](.ai/decisions/)：架构和流程决策记录

### 2. Bridge files

根目录的 [AGENTS.md](AGENTS.md)、[CLAUDE.md](CLAUDE.md)、[codex-prompt.md](codex-prompt.md) 都只做一件事：

- 告诉不同 AI 工具先读什么
- 把它们指回同一份 canonical source
- 明确“改完代码后还要更新哪些记录”

它们不是第二套世界观，只是入口。

### 3. Minimal fullstack scaffold

这个仓库已经自带最小可运行的全栈骨架：

- [`apps/api`](apps/api)：FastAPI，内置 `/health`
- [`apps/web`](apps/web)：Next.js App Router，内置页面和 `/api/health`
- [`packages/shared-types`](packages/shared-types)：共享类型占位包
- [`tests`](tests)：脚手架 contract tests，不是空壳项目

### 4. Governance scripts

脚本层已经给你准备好了最小治理工具：

- [`scripts/init_project.py`](scripts/init_project.py)：按项目名生成一个干净副本
- [`scripts/new_task.py`](scripts/new_task.py)：往 current task 里追加结构化任务
- [`scripts/new_adr.py`](scripts/new_adr.py)：创建编号 ADR
- [`scripts/log_iteration.py`](scripts/log_iteration.py)：写入一条迭代日志
- [`scripts/drift_check.py`](scripts/drift_check.py)：检查项目有没有偏离 mission / scope / non-goals

## 快速开始

### 1. 安装依赖

```bash
uv sync --group dev
```

你会得到一个可运行的 Python 开发环境和锁定依赖。

### 2. 跑测试，确认这不是 PPT 项目

```bash
uv run python -m pytest -q
```

当前仓库应该通过全部脚手架测试。

### 3. 生成一个新项目副本

```bash
uv run python scripts/init_project.py --name my-app --output-dir /tmp/aistart-demo
```

这会生成 `/tmp/aistart-demo/my-app`，并把仓库里的 `AIStart` 占位符替换成你的项目名。

### 4. 做一个最小 API 检查

```bash
uv run python - <<'PY'
from fastapi.testclient import TestClient
from apps.api.app.main import app
print(TestClient(app).get("/health").json())
PY
```

你应该看到：

```python
{'status': 'ok', 'project': 'AIStart'}
```

## 给 AI 的读取顺序

如果你是进入这个仓库的 AI agent，先停一下，按这个顺序读：

1. [`.ai/project/mission.md`](.ai/project/mission.md)
2. [`.ai/project/scope.md`](.ai/project/scope.md)
3. [`.ai/project/non-goals.md`](.ai/project/non-goals.md)
4. [`.ai/context/technical-constraints.md`](.ai/context/technical-constraints.md)
5. [`.ai/memory/stable-facts.md`](.ai/memory/stable-facts.md)
6. [`.ai/memory/anti-drift.md`](.ai/memory/anti-drift.md)
7. [`.ai/tasks/current.md`](.ai/tasks/current.md)

然后遵守这几条规则：

- 只认 [`.ai/`](.ai/) 为 canonical source of truth
- [AGENTS.md](AGENTS.md)、[CLAUDE.md](CLAUDE.md)、[codex-prompt.md](codex-prompt.md) 只是 bridge，不是第二套真相
- 做完有意义的改动后，更新 current task，并在 [`.ai/iterations/`](.ai/iterations/) 里补一条记录
- 如果改了架构或流程约束，去 [`.ai/decisions/`](.ai/decisions/) 写 ADR

这段既是给 AI 的，也是给人的。它表达的是：这个仓库不是靠长 prompt 硬撑，而是有结构化约束。

## 适合谁

AIStart 适合：

- 高频启动新项目的独立开发者
- 同时用多个 AI 编程工具的人
- 想把项目上下文、任务和迭代记录规范起来的小团队
- 想从第一天开始就把“项目真相”和“代码实现”绑在一起的人

## 不适合谁

如果你要的是下面这些，AIStart 不是你的答案：

- 一键全自治研发平台
- 自带 auth / billing / database / queue / deploy 全家桶的大模板
- 面向大企业的大而全脚手架
- “让 AI 自动替代产品经理和架构师”的幻觉型系统

## Non-Goals

AIStart V1 明确不做这些事：

- multi-agent orchestration platform
- auto PR review / auto merge
- 默认内建 auth / billing / database / queue 方案
- 复杂插件系统
- 项目管理平台化
- “一切交给 AI 自动搞定”的自治承诺

克制不是缺点。对一个 starter 来说，边界清楚比功能堆满更重要。

## 仓库结构

```text
AIStart/
├─ .ai/                 # canonical context
├─ apps/
│  ├─ api/              # FastAPI scaffold
│  └─ web/              # Next.js scaffold
├─ packages/            # shared packages
├─ scripts/             # bootstrap and governance
├─ tests/               # scaffold contract tests
├─ AGENTS.md
├─ CLAUDE.md
├─ codex-prompt.md
└─ README.md
```

如果你想看更细的结构职责，继续读 [docs/architecture/overview.md](docs/architecture/overview.md)。

## Next

接下来最值得做的不是继续堆功能，而是把这套东西放进真实项目里打磨几轮：

- 用第一个下游项目 dogfood `init_project.py`
- 只在真实使用后，再决定要不要抽 shared lint / CI presets
- 继续优化生成项目的默认内容，而不是过早做大而全模板

## English Summary

AIStart is an AI-native fullstack starter for solo builders and small teams.

It is built for people who use Claude, Codex, Cursor, or other AI coding tools to start projects quickly, but want much less context drift as the project grows.

The core idea is simple:

- keep [`.ai/`](.ai/) as the canonical context source
- let bridge files point every AI tool back to the same project truth
- ship a minimal FastAPI + Next.js scaffold
- keep tasks, iteration logs, and ADRs in the repo from day one

AIStart is not an autonomous multi-agent platform. It is a disciplined starting point for AI-assisted product development.
