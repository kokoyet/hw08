import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI

# 加载密钥
load_dotenv()
api_key = os.getenv("ZHIPU_API_KEY")
base_url = os.getenv("ZHIPU_BASE_URL")
model = os.getenv("MODEL_NAME")

app = Flask(__name__)

# 初始化免费大模型
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base=base_url,
    model_name=model,
    temperature=0.2
)

# 翻译润色核心函数
def translate_polish(text, source_lang, target_lang, mode):
    prompt = f"""
你是专业多语言翻译与文本润色助手。
原文语言：{source_lang}
目标语言：{target_lang}
润色模式：{mode}
模式说明：
1.标准翻译：准确直译，语句通顺
2.学术润色：适合论文作业，用词严谨、逻辑规范
3.口语简化：日常聊天短句，通俗易懂
4.精简压缩：缩短原文，保留核心意思

原文内容：
{text}

输出格式：
【翻译结果】
xxx
【润色后文本】
xxx
【重点词汇释义】
逐条列出文中专业/难词解释
"""
    res = llm.invoke(prompt)
    return res.content

# 首页页面
@app.route("/")
def index():
    return render_template("index.html")

# 翻译接口
@app.route("/translate", methods=["POST"])
def do_translate():
    data = request.get_json()
    text = data.get("text", "")
    src = data.get("source")
    dst = data.get("target")
    mode = data.get("mode")
    if not text:
        return jsonify({"result": "请输入需要翻译的文本"})
    ans = translate_polish(text, src, dst, mode)
    return jsonify({"result": ans})

if __name__ == "__main__":
    app.run(debug=True)