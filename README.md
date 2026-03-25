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

## 目录结构

- `.ai/`：唯一可信的项目上下文源
- `AGENTS.md` / `CLAUDE.md` / `codex-prompt.md`：不同 AI 工具的桥接入口
- `apps/api`：最小 FastAPI 应用，内置 `/health`
- `apps/web`：最小 Next.js App Router 页面与 `/api/health`
- `packages/shared-types`：共享类型占位包
- `scripts/`：项目初始化、任务、ADR、迭代、drift check 脚本
- `tests/`：脚手架自身的 contract tests

## 快速开始

安装 Python 依赖并运行测试：

```bash
uv sync --group dev
uv run python -m pytest -q
```

生成一个新项目副本：

```bash
uv run python scripts/init_project.py --name demo-project --output-dir /tmp/aistart-demo
```

做一个最小 API 检查：

```bash
uv run python - <<'PY'
from fastapi.testclient import TestClient
from apps.api.app.main import app
print(TestClient(app).get('/health').json())
PY
```

## `.ai/` 与 bridge files 的关系

- `.ai/` 保存 mission、scope、non-goals、memory、tasks、iterations 等 canonical context
- 根目录 bridge files 只定义读取顺序和工作纪律，不复制完整项目真相
- 任何重要改动后，都应该同步更新 `.ai/tasks/current.md`，并在 `.ai/iterations/` 中补一条迭代记录
- 架构或流程约束变化时，用 `.ai/decisions/` 记录 ADR

## V1 明确不做

- 多 agent orchestration 平台
- 自动 PR review / merge
- 完整自治研发系统
- auth、billing、database、queue 等业务层能力
- 大而全的项目管理平台
