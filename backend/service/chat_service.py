import json
from repository.chat_repo import save_message, get_history
from utils.prompt_builder import build_prompt
from llm.llm_client import call_llm


def process_chat(db, conversation, target_msg):
    # 1. 存对方消息
    save_message(db, conversation.id, "target", target_msg)

    # 2. 获取历史
    history = get_history(db, conversation.id)

    # 3. 构建prompt
    messages = build_prompt(conversation.profile, history, target_msg)

    # 4. 调用AI
    raw_reply = call_llm(messages)

    # 5. 解析JSON（容错）
    try:
        parsed = json.loads(raw_reply)
    except:
        parsed = {
            "analysis": "解析失败",
            "stage": "未知",
            "reply": raw_reply,
            "score": 60
        }

    # 6. 存AI回复
    save_message(db, conversation.id, "ai", parsed["reply"])

    return parsed