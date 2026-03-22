export default function ScorePanel({ analysis, stage, score }: any) {
    return (
        <div className="score-panel">
            <h3>评估</h3>

            <p><b>当前阶段：</b>{stage}</p>
            <p><b>评分：</b>{score}</p>

            <h4>分析</h4>
            <div className="analysis-box">
                {analysis}
            </div>
        </div>
    );
}