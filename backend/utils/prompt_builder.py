SYSTEM_PROMPT = """
你是一个高情商恋爱沟通助手。

目标：
1. 分析对方心理状态
2. 判断关系阶段
3. 给出自然真实的回复

要求：
- 不油腻
- 不模板化
- 像真人聊天

输出JSON格式：
{
    "analysis": "...",
    "stage": "...",
    "reply": "...",
    "score": 0-100
}
"""


def build_prompt(profile, history, target_msg):
    history_text = "\n".join([
        f"{m.role}: {m.content}" for m in history[-10:]
    ])

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"""
对方画像：
{profile}

聊天记录：
{history_text}

对方最新消息：
{target_msg}
"""}
    ]