<p align="center">
  <img src="assets/profile/typing-intro-georgia-bold-italic-v6.svg" alt="Typing introduction" width="820" />
</p>

<div align="center">

<a href="https://www.polyu.edu.hk/"><img src="assets/profile/hi-cht-polyu-v5.svg" alt="Hi, I'm CHT — The Hong Kong Polytechnic University" height="50" /></a>
<img src="assets/profile/role-subtitle-v2.svg" alt="Product manager · Interest-driven developer" height="28" />


[👋 About](#about) · [💻 Software](#software-development) · [📊 Data](#data-analytics) · [🤖 Agents](#agents) · [🛠 Stack](#stack)

</div>

<br>

<a href="https://cht.me"><img src="assets/profile/cht-me-v3.svg" alt="cht.me" height="52" /></a> <a href="https://github.com/okht/red-owl-vector-animated"><img src="assets/sleepclaw/red-owl-vector-animated.svg" alt="Red owl animated" height="52" /></a>

---

<a id="about"></a>
## 👋 About me

Hi, I'm CHT. I graduated from The Hong Kong Polytechnic University. I am a product manager and interest-driven developer exploring AI agents, software, and data analytics through open-source projects.

I like starting with a real problem: a repetitive action, a vague product question, or a workflow that keeps losing context. I turn it into a product, then use code and data to make it tangible and testable.

This profile follows three lines of work. Every repository begins with a concrete problem and carries my product judgment about trade-offs, evidence, and what the product could become.

| <div align="center">Line of work</div> | <div align="center">What I care about</div> |
|---|---|
| **Software development** | Remove recurring friction with small, usable tools |
| **Data analytics** | Make assumptions, costs, failures, and decisions inspectable |
| **Agents** | Combine reusable context, tools, and judgment around repeatable workflows |

---

<p align="center">
  <img src="assets/sleepclaw/sleepclaw-coming-soon-v8.svg" alt="SleepClaw — Coming soon." width="820" />
</p>

<a id="software-development"></a>
## 💻 Software development

I build focused tools around problems I have actually encountered.

| <div align="center">Project</div> | <div align="center">Product idea</div> | <div align="center">Stars</div> |
|---|---|---:|
| [**clip-md**](https://github.com/okht/clip-md) | Save valuable AI responses to local Markdown in one click, without breaking the current train of thought | [![Stars](https://img.shields.io/github/stars/okht/clip-md?style=social)](https://github.com/okht/clip-md) |
| [**gmail-inbox-system-public**](https://github.com/okht/gmail-inbox-system-public) | Turn Gmail into a cautious hub for multiple inboxes with composable labels and guarded archiving | [![Stars](https://img.shields.io/github/stars/okht/gmail-inbox-system-public?style=social)](https://github.com/okht/gmail-inbox-system-public) |
| [**okx-btc-daily-report-public**](https://github.com/okht/okx-btc-daily-report-public) | Recalculate the BTC DCA metrics I care about from read-only trades and deliver them by email | [![Stars](https://img.shields.io/github/stars/okht/okx-btc-daily-report-public?style=social)](https://github.com/okht/okx-btc-daily-report-public) |

<details>
<summary><strong>clip-md</strong> — Copy what matters. Keep it as Markdown.</summary>

<br>

I built `clip-md` after repeatedly feeling friction when saving useful AI content. ChatGPT, Claude, and other tools often produce answers worth keeping, and I wanted those answers to become part of my local knowledge base. The old flow required an editor, a new file, a destination, a filename, and a final save. That sequence was long enough to interrupt the thought I was trying to preserve.

I reduced the core interaction to one small action: copy text, use the control that appears near the pointer, and save it directly as local Markdown. Automatic naming is another deliberate choice. The app extracts keywords and uses a fallback chain when extraction is weak, removing one more decision while keeping files readable and searchable.

I want `clip-md` to serve frequent AI users and knowledge workers. Its direction is deliberately lightweight: improve reliability, platform fit, signed distribution, and the quiet details that let a desktop tool stay useful for a long time.

</details>

<details>
<summary><strong>gmail-inbox-system-public</strong> — One inbox, several meanings, controlled automation.</summary>

<br>

I built Gmail Inbox System after routing several mailboxes into Gmail. Switching decreased, but the inbox began to lose source and action semantics. App notifications, bills, security alerts, personal messages, and pending work arrived in one stream, while the old labels mixed source, content type, and status in ways that became harder to maintain over time.

I separated the label system into composable dimensions: application, type, source, and status each express one meaning. A message can preserve where it came from, what it contains, and what action it needs. Classification, preview, retention windows, and protection rules form explicit gates around archiving, while uncertain mail remains visible.

I want this system to become my personal email hub, with Gmail as the unified entrance and AI-generated daily briefings as a future layer. The public repository contains reusable, privacy-conscious rules and examples; it contains no private messages, account credentials, or access to my live mailboxes.

</details>

<details>
<summary><strong>okx-btc-daily-report-public</strong> — My DCA strategy, measured on my terms.</summary>

<br>

I built OKX BTC Daily Report because I follow my own BTC DCA strategy. The exchange's built-in plan did not match the rules and cadence I wanted, and its fixed dashboard could not answer the questions I cared about, such as 30-day performance, planned versus actual investment, and the result after fills and fees.

The workflow reads trade data through read-only access and recalculates daily, 7-day, 30-day, and cumulative views with my own definitions. Split fills, fees, and quote currencies make manual tracking drift over time, so the rules need to run consistently. I chose email delivery because the report should arrive inside an existing routine without asking me to maintain another dashboard.

I want it to develop into a personal investment data console covering more assets, time windows, metrics, and visual views. The public repository is a sanitized reference implementation: it contains no API keys, cannot see my OKX account, and does not execute trades.

</details>

---

<a id="data-analytics"></a>
## 📊 Data analytics

I use analysis to challenge intuition, record uncertainty, and make decisions easier to revisit.

> The investment and trading projects document personal research. They do not provide financial advice.

| <div align="center">Project</div> | <div align="center">Product idea</div> | <div align="center">Stars</div> |
|---|---|---:|
| [**quant-research**](https://github.com/okht/quant-research) | A reusable research framework that records assumptions, costs, failed experiments, and validation limits | [![Stars](https://img.shields.io/github/stars/okht/quant-research?style=social)](https://github.com/okht/quant-research) |
| [**crypto-trading-research**](https://github.com/okht/crypto-trading-research) | Test whether active BTC strategies add enough value to justify their cost and effort against long-term holding | [![Stars](https://img.shields.io/github/stars/okht/crypto-trading-research?style=social)](https://github.com/okht/crypto-trading-research) |
| [**ecommerce-user-analysis**](https://github.com/okht/ecommerce-user-analysis) | Turn historical transactions into customer segments and growth hypotheses through RFM and K-Means | [![Stars](https://img.shields.io/github/stars/okht/ecommerce-user-analysis?style=social)](https://github.com/okht/ecommerce-user-analysis) |
| [**ai-chat-analytics**](https://github.com/okht/ai-chat-analytics) | Link conversation behavior, issue attribution, and follow-up signals to AI product priorities | [![Stars](https://img.shields.io/github/stars/okht/ai-chat-analytics?style=social)](https://github.com/okht/ai-chat-analytics) |

<details>
<summary><strong>quant-research</strong> — Keep the evidence, including the failures.</summary>

<br>

I built `quant-research` to turn investment ideas into hypotheses that data can challenge. A strategy can sound reasonable and still rely on one favorable period. I want to see which data it used, how it formed signals, where returns came from, and how much survives when windows, parameters, and models change.

I pay particular attention to overfitting and fragmented research chains. Parameter searches can produce attractive in-sample results, while code, data, and temporary outputs slowly lose their connection. I keep weak factors, failed models, and degraded strategies, and I evaluate costs, attribution, drawdown, and out-of-sample behavior alongside return. A failed experiment still tells me which path lacks durable evidence.

I want `quant-research` to become a reusable framework for snapshots, hypotheses, signals, backtests, validation, and recorded findings. New markets and models can then enter the same structure, making personal research cumulative, comparable, and reviewable.

</details>

<details>
<summary><strong>crypto-trading-research</strong> — Can active BTC trading earn its complexity?</summary>

<br>

I built `crypto-trading-research` around a question that directly affects my own decisions: after fees, slippage, turnover, and attention are counted, is long-term BTC holding already the lowest-cost and lowest-effort strategy? Active trading and machine learning can look sophisticated, but complexity alone does not prove additional value.

I use long-term holding as the persistent baseline, then test classic indicators, statistical signals, and machine-learning models against it. Costs are explicit because frequent turnover can erase a paper advantage. Windows and fee assumptions remain visible, and model metrics still need to become real strategy returns. MA, RSI, Bollinger Bands, and XGBoost experiments remain in the repository even when their results are weak.

I want the project to become a BTC decision evidence base that keeps testing the same question across new data and market regimes. Every conclusion stays attached to its sample window, cost assumption, and validation method so another learner can review the whole path.

</details>

<details>
<summary><strong>ecommerce-user-analysis</strong> — See the customers hidden inside aggregate metrics.</summary>

<br>

I built `ecommerce-user-analysis` to understand how transaction records become meaningful customer segments. Revenue, order count, and average order value describe the whole business, but they compress differences between loyal customers, drifting customers, promising newcomers, and people who need a different strategy.

I use RFM to create an interpretable business segmentation, then K-Means to inspect the natural structure in the data. Together they preserve a clear operating language while adding a second analytical view. The project moves from more than one million historical transactions through cleaning, exploration, segmentation, and visualization, then turns the result into retention, reactivation, and conversion hypotheses.

I want it to develop into an e-commerce growth analytics console that tracks how segments change, which metrics matter for each group, and what growth experiments actually change behavior.

</details>

<details>
<summary><strong>ai-chat-analytics</strong> — Turn conversational signals into product priorities.</summary>

<br>

I built `ai-chat-analytics` because likes, dislikes, retries, and follow-ups do not directly tell an AI product team what to fix first, why users are dissatisfied, or whether an improvement changed the experience. Broad labels such as general quality can locate a problem while still leaving the cause unclear.

I split the work into synthetic data generation, behavior analysis, issue attribution, follow-up signals, and insight summarization. A fixed seed makes the public snapshot reproducible without exposing real conversations. Transparent keyword rules establish an explainable baseline and expose their own limit: 71.2% of current bad cases still fall into a catch-all label, and manual validation remains incomplete.

I want the project to serve AI product leaders and grow into an AI experience monitoring console, with continuous metrics, attribution quality, alerts, and experiment results connected in one place.

</details>

---

<a id="agents"></a>
## 🤖 Agents

I build agent systems around workflows that benefit from reusable context, tools, and judgment.

| <div align="center">Project</div> | <div align="center">Product idea</div> | <div align="center">Stars</div> |
|---|---|---:|
| [**readme-craft**](https://github.com/okht/readme-craft) | Build and maintain public READMEs from repository evidence, with multilingual and visual validation | [![Stars](https://img.shields.io/github/stars/okht/readme-craft?style=social)](https://github.com/okht/readme-craft) |
| [**desktop-organizer**](https://github.com/okht/desktop-organizer) | Organize Windows folders through a dry-run, explicit approval, safe moves, and verification | [![Stars](https://img.shields.io/github/stars/okht/desktop-organizer?style=social)](https://github.com/okht/desktop-organizer) |
| [**become-master**](https://github.com/okht/become-master) | Compress an unfamiliar field into prioritized talking points and a 30-second memory card | [![Stars](https://img.shields.io/github/stars/okht/become-master?style=social)](https://github.com/okht/become-master) |
| [**ai-dev-context-framework**](https://github.com/okht/ai-dev-context-framework) | Preserve product intent, permissions, decisions, and task state across coding-Agent sessions | [![Stars](https://img.shields.io/github/stars/okht/ai-dev-context-framework?style=social)](https://github.com/okht/ai-dev-context-framework) |

<details>
<summary><strong>readme-craft</strong> — Make public documentation prove what a repository can do.</summary>

<br>

I built `readme-craft` after repeatedly making the same publishing decisions across public projects. Hero structure, badge colors, section order, language navigation, table width, Mermaid size, and privacy checks all required fresh manual judgment. I wanted a reusable publishing standard whose quality could remain stable across repositories.

Evidence-driven design is the core principle. The Skill inspects code, manifests, releases, workflows, licenses, and repository state before it writes. A validator checks links, anchors, language parity, diagrams, and private paths, while rendered previews cover layout that source inspection cannot prove.

I want `readme-craft` to serve independent developers and maintainers, then grow into a README maintenance system that detects repository changes and content drift over time.

</details>

<details>
<summary><strong>desktop-organizer</strong> — See every move before anything moves.</summary>

<br>

I built `desktop-organizer` from my own need to clean a Windows Desktop filled with documents, screenshots, installers, archives, and code projects. Manual sorting required repeated decisions, while direct automation introduced the risks of misclassification, overwrites, and unintended file operations.

The workflow is inspect, plan, approve, execute, and verify. Its default mode only prints a dry-run; moving requires explicit approval. It does not delete or overwrite, conflicts stop execution early, shortcuts and system files stay in place, uncertain items enter a review inbox, and all work remains local.

I want it to serve heavy Windows Desktop users and develop into a personalized classification system where people can keep their own taxonomy, rules, and exception lists.

</details>

<details>
<summary><strong>become-master</strong> — Five minutes to find your footing in a conversation.</summary>

<br>

I built `become-master` after seeing a close friend in tech struggle to enter social conversations. He was capable and curious, yet conversations with colleagues or someone he liked could stall because he could not quickly find shared topics. Search gave him plenty of information, but very little priority.

The Skill starts with a field and a real situation, then organizes terms, products, judgments, talking points, common traps, and recovery patterns. Its most important choice is forced compression: a large field ends as an 18-node memory card that can be reviewed just before the conversation. The direction I care about is honest preparation, better listening, and more natural questions.

I want it to become a personal social-preparation assistant that uses the relationship and setting to help users discover shared interests, prepare openings, and keep a conversation moving naturally.

</details>

<details>
<summary><strong>ai-dev-context-framework</strong> — Keep coding Agents aligned across sessions.</summary>

<br>

I built `ai-dev-context-framework` because coding Agents can lose continuity across sessions. Product intent, technical constraints, architecture choices, and task state become scattered across chats and temporary files. As a project grows, routine progress updates can also reach decisions that should remain under user control.

I chose Markdown contracts for the context layer. Product discussion becomes `SPEC.md`, then the framework creates an Agent entry point, a task queue, and additional architecture, data, design, issue, decision, and handoff files when complexity triggers them. Locked and generated regions express maintenance boundaries, while Full and Lite editions support different project sizes. The current guardrails remain conventions that depend on Agent compliance.

I want the framework to serve maintainers of complex projects and grow into an Agent project-governance layer that checks context consistency, permission boundaries, decision records, and reliable restart points.

</details>

---

<a id="stack"></a>
## 🛠 Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000000)
![Jupyter](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![PowerShell](https://img.shields.io/badge/-PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Mermaid](https://img.shields.io/badge/-Mermaid-FF3670?style=for-the-badge&logo=mermaid&logoColor=white)
![Codex](https://img.shields.io/badge/-Codex-000000?style=for-the-badge&logo=openai&logoColor=white)
![Claude Code](https://img.shields.io/badge/-Claude%20Code-D97757?style=for-the-badge)
![AI Agents](https://img.shields.io/badge/-AI%20Agents-8B5CF6?style=for-the-badge)

---

<div align="center">

### **Build from real problems. Measure honestly. Keep what compounds.**

Thanks for stopping by. Explore any project that catches your eye.

</div>
