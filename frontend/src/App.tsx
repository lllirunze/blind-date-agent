import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatPanel from "./components/ChatPanel";
import ScorePanel from "./components/ScorePanel";
import "./styles.css";

function App() {
  const [currentConv, setCurrentConv] = useState<any>(null);
  const [analysis, setAnalysis] = useState("");
  const [stage, setStage] = useState("");
  const [score, setScore] = useState(0);

  return (
    <div className="app">
      <Sidebar onSelect={setCurrentConv} />

      <ChatPanel
        conversation={currentConv}
        setAnalysis={setAnalysis}
        setStage={setStage}
        setScore={setScore}
      />

      <ScorePanel analysis={analysis} stage={stage} score={score} />
    </div>
  );
}

export default App;