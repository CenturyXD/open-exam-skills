"""
Quiz Skill - Convert JSON quiz to interactive HTML
Pure frontend converter - no AI/LLM required
"""

import json
import argparse
import shutil
from pathlib import Path
from typing import Optional
from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")


def find_katex_dist() -> Optional[Path]:
    npm_cache = Path.home() / '.npm' / '_npx'
    candidates = []

    if npm_cache.exists():
        candidates.extend(npm_cache.glob('*/node_modules/katex/dist'))

    local_node_modules = Path.cwd() / 'node_modules' / 'katex' / 'dist'
    if local_node_modules.exists():
        candidates.append(local_node_modules)

    if not candidates:
        return None

    return max(candidates, key=lambda path: path.stat().st_mtime)


def get_katex_assets() -> dict:
    dist = find_katex_dist()
    if dist:
        css_path = dist / 'katex.min.css'
        js_path = dist / 'katex.min.js'
        auto_render_path = dist / 'contrib' / 'auto-render.min.js'
        if css_path.exists() and js_path.exists() and auto_render_path.exists():
            css = css_path.read_text(encoding='utf-8')
            katex_js = js_path.read_text(encoding='utf-8')
            auto_render_js = auto_render_path.read_text(encoding='utf-8')
            return {
                'styles': f"<style>{css}</style>",
                'scripts': f"<script>{katex_js}</script>\n<script>{auto_render_js}</script>",
                'fonts_dir': dist / 'fonts'
            }

    version = '0.16.18'
    return {
        'styles': (
            f"<link rel=\"stylesheet\" "
            f"href=\"https://cdn.jsdelivr.net/npm/katex@{version}/dist/katex.min.css\">"
        ),
        'scripts': (
            f"<script src=\"https://cdn.jsdelivr.net/npm/katex@{version}/dist/katex.min.js\"></script>\n"
            f"<script src=\"https://cdn.jsdelivr.net/npm/katex@{version}/dist/contrib/auto-render.min.js\"></script>"
        ),
        'fonts_dir': None
    }


def ensure_katex_fonts(output_path: str, fonts_dir: Optional[Path]) -> None:
    if not fonts_dir or not fonts_dir.exists():
        return

    output_dir = Path(output_path).resolve().parent
    dest_dir = output_dir / 'fonts'
    dest_dir.mkdir(parents=True, exist_ok=True)

    for font_file in fonts_dir.glob('*'):
        if font_file.is_file():
            shutil.copy2(font_file, dest_dir / font_file.name)

    logger.info(f"✓ KaTeX fonts copied to: {dest_dir}")


def load_quiz_data(json_path: str) -> dict:
    """Load quiz data from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle both array format and object format
    if isinstance(data, list):
        return {
            "title": "Quiz",
            "questions": data,
            "banks": [{
                "id": "set1",
                "title": "Quiz",
                "questions": data
            }]
        }

    # Normalize banks: prefer explicit banks, else wrap questions
    if data.get("banks"):
        return data

    questions = data.get("questions", [])
    data["banks"] = [{
        "id": "set1",
        "title": data.get("title", "Quiz"),
        "questions": questions
    }]
    return data


def generate_html(quiz_data: dict, katex_assets: dict) -> str:
    """Generate interactive quiz HTML."""

    title = quiz_data.get("title", "Quiz")
    banks = quiz_data.get("banks") or [{
        "id": "set1",
        "title": title,
        "questions": quiz_data.get("questions", [])
    }]
    questions = banks[0].get("questions", [])
    total_questions = len(questions)

    # Convert banks/questions to JSON string for embedding
    banks_json = json.dumps(banks, ensure_ascii=False)
    questions_json = json.dumps(questions, ensure_ascii=False)

    katex_styles = katex_assets['styles']
    katex_scripts = katex_assets['scripts']

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: #ffffff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 24px 16px 32px;
        }}

        .quiz-container {{
            background: white;
            border-radius: 16px;
            box-shadow: none;
            max-width: 520px;
            width: 100%;
            padding: 18px 16px 20px;
            display: flex;
            flex-direction: column;
            min-height: 640px;
        }}

        .quiz-header {{
            text-align: left;
            margin-bottom: 16px;
        }}

        .quiz-title {{
            font-size: 22px;
            font-weight: 600;
            color: #232323;
            margin-bottom: 4px;
        }}

        .quiz-subtitle {{
            font-size: 13px;
            color: #9d9d9d;
        }}

        .progress-text {{
            text-align: left;
            font-size: 13px;
            color: #9d9d9d;
            margin-bottom: 12px;
            font-weight: 500;
        }}

        .question-text {{
            font-size: 16px;
            font-weight: 500;
            color: #2a2a2a;
            margin-bottom: 16px;
            line-height: 1.5;
        }}

        .options {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 16px;
            max-height: 400px;
            overflow-y: auto;
            padding-right: 4px;
        }}

        .options::-webkit-scrollbar {{
            width: 6px;
        }}

        .options::-webkit-scrollbar-track {{
            background: #f0f0f0;
            border-radius: 3px;
        }}

        .options::-webkit-scrollbar-thumb {{
            background: #c0c0c0;
            border-radius: 3px;
        }}

        .options::-webkit-scrollbar-thumb:hover {{
            background: #a0a0a0;
        }}

        .option {{
            display: flex;
            align-items: center;
            padding: 14px 16px;
            border: 1px solid #f0f0f0;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
            background: #f8f8f8;
        }}

        .option:hover:not(.selected):not(.disabled) {{
            border-color: #e6e6e6;
            background: #f6f6f6;
        }}

        .option.selected {{
            border-color: #d0d0d0;
            background: #dedede;
        }}

        .option.correct,
        .option.wrong {{
            border-color: #f0f0f0;
            background: #f8f8f8;
        }}

        .option.disabled {{
            cursor: default;
        }}

        .option-label {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: 500;
            margin-right: 10px;
            flex-shrink: 0;
            color: #9d9d9d;
            width: 22px;
        }}

        .option.selected .option-label {{
            color: #3a3a3a;
        }}

        .option.disabled .option-text {{
            color: #bdbdbd;
        }}

        .option.disabled .option-label {{
            color: #bdbdbd;
        }}

        .option-text {{
            flex: 1;
            font-size: 15px;
            color: #3a3a3a;
        }}


        .feedback-card {{
            padding: 14px 16px;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            opacity: 0;
            transform: translateY(8px);
            transition: opacity 0.25s ease, transform 0.25s ease;
        }}

        .feedback-card.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        .feedback-card.correct {{
            background: #bfeacb;
        }}

        .feedback-card.wrong {{
            background: #fff7f7;
        }}

        .feedback-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            font-weight: 600;
        }}

        .feedback-header.correct {{
            color: #697b6e;
        }}

        .feedback-header.wrong {{
            color: #a42d22;
        }}

        .feedback-icon {{
            font-size: 16px;
            font-weight: 600;
        }}

        .feedback-answer {{
            font-size: 15px;
            color: #2a2a2a;
        }}

        .feedback-text {{
            font-size: 13px;
            line-height: 1.5;
        }}

        .feedback-card.correct .feedback-text {{
            color: #444443;
        }}

        .feedback-card.wrong .feedback-text {{
            color: #2e2e2f;
        }}

        .buttons {{
            display: flex;
            justify-content: space-between;
            gap: 12px;
            margin-top: 24px;
            min-height: 52px;
        }}

        .btn {{
            padding: 10px 22px;
            border-radius: 999px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            border: none;
            transition: all 0.2s ease;
            min-width: 120px;
        }}

        .btn-secondary {{
            background: #ffffff;
            color: #6b7280;
            border: 1px solid #e2e2e2;
        }}

        .btn-secondary:hover:not(:disabled) {{
            background: #e5e5e5;
        }}

        .btn-secondary:disabled {{
            opacity: 0.4;
            cursor: not-allowed;
        }}

        .btn-primary {{
            background: #424cf7;
            color: white;
        }}

        .btn-primary:hover:not(:disabled) {{
            opacity: 0.95;
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(66, 76, 247, 0.25);
        }}

        .btn-primary:disabled {{
            opacity: 0.4;
            cursor: not-allowed;
        }}


        .completion-container {{
            text-align: center;
            display: none;
        }}

        .completion-container.show {{
            display: block;
        }}

        .completion-icon {{
            font-size: 64px;
            margin-bottom: 20px;
        }}

        .completion-title {{
            font-size: 28px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 12px;
        }}

        .completion-subtitle {{
            font-size: 16px;
            color: #666;
            margin-bottom: 30px;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 30px;
        }}

        .stat-card {{
            background: #f8f9ff;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
        }}

        .stat-label {{
            font-size: 14px;
            color: #666;
            margin-bottom: 8px;
        }}

        .stat-value {{
            font-size: 28px;
            font-weight: 600;
            color: #1a1a1a;
        }}

        .stat-card.score {{
            grid-column: 1 / -1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}

        .stat-card.score .stat-label {{
            color: rgba(255, 255, 255, 0.9);
        }}

        .stat-card.score .stat-value {{
            color: white;
        }}

        .completion-buttons {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: stretch;
            gap: 12px;
            max-width: 320px;
            margin: 0 auto;
        }}

        .completion-buttons .btn {{
            width: 100%;
        }}

        .completion-buttons .btn-primary {{
            order: -1;
            font-size: 16px;
            padding: 14px 20px;
        }}

        .wrong-review {{
            text-align: left;
            margin: 24px 0 8px;
        }}

        .wrong-review-title {{
            font-size: 18px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 12px;
        }}

        .wrong-empty {{
            background: #ecfdf3;
            color: #166534;
            border: 1px solid #bbf7d0;
            border-radius: 12px;
            padding: 14px 16px;
            font-size: 14px;
        }}

        .wrong-item {{
            background: #fff;
            border: 1px solid #f1d0d0;
            border-left: 4px solid #ef4444;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 10px;
        }}

        .wrong-item-q {{
            font-size: 14px;
            font-weight: 600;
            color: #1f2430;
            margin-bottom: 8px;
            line-height: 1.5;
        }}

        .wrong-meta {{
            font-size: 13px;
            line-height: 1.55;
            margin-bottom: 4px;
        }}

        .wrong-meta .label {{
            color: #6b7280;
        }}

        .wrong-meta.yours {{
            color: #b91c1c;
        }}

        .wrong-meta.correct {{
            color: #15803d;
        }}

        .wrong-explain {{
            margin-top: 8px;
            font-size: 13px;
            color: #374151;
            background: #f9fafb;
            border-radius: 8px;
            padding: 8px 10px;
        }}

        .hint-toggle {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 13px;
            color: #4e4e4e;
            background: none;
            border: none;
            padding: 0;
            cursor: pointer;
        }}

        .hint-toggle .chevron {{
            display: inline-block;
            transition: transform 0.2s ease;
        }}

        .hint-toggle.open .chevron {{
            transform: rotate(180deg);
        }}

        .hint-panel {{
            padding: 12px 14px;
            background: #ebecf8;
            border-radius: 12px;
            display: none;
            opacity: 0;
            transform: translateY(6px);
            transition: opacity 0.2s ease, transform 0.2s ease;
        }}

        .hint-panel.show {{
            display: block;
            opacity: 1;
            transform: translateY(0);
        }}

        .hint-title {{
            font-weight: 600;
            font-size: 13px;
            color: #4e4e4e;
            margin-bottom: 6px;
        }}

        .hint-text {{
            font-size: 13px;
            color: #474749;
            line-height: 1.5;
        }}

        .hint-slot {{
            min-height: 72px;
        }}

        .quiz-footer {{
            margin-top: auto;
        }}

        .question-container {{
            display: none;
        }}

        .question-container.active {{
            display: block;
        }}
    </style>
    {katex_styles}
</head>
<body>
    <div class="quiz-container">
        <div class="quiz-header">
            <div class="quiz-title" id="quiz-title">{title}</div>
            <div class="quiz-subtitle" id="quiz-subtitle">ชุดที่ 1</div>
        </div>

        <div id="quiz-content">
            <!-- Questions will be rendered here -->
        </div>

        <div id="completion-screen" class="completion-container">
            <div class="completion-icon">🎉</div>
            <div class="completion-title">ทำครบแล้ว!</div>
            <div class="completion-subtitle">ดูผลคะแนนของคุณ แล้วกดสร้างควิซใหม่เพื่อเปลี่ยนไปชุดข้อสอบถัดไป</div>

            <div class="stats-grid">
                <div class="stat-card score">
                    <div class="stat-label">คะแนน</div>
                    <div class="stat-value" id="score-value">0/{total_questions}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">ความแม่นยำ</div>
                    <div class="stat-value" id="accuracy-value">0%</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">ถูก</div>
                    <div class="stat-value" id="right-value">0</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">ผิด</div>
                    <div class="stat-value" id="wrong-value">0</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">ข้าม</div>
                    <div class="stat-value" id="skipped-value">0</div>
                </div>
            </div>

            <div class="wrong-review">
                <div class="wrong-review-title">ข้อที่ผิด / ควรทบทวน</div>
                <div id="wrong-list"></div>
            </div>

            <div class="completion-buttons">
                <button class="btn btn-primary" onclick="createNewQuiz()">สร้างควิซใหม่ (ชุดถัดไป)</button>
                <button class="btn btn-secondary" onclick="reviewQuiz()">ทบทวนข้อสอบ</button>
            </div>
        </div>
    </div>

    {katex_scripts}
    <script>
        const quizBanks = {banks_json};
        let currentBankIndex = 0;
        let questions = quizBanks[0].questions.map(q => ({{ ...q, options: [...q.options] }}));
        let totalQuestions = questions.length;
        let currentQuestionIndex = 0;
        let userAnswers = []; // Store user's answers {{questionIndex, selectedIndex, isCorrect}}
        let isReviewMode = false;

        function updateQuizHeader() {{
            const bank = quizBanks[currentBankIndex];
            const titleEl = document.getElementById('quiz-title');
            const subtitleEl = document.getElementById('quiz-subtitle');
            if (titleEl) {{
                titleEl.textContent = bank.title || '{title}';
            }}
            if (subtitleEl) {{
                subtitleEl.textContent = `ชุดที่ ${{currentBankIndex + 1}} / ${{quizBanks.length}} · ข้อสอบใหม่ทั้งชุด`;
            }}
        }}

        function renderMath(target) {{
            if (!target || typeof renderMathInElement !== 'function') return;
            renderMathInElement(target, {{
                delimiters: [
                    {{left: '$$', right: '$$', display: true}},
                    {{left: '$', right: '$', display: false}},
                    {{left: '\\(', right: '\\)', display: false}},
                    {{left: '\\[', right: '\\]', display: true}}
                ],
                throwOnError: false
            }});
        }}

        function initQuiz() {{
            renderQuestion();
        }}

        function renderQuestion() {{
            const quizContent = document.getElementById('quiz-content');
            const question = questions[currentQuestionIndex];
            const userAnswer = userAnswers[currentQuestionIndex];

            const isAnswered = userAnswer !== undefined;

            // Determine button states
            const showPrevious = currentQuestionIndex > 0;
            const showNext = isAnswered && currentQuestionIndex < totalQuestions - 1;
            const showFinish = isAnswered && currentQuestionIndex === totalQuestions - 1 && !isReviewMode;
            const showFinishReview = isReviewMode && currentQuestionIndex === totalQuestions - 1;
            const showHint = !!question.hint;

            let optionsHtml = '';
            question.options.forEach((option, index) => {{
                const letter = String.fromCharCode(65 + index); // A, B, C, D

                if (isAnswered) {{
                    if (index === question.correctIndex) {{
                        const correctExplain = question.correctExplanation || question.explanation || '';
                        optionsHtml += `
                            <div class="feedback-card correct show">
                                <div class="feedback-answer">${{letter}}. ${{option}}</div>
                                <div class="feedback-header correct">
                                    <span class="feedback-icon">✓</span>
                                    <span>Right answer</span>
                                </div>
                                <div class="feedback-text">${{correctExplain}}</div>
                            </div>
                        `;
                        return;
                    }}

                    if (!userAnswer.isCorrect && index === userAnswer.selectedIndex) {{
                        const wrongExplain = question.wrongExplanation || question.explanation || '';
                        optionsHtml += `
                            <div class="feedback-card wrong show">
                                <div class="feedback-answer">${{letter}}. ${{option}}</div>
                                <div class="feedback-header wrong">
                                    <span class="feedback-icon">✕</span>
                                    <span>Not quite</span>
                                </div>
                                <div class="feedback-text">${{wrongExplain}}</div>
                            </div>
                        `;
                        return;
                    }}

                    optionsHtml += `
                        <div class="option disabled" data-index="${{index}}">
                            <span class="option-label">${{letter}}.</span>
                            <span class="option-text">${{option}}</span>
                        </div>
                    `;
                    return;
                }}

                const optionClass = index === (userAnswer ? userAnswer.selectedIndex : -1) ? 'option selected' : 'option';
                optionsHtml += `
                    <div class="${{optionClass}}" onclick="selectAnswer(${{index}})" data-index="${{index}}">
                        <span class="option-label">${{letter}}.</span>
                        <span class="option-text">${{option}}</span>
                    </div>
                `;
            }});

            let hintHtml = '';
            if (showHint) {{
                hintHtml = `
                    <button class="hint-toggle" id="hint-toggle" onclick="toggleHint()">
                        <span>Hint</span>
                        <span class="chevron">⌃</span>
                    </button>
                    <div id="hint-panel" class="hint-panel">
                        <div class="hint-title">Hint</div>
                        <div class="hint-text">${{question.hint}}</div>
                    </div>
                `;
            }}

            let buttonsHtml = `
                <div class="quiz-footer">
                    <div class="buttons">
                        <div style="display: flex; gap: 12px;">
                            <button class="btn btn-secondary" onclick="previousQuestion()" ${{showPrevious ? '' : 'disabled'}}>
                                Previous
                            </button>
                        </div>
                        <div>
                            ${{showNext ? '<button class="btn btn-primary" onclick="nextQuestion()">Next</button>' : ''}}
                            ${{showFinish ? '<button class="btn btn-primary" onclick="finishQuiz()">ดูผลคะแนน</button>' : ''}}
                            ${{showFinishReview ? '<button class="btn btn-primary" onclick="finishReview()">กลับหน้าผลคะแนน</button>' : ''}}
                        </div>
                    </div>
                </div>
            `;

            quizContent.innerHTML = `
                <div class="progress-text">${{currentQuestionIndex + 1}} / ${{totalQuestions}}</div>
                <div class="question-text">${{question.question}}</div>
                <div class="options">
                    ${{optionsHtml}}
                </div>
                <div class="hint-slot">
                    ${{hintHtml}}
                </div>
                ${{buttonsHtml}}
            `;
            renderMath(quizContent);
        }}

        function selectAnswer(selectedIndex) {{
            if (isReviewMode || userAnswers[currentQuestionIndex] !== undefined) return;

            const question = questions[currentQuestionIndex];
            const isCorrect = selectedIndex === question.correctIndex;

            // Store the answer
            userAnswers[currentQuestionIndex] = {{
                questionIndex: currentQuestionIndex,
                selectedIndex: selectedIndex,
                isCorrect: isCorrect
            }};

            // Re-render to show feedback
            renderQuestion();

            // After the last question is answered, jump to the score screen
            if (currentQuestionIndex === totalQuestions - 1) {{
                setTimeout(() => finishQuiz(), 650);
            }}
        }}

        function toggleHint() {{
            const hintPanel = document.getElementById('hint-panel');
            const hintToggle = document.getElementById('hint-toggle');
            if (hintPanel) {{
                hintPanel.classList.toggle('show');
            }}
            if (hintToggle) {{
                hintToggle.classList.toggle('open');
            }}
        }}

        function nextQuestion() {{
            if (currentQuestionIndex < totalQuestions - 1) {{
                currentQuestionIndex++;
                renderQuestion();
            }}
        }}

        function previousQuestion() {{
            if (currentQuestionIndex > 0) {{
                currentQuestionIndex--;
                renderQuestion();
            }}
        }}

        function finishQuiz() {{
            showCompletionScreen();
        }}

        function showCompletionScreen() {{
            const quizContent = document.getElementById('quiz-content');
            const completionScreen = document.getElementById('completion-screen');

            // Calculate stats
            const answeredQuestions = userAnswers.filter(a => a !== undefined);
            const correctAnswers = userAnswers.filter(a => a && a.isCorrect).length;
            const wrongAnswers = userAnswers.filter(a => a && !a.isCorrect).length;
            const skipped = totalQuestions - answeredQuestions.length;
            const accuracy = answeredQuestions.length > 0
                ? Math.round((correctAnswers / answeredQuestions.length) * 100)
                : 0;

            // Update stats
            document.getElementById('score-value').textContent = `${{correctAnswers}}/${{totalQuestions}}`;
            document.getElementById('accuracy-value').textContent = `${{accuracy}}%`;
            document.getElementById('right-value').textContent = correctAnswers;
            document.getElementById('wrong-value').textContent = wrongAnswers;
            document.getElementById('skipped-value').textContent = skipped;

            // Render wrong / skipped review
            const wrongList = document.getElementById('wrong-list');
            let reviewHtml = '';
            questions.forEach((q, idx) => {{
                const ans = userAnswers[idx];
                const letter = (i) => String.fromCharCode(65 + i);
                if (!ans) {{
                    reviewHtml += `
                        <div class="wrong-item">
                            <div class="wrong-item-q">ข้อ ${{idx + 1}}. ${{q.question}}</div>
                            <div class="wrong-meta yours"><span class="label">คำตอบของคุณ:</span> ยังไม่ได้ตอบ</div>
                            <div class="wrong-meta correct"><span class="label">เฉลย:</span> ${{letter(q.correctIndex)}}. ${{q.options[q.correctIndex]}}</div>
                            <div class="wrong-explain">${{q.wrongExplanation || q.correctExplanation || q.explanation || ''}}</div>
                        </div>
                    `;
                    return;
                }}
                if (!ans.isCorrect) {{
                    reviewHtml += `
                        <div class="wrong-item">
                            <div class="wrong-item-q">ข้อ ${{idx + 1}}. ${{q.question}}</div>
                            <div class="wrong-meta yours"><span class="label">คำตอบของคุณ:</span> ${{letter(ans.selectedIndex)}}. ${{q.options[ans.selectedIndex]}}</div>
                            <div class="wrong-meta correct"><span class="label">เฉลย:</span> ${{letter(q.correctIndex)}}. ${{q.options[q.correctIndex]}}</div>
                            <div class="wrong-explain">${{q.wrongExplanation || q.correctExplanation || q.explanation || ''}}</div>
                        </div>
                    `;
                }}
            }});
            if (!reviewHtml) {{
                reviewHtml = '<div class="wrong-empty">เยี่ยมมาก! ไม่มีข้อผิดในชุดนี้</div>';
            }}
            wrongList.innerHTML = reviewHtml;
            renderMath(wrongList);

            // Show completion screen
            quizContent.style.display = 'none';
            completionScreen.classList.add('show');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function reviewQuiz() {{
            isReviewMode = true;
            currentQuestionIndex = 0;
            const quizContent = document.getElementById('quiz-content');
            const completionScreen = document.getElementById('completion-screen');

            quizContent.style.display = 'block';
            completionScreen.classList.remove('show');
            renderQuestion();
        }}

        function finishReview() {{
            showCompletionScreen();
        }}

        function createNewQuiz() {{
            if (quizBanks.length > 1) {{
                currentBankIndex = (currentBankIndex + 1) % quizBanks.length;
            }}

            const bank = quizBanks[currentBankIndex];
            isReviewMode = false;
            currentQuestionIndex = 0;
            userAnswers = [];
            questions = bank.questions.map(q => ({{ ...q, options: [...q.options] }}));
            totalQuestions = questions.length;

            const quizContent = document.getElementById('quiz-content');
            const completionScreen = document.getElementById('completion-screen');
            document.getElementById('score-value').textContent = `0/${{totalQuestions}}`;
            updateQuizHeader();

            quizContent.style.display = 'block';
            completionScreen.classList.remove('show');
            renderQuestion();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // Keep old name as alias for compatibility
        function retakeQuiz() {{
            createNewQuiz();
        }}

        // Initialize quiz on page load
        updateQuizHeader();
        initQuiz();
    </script>
</body>
</html>"""

    return html


def convert_quiz(input_path: str, output_path: str) -> str:
    """Convert JSON quiz to interactive HTML."""
    logger.info(f"Loading quiz from {input_path}")
    quiz_data = load_quiz_data(input_path)

    banks = quiz_data.get("banks") or []
    question_count = sum(len(bank.get("questions", [])) for bank in banks) or len(quiz_data.get("questions", []))
    logger.info(f"Generating HTML with {len(banks) or 1} bank(s), {question_count} total questions")
    katex_assets = get_katex_assets()
    html = generate_html(quiz_data, katex_assets)

    logger.info(f"Writing HTML to {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    ensure_katex_fonts(output_path, katex_assets['fonts_dir'])
    logger.success(f"Quiz created: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert JSON quiz to interactive HTML")
    parser.add_argument('-i', '--input', required=True, help='Input JSON file')
    parser.add_argument('-o', '--output', default='quiz.html', help='Output HTML file')

    args = parser.parse_args()

    convert_quiz(args.input, args.output)


if __name__ == "__main__":
    main()
