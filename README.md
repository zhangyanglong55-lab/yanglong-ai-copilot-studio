# Yanglong AI Copilot Studio

面向 AI 产品设计、AIGC 商业化与 Agent 工作流的中文智能工作台，由 **Zhang Yanglong** 维护。

## 功能

- 中文 AI Copilot 对话界面
- GPT-4o / GPT-4o mini 模型切换
- AI 产品与 Agent 场景专属指令
- 文件、搜索、代码解释器等 OpenAI 工具能力

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
streamlit run app.py
```

维护者：[Zhang Yanglong](https://github.com/zhangyanglong55-lab)

## 来源与许可

基于 [dKosarevsky/AI-Talks](https://github.com/dKosarevsky/AI-Talks) 改造，新增独立中文入口、个人品牌界面、模型设置和场景提示词。原项目与本项目依据仓库内 MIT License 使用。
