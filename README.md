# AI Ethics

Universität Konstanz, winter semester 2026/27
Wednesdays, Oct 21 – Feb 3 · Carina Hausladen & Tobias Henschen


Alignment is an implicitly normative project: every technique for making AI "good" takes a stance on what good means.
In this seminar we read six philosophical lenses into four corpora of how researchers, companies, governments and the press talk about AI.

1. **Fairness & pluralism.** Can AI be fair, and whose values count when they differ?
2. **Metaethics & moral uncertainty.** Does alignment presuppose objective values, and how should systems reason when they don't know which ethics is right?
3. **Preference & welfare.** Should AI track what people say they want, what they do, or what is good for them?
4. **Character & virtue.** Should we specify rules and utility functions, or cultivate something like good character?
5. **Agency & autonomy.** Can AI systems be moral agents, or only tools? Corrigible or autonomous?
6. **Long-termism & existential risk.** What do we owe future generations, and how should that shape alignment today?



## Sessions

| Date | Session |
|---|---|
| Oct 21 | Introduction |
| Oct 28 | Corpus kickoff: teams form and adopt corpora |
| Nov 4 | 1. Fairness & pluralism |
| Nov 11 | 2. Metaethics & moral uncertainty |
| Nov 18 | 3. Preference & welfare |
| Nov 25 | 4. Character & virtue |
| Dec 2 | 5. Agency & autonomy |
| Dec 9 | 6. Long-termism & existential risk |
| Dec 16 | Preliminary results |
| Jan 13 | Hackathon: feedback |
| Jan 20 | Final group results |
| Jan 27 | Paper hackathon I |
| Feb 3 | Paper hackathon II |



## Corpora

Each group takes one document, reads it through all six lenses, and tests whether the model does what the document says.

1. **[Claude's Constitution](https://www.anthropic.com/constitution)** (Anthropic, 2026) · ~80 pp
2. **[Model Spec](https://model-spec.openai.com/)** (OpenAI, 2026) · ~100 pp
3. **[Claude Opus 5 system card](https://anthropic.com/claude-opus-5-system-card)** (Anthropic, 2026), ch. 4, 6, 7 · ~90 pp
4. **OpenAI system card & shorter texts** · ~95 pp
   - [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) (OpenAI, 2026), §1–10
   - [Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input) (Anthropic, 2023)
   - [Collective alignment](https://openai.com/index/collective-alignment-aug-2025-updates/) (OpenAI, 2025)
   - [Claude's Character](https://www.anthropic.com/news/claude-character) (Anthropic, 2024)
   - [Deprecation commitments](https://www.anthropic.com/research/deprecation-commitments) (Anthropic, 2025)
   - [Model Spec changelog](https://github.com/openai/model_spec) (OpenAI, ongoing)



## Readings

Technical concepts per lens and two papers per week; the remaining concepts are covered in the lecture.

| Lens | Technical concept | Paper |
|---|---|---|
| **Basics (W1–W2)** | • Pretraining (base vs. chat model)<br>• Training data (memorization, consent, copyright)<br>• System prompt<br>• Benchmarks & evaluation validity<br>• LLM-as-a-judge<br>• Reading an experiment (randomized trials, effect sizes) |  |
| **1. Fairness & pluralism** | • Fairness metrics (group, individual, counterfactual)<br>• Impossibility result<br>• Bias metrics & benchmarks (BBQ, WinoBias, BOLD)<br>• Measuring model opinions (answer distributions vs. surveys)<br>• Political bias<br>• Pluralistic alignment (incl. WEIRD bias) | Anthis 2025, Santurkar 2023 |
| **2. Metaethics & moral uncertainty** | • Social choice (preference aggregation)<br>• RLHF (and DPO)<br>• Reward model<br>• Utility & expected utility<br>• Incommensurable values & moral uncertainty | Zhi-Xuan 2024, Conitzer 2024 |
| **3. Preference & welfare** | • Engagement optimization<br>• Reward hacking / Goodhart<br>• Immediate vs. reflective preferences (stated, revealed)<br>• Sycophancy (incl. social sycophancy)<br>• Persuasion & manipulation<br>• Companion AI / emotional reliance | Cheng 2026, Costello 2024 |
| **4. Character & virtue** | • Character training & persona<br>• Constitutional AI / Model spec<br>• Fine-tuning & emergent misalignment<br>• Chain of thought & faithfulness<br>• Honesty, deception & hallucination<br>• Interpretability | Betley 2026, Turpin 2023 |
| **5. Agency & autonomy** | • AI agent<br>• Agentic evaluation (benchmark vs. trajectory)<br>• Human oversight / AI control / scalable oversight<br>• Corrigibility<br>• Model welfare & AI consciousness | Lynch 2025, Butlin 2025 |
| **6. Long-termism & existential risk** | • Dangerous-capability evals<br>• Scaling policy<br>• Jailbreak<br>• Deceptive alignment / alignment faking<br>• Deepfakes, watermarking & the liar's dividend | Greenblatt 2024, Schiff 2024 |
