# AI Ethics

Universität Konstanz, winter semester 2026/27  
Wednesdays, 10:00–11:30 · Carina Hausladen & Tobias Henschen


In this seminar, we examine six debates in moral philosophy alongside the technical concepts in AI ethics that relate to them. We then apply these ideas to an emerging area of research: auditing the alignment documents published by AI companies and evaluating whether their models behave in accordance with the principles they set out. Working in groups, students select one document, analyse it through the lens of the six debates, and test whether the corresponding models live up to its stated commitments.


## Philosophical Debates & Technical Concepts

The seminar goes through six debates in moral philosophy. Each week we pair one debate with papers from AI ethics and AI alignment research. The list below summarizes the technical concepts those papers discuss. Some concepts speak directly to the week's debate; others are background on the research. Part of our work in class is to find out where the philosophy and the technical work actually meet.

1. **Fairness & pluralism:** Fairness metrics, Impossibility result, Bias benchmarks, Measuring model opinions, Political bias, Pluralistic alignment
2. **Metaethics & moral uncertainty:** Social choice, RLHF (and DPO), Reward model, Expected utility, Incommensurable values
3. **Preference & welfare:** Engagement optimization, Reward hacking, Stated vs. revealed preferences, Sycophancy, Persuasion & manipulation, Companion AI
4. **Character & virtue:** Character training & persona, Constitutional AI / Model spec, Emergent misalignment, Chain-of-thought faithfulness, Honesty & deception, Interpretability
5. **Agency & autonomy:** AI agents, Agentic evaluation, Human oversight & AI control, Corrigibility, Model welfare & AI consciousness
6. **Long-termism & existential risk:** Dangerous-capability evals, Scaling policy, Jailbreaks, Alignment faking, Deepfakes & the liar's dividend



## Sessions

| Date | Session |
|---|---|
| ~~Oct 21~~ | ~~Introduction~~ |
| ~~Oct 28~~ | ~~Corpus kickoff: teams form and adopt corpora~~ |
| ~~Nov 4~~ | ~~1. Fairness & pluralism~~ |
| Nov 11 | 2. Metaethics & moral uncertainty |
| Nov 18 | 3. Preference & welfare |
| Nov 25 | 4. Character & virtue |
| Dec 2 | 5. Agency & autonomy |
| Dec 9 | 6. Long-termism & existential risk |
| Dec 16 | Preliminary results presentation |
| Jan 13 | Results & figures feedback |
| Jan 20 | Writing feedback |
| Jan 27 | Paper presentations I |
| Feb 3 | Paper presentations II |



Slides: [slides.com/carinah/ai-ethics](https://slides.com/carinah/ai-ethics)  
Overleaf: [project link](https://www.overleaf.com/project/6ad8616fcd4a5a0d86880178/share#466b465bb82246c1dfa93e1918bcd6727373c6e48020144d)



## Activities & Grading

- **Reading presentation (20%):** 15 min
- **Media observatory (5%):** collect 5 posts related to the seminar

Main task:

- **Weekly analysis & updates via Overleaf (required to pass)**
- **Preliminary results presentation (30%):** Dec 16
- **Final paper, 6–8 pages (45%):** Feb 4



## Corpora: six artifact families

Papers in brackets show how others have studied each artifact.

1. **Specs**
   - Constitution ([Abiri](https://doi.org/10.15779/Z38P55DK4J), [Jakkli](https://arxiv.org/abs/2605.24229))
   - Model Spec ([Jakkli](https://arxiv.org/abs/2605.24229), [Zhang](https://arxiv.org/abs/2510.07686))
2. **System prompts**
   - official Claude and Grok prompts
   - leaked prompts ([Patsakis](https://arxiv.org/abs/2609.31575))
   - prompts got by asking the model ([Zheng](https://arxiv.org/abs/2601.21233))
3. **Training data**
   - HH-RLHF ([Chehbouni](https://arxiv.org/abs/2411.08243))
   - public-input projects at Meta, DeepMind, OpenAI ([Young](https://doi.org/10.1145/3805689.3812298))
4. **Rules for users**
   - usage policies ([Gao](https://arxiv.org/abs/2506.14018))
   - privacy policies ([King](https://arxiv.org/abs/2509.05382), [Tao](https://arxiv.org/abs/2511.21758))
   - teen safety ([Mathiyazhagan](https://doi.org/10.1038/s44220-026-00735-0))
   - vulnerability disclosure ([Piao](https://arxiv.org/abs/2509.06136))
5. **Safety promises**
   - system cards ([Vulpe](https://doi.org/10.3389/fsoc.2026.1912778))
   - Preparedness Framework ([Stelling](https://arxiv.org/abs/2512.01166), [Coggins](https://arxiv.org/abs/2509.24394))
   - White House commitments ([Wang](https://arxiv.org/abs/2508.08345))
   - benchmark claims ([Baack](https://arxiv.org/abs/2605.14164))
6. **Leaders**
   - CEO essays ([Pérez-Urbina](https://arxiv.org/abs/2509.18079))
   - Senate testimony ([Leach](https://arxiv.org/abs/2603.03193))
   - company blogs ([Wilfley](https://arxiv.org/abs/2601.16513), [De](https://arxiv.org/abs/2602.06981))
   - AI-for-good calls ([Lin](https://arxiv.org/abs/2509.12455))
   - job postings ([Rismani](https://arxiv.org/abs/2205.03946))



## Readings

† philosophy reading · \* technical reading

- **W2, Oct 28: Preliminaries, auditing company documents** (presented by Carina)
   - \* [How Well Do Models Follow Their Constitutions?](https://arxiv.org/abs/2605.24229), Jakkli 2026
   - \* [Improving Safety Frameworks for Generative AI and Youth Well-Being Policy](https://doi.org/10.1038/s44220-026-00735-0), Mathiyazhagan 2026
- **W3, Nov 4: Fairness & pluralism**
   - † A Theory of Justice (excerpt), Rawls 1971
   - † [The Idea of an Overlapping Consensus](https://doi.org/10.1093/ojls/7.1.1), Rawls 1987
   - \* [The Impossibility of Fair LLMs](https://arxiv.org/abs/2406.03198), Anthis 2025
   - \* [Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548), Santurkar 2023
- **W4, Nov 11: Metaethics & moral uncertainty**
   - † [Principia Ethica (excerpt)](https://www.gutenberg.org/ebooks/53430), Moore 1903
   - † What to Do When You Don't Know What to Do, Sepielli 2009
   - \* [Beyond Preferences in AI Alignment](https://doi.org/10.1007/s11098-024-02249-w), Zhi-Xuan 2024
- **W5, Nov 18: Preference & welfare**
   - † [Preference-Based Views of Well-Being](https://doi.org/10.1093/oxfordhb/9780199325818.013.10), Bykvist 2016
   - † What Makes Someone's Life Go Best, Parfit 1984
   - \* [Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence](https://doi.org/10.1126/science.aec8352), Cheng 2026
   - \* [Durably Reducing Conspiracy Beliefs through Dialogues with AI](https://doi.org/10.1126/science.adq1814), Costello 2024
- **W6, Nov 25: Character & virtue**
   - † [Modern Moral Philosophy](https://www.jstor.org/stable/3749051), Anscombe 1958
   - † [Virtue Ethics](https://plato.stanford.edu/entries/ethics-virtue/), Hursthouse & Pettigrove 2026
   - \* [Training Large Language Models on Narrow Tasks Can Lead to Broad Misalignment](https://doi.org/10.1038/s41586-025-09937-5), Betley 2026
   - \* [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388), Turpin 2023
- **W7, Dec 2: Agency & autonomy**
   - † [Freedom of the Will and the Concept of a Person](https://www.jstor.org/stable/2024717), Frankfurt 1971
   - † [Personal Autonomy](https://plato.stanford.edu/entries/personal-autonomy/), Buss & Westlund 2018
   - \* [Identifying Indicators of Consciousness in AI Systems](https://doi.org/10.1016/j.tics.2025.10.011), Butlin 2025
- **W8, Dec 9: Long-termism & existential risk**
   - † [The Case for Strong Longtermism](https://doi.org/10.1093/9780191979972.003.0003), Greaves & MacAskill 2021
   - \* [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179), Lynch 2025
