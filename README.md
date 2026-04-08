```markdown
# 毒舌求职顾问 (The Roasting Career Coach) 🚀

这是一个基于 **DeepSeek-V3** 大模型开发的智能求职辅助工具。它不喝鸡汤，只说实话。

## 🌟 项目亮点
- **人格化调教**：内置深度定制的 System Prompt，AI 将扮演一个专业、犀利、毒舌的面试官。
- **双模对话**：支持极简的网页交互界面（基于 Gradio）。
- **实时响应**：采用流式传输技术，回答无需等待。

## 🛠️ 技术栈
- **大模型 API**: DeepSeek-V3 (OpenAI SDK 兼容)
- **后端**: Python 3.10+
- **前端界面**: Gradio
- **环境管理**: python-dotenv

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone [https://github.com/nanagogo/AI-Job-Consultant.git](https://github.com/nanagogo/AI-Job-Consultant.git)
cd AI-Job-Consultant
```

### 2. 安装依赖
```bash
pip install openai gradio python-dotenv
```

### 3. 配置密钥
在项目根目录新建 `.env` 文件，并填入你的 DeepSeek API Key：
```text
OPENAI_API_KEY=sk-你的key
```

### 4. 运行应用
```bash
python app.py
```

## 📖 核心逻辑
项目通过修改 `System Prompt` 实现了 AI 的性格转变，要求 AI 在给出求职建议前必须先指出用户逻辑中的一个短板。这种“先破后立”的模式能更有效地帮助求职者发现真实问题。

---
*本项目仅用于学习 AI 应用开发流转，祝每一位求职者都能在毒舌中进化！*
```

---
