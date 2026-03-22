import { useState } from "react";
import { sendMessage } from "../api/api";

export default function ChatPanel({
    conversation,
    setAnalysis,
    setStage,
    setScore
}: any) {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState<any[]>([]);

    const send = async () => {
        if (!conversation) return;

        const res = await sendMessage({
            conversation_id: conversation.id,
            message: input
        });

        setMessages([
            ...messages,
            { role: "target", content: input },
            { role: "ai", content: res.data.reply }
        ]);

        setAnalysis(res.data.analysis);
        setStage(res.data.stage);
        setScore(res.data.score);

        setInput("");
    };

    return (
        <div className="chat-panel">
            <div className="chat-history">
                {messages.map((m, i) => (
                    <div key={i} className={`msg ${m.role}`}>
                        {m.content}
                    </div>
                ))}
            </div>

            <div className="chat-input">
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="输入对方的话..."
                />
                <button onClick={send}>发送</button>
            </div>
        </div>
    );
}