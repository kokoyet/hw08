# AI多语言翻译润色Web工具
课程期末综合大作业 hw08
技术路线：大模型云API + Flask网页应用

## 项目简介
面向学生外文作业、论文写作，提供中英日韩多语言互译+4种风格文本润色，基于智谱免费glm-4-flash大模型实现AI翻译能力。

## 目录结构
- translate_app.py：Flask后端主程序
- templates/index.html：前端交互网页
- requirements.txt：Python环境依赖
- report.md：完整项目报告

## 一键本地运行步骤
1. 安装依赖
pip install -r requirements.txt
2. 配置密钥：新建.env文件，填入智谱API Key
```env
ZHIPU_API_KEY=你的完整密钥
ZHIPU_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
MODEL_NAME=glm-4-flash
