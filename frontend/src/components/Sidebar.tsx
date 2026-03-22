import { useEffect, useState } from "react";
import { getConversations, createConversation } from "../api/api";

export default function Sidebar({ onSelect }: any) {
    const [list, setList] = useState<any[]>([]);
    const [name, setName] = useState("");

    const load = async () => {
        const res = await getConversations();
        setList(res.data);
    };

    useEffect(() => {
        load();
    }, []);

    const create = async () => {
        await createConversation({
            name,
            profile: "默认画像"
        });
        setName("");
        load();
    };

    return (
        <div className="sidebar">
            <h3>相亲对象</h3>

            <div className="create-box">
                <input
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="名字"
                />
                <button onClick={create}>创建</button>
            </div>

            {list.map((c) => (
                <div
                    key={c.id}
                    className="conv-item"
                    onClick={() => onSelect(c)}
                >
                    {c.name}
                </div>
            ))}
        </div>
    );
}