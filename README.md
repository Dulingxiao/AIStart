# AIStart

AIStart 是一个面向前后端一体项目的 AI 冷启动母版仓库。

它提供三层基础能力：
- `.ai/` 作为唯一可信的项目上下文源
- `AGENTS.md` / `CLAUDE.md` / `codex-prompt.md` 作为跨工具桥接入口
- 最小可运行的全栈骨架与治理脚本，帮助项目从第一天开始就不跑偏

## V1 范围

- canonical context 目录结构
- bridge files 读取约定
- 最小 FastAPI + Next.js 骨架
- task / ADR / iteration / drift 治理脚本

## 本地开发

```bash
uv sync --group dev
uv run python -m pytest -q
```
