<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=000000&center=true&vCenter=true&random=false&width=820&lines=%E4%BB%8E%E7%9C%9F%E5%AE%9E%E9%97%AE%E9%A2%98%E5%87%BA%E5%8F%91%E3%80%82;%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91%20%C2%B7%20%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%20%C2%B7%20Agent%E3%80%82;%E8%AE%A9%E6%83%B3%E6%B3%95%E5%8F%AF%E4%BB%A5%E8%90%BD%E5%9C%B0%E3%80%81%E9%AA%8C%E8%AF%81%E5%92%8C%E5%A4%8D%E7%94%A8%E3%80%82" alt="动态个人介绍" />
</p>

<div align="center">

# 👋 Hi，这里是 Ht.

### *产品经理 · 兴趣驱动的开发者 · 数据分析工程师*


[![GitHub 关注者](https://img.shields.io/github/followers/okht?style=social)](https://github.com/okht) [![GitHub Stars 总计](https://img.shields.io/github/stars/okht?style=social&label=Stars)](https://github.com/okht?tab=repositories)

<br>

<table>
<tr><td align="left">

🧩 &nbsp;当重复动作值得拥有一个产品时，我会把它做成程序。<br>
📊 &nbsp;当直觉需要证据时，我会用数据检验它。<br>
🧠 &nbsp;当工作流值得长期复用时，我会把它做成 Agent Skill。

</td></tr>
</table>

### ✨ 我把真实问题变成可以使用、衡量和持续改进的产品。

**好奇心 → 产品判断 → 程序或分析 → 可复用系统**

<br>

[👋 关于我](#about) · [💻 程序开发](#software-development) · [📊 数据分析](#data-analytics) · [🧠 Agent Skills](#agent-skills) · [🧭 产品原则](#principles) · [🛠 技术工具](#stack)

[**English**](../../README.md) · [**简体中文**](README_ZH.md) · [**Español**](README_ES.md) · [**Deutsch**](README_DE.md) · [**日本語**](README_JA.md) · [**Русский**](README_RU.md) · [**Português**](README_PT.md) · [**한국어**](README_KO.md)

</div>

---

<a id="about"></a>
## 👋 关于我

Hi，这里是 Ht. 我是一名产品经理，也是一名兴趣驱动的开发者和数据分析工程师。

我喜欢从真实问题出发：一个反复出现的动作、一个模糊的产品问题，或者一条持续丢失上下文的工作流。我会先把它整理成产品，再通过代码和数据让它落地并接受验证。

这个主页记录了我的三条作品主线。每个项目都始于一个具体问题，也保留了我对产品取舍、证据边界和未来方向的判断。

| 作品主线 | 我关注的事情 |
|---|---|
| **程序开发** | 用小而可用的工具减少反复出现的摩擦 |
| **数据分析** | 让假设、成本、失败结果和决策依据保持可检查 |
| **Agent Skills** | 把重复工作流沉淀成可以长期复用的系统 |

---

<a id="software-development"></a>
## 💻 程序开发

我围绕自己真正遇到的问题，开发边界清晰的实用工具。

| 项目 | 产品想法 | Stars |
|---|---|---:|
| [**clip-md**](https://github.com/okht/clip-md) | 一次点击把有价值的 AI 回答保存为本地 Markdown，同时保持当前思路的连续性 | [![Stars](https://img.shields.io/github/stars/okht/clip-md?style=social)](https://github.com/okht/clip-md) |
| [**gmail-inbox-system-public**](https://github.com/okht/gmail-inbox-system-public) | 用可组合标签和受控归档，把 Gmail 变成多个邮箱的谨慎中枢 | [![Stars](https://img.shields.io/github/stars/okht/gmail-inbox-system-public?style=social)](https://github.com/okht/gmail-inbox-system-public) |
| [**okx-btc-daily-report-public**](https://github.com/okht/okx-btc-daily-report-public) | 从只读成交数据重新计算我关心的 BTC 定投指标，并通过邮件送达 | [![Stars](https://img.shields.io/github/stars/okht/okx-btc-daily-report-public?style=social)](https://github.com/okht/okx-btc-daily-report-public) |

<details>
<summary><strong>clip-md</strong> — 复制值得保留的内容，把它保存成 Markdown。</summary>

<br>

我做 `clip-md`，源于自己长期保存 AI 内容时遇到的摩擦。使用 ChatGPT、Claude 等工具时，我经常会碰到值得长期保留的回答，也希望它们能够沉淀进自己的本地知识库。原来的流程需要打开编辑器、创建文件、选择目录、起名字再保存，连续的操作很容易打断当前思路。保存成本一旦变高，有价值的内容也更容易被暂时搁置。

因此，我把 `clip-md` 的核心体验压缩到了一个很小的动作里：复制文本后，保存入口直接出现在鼠标旁边，点击一次就能写入本地 Markdown。自动命名也是我很看重的产品决定。系统会提取关键词，并在无法提取时使用逐级降级规则，让用户少做一次命名判断，同时保留清晰、可搜索的本地文件。

我主要希望它服务高频 AI 用户和知识工作者。未来我希望 `clip-md` 继续保持轻量，专注打磨稳定性、系统适配、签名分发和日常使用体验，让它成为一个可以长期留在桌面上的安静工具。

</details>

<details>
<summary><strong>gmail-inbox-system-public</strong> — 一个收件箱，多种语义，受控自动化。</summary>

<br>

我做 Gmail Inbox System，是因为我把多个邮箱逐步汇入 Gmail 后，虽然减少了来回切换，收件箱却开始失去来源和处理语义。应用通知、账单、安全提醒、个人邮件和待处理事项堆在同一个入口里，原有标签也同时承载来源、类型与状态，数量越多越难维护。

我把标签体系拆成了可以自由组合的独立维度：应用、类型、来源和状态分别表达自己的含义。这样，同一封邮件可以同时保留它来自哪里、属于什么内容、当前需要什么动作。归档流程保持谨慎，分类、预览、保留期和保护规则构成明确的安全门，让不确定邮件继续留在收件箱里。

我希望它最终成为自己的个人邮箱中枢：多个邮箱通过 Gmail 形成统一入口，同时保留清楚的来源与行动状态。接下来我会继续加强稳定性和受控自动化，并加入 AI 每日邮箱简报。公开仓库只包含可复用规则和隐私安全示例，其中没有私人邮件、账户凭据或实时邮箱访问能力。

</details>

<details>
<summary><strong>okx-btc-daily-report-public</strong> — 用自己的口径衡量自己的定投策略。</summary>

<br>

我做 OKX BTC Daily Report，是因为我有自己的 BTC 定投策略，交易所提供的定投功能无法满足我对规则和节奏的自定义需求。交易所看板也只提供固定的统计方式，我无法直接查看自己真正关心的指标，例如近 30 日定投表现、计划投入与实际投入的偏差，以及不同成交和手续费共同形成的真实结果。

因此，我让系统直接读取只读成交数据，按照自己的时间窗口和统计口径重新计算每日、近 7 日、近 30 日与累计表现。手工统计在面对拆分成交、手续费和不同计价币种时很容易逐渐失真，所以这些计算规则需要由系统稳定执行。我选择邮件作为交付方式，让报告按计划主动到达日常邮箱，减少反复打开交易所和维护另一个独立看板的成本。

我希望它未来发展成个人投资数据台，可以逐步覆盖更多资产、观察周期、指标和可视化方式。公开仓库是一份经过脱敏的参考实现，其中没有 API 密钥，无法查看我的 OKX 账户，也不具备交易执行能力。

</details>

---

<a id="data-analytics"></a>
## 📊 数据分析

我用分析挑战直觉、记录不确定性，也让每个决定更容易被重新检查。

> 投资与交易项目用于记录个人研究，不提供投资建议。

| 项目 | 产品想法 | Stars |
|---|---|---:|
| [**quant-research**](https://github.com/okht/quant-research) | 一套记录假设、成本、失败实验和验证边界的可复用研究框架 | [![Stars](https://img.shields.io/github/stars/okht/quant-research?style=social)](https://github.com/okht/quant-research) |
| [**crypto-trading-research**](https://github.com/okht/crypto-trading-research) | 检验主动 BTC 策略相对长期持有能否创造足以覆盖成本和精力的价值 | [![Stars](https://img.shields.io/github/stars/okht/crypto-trading-research?style=social)](https://github.com/okht/crypto-trading-research) |
| [**ecommerce-user-analysis**](https://github.com/okht/ecommerce-user-analysis) | 通过 RFM 与 K-Means，把历史交易转换成用户分层和增长假设 | [![Stars](https://img.shields.io/github/stars/okht/ecommerce-user-analysis?style=social)](https://github.com/okht/ecommerce-user-analysis) |
| [**ai-chat-analytics**](https://github.com/okht/ai-chat-analytics) | 把对话行为、问题归因和追问信号连接到 AI 产品优先级 | [![Stars](https://img.shields.io/github/stars/okht/ai-chat-analytics?style=social)](https://github.com/okht/ai-chat-analytics) |

<details>
<summary><strong>quant-research</strong> — 保留全部证据，也保留失败结果。</summary>

<br>

我做 `quant-research`，是为了把自己的投资想法转换成可以被数据检验的假设。一个策略在直觉上合理，或者在某段历史数据上取得高收益，都不足以支撑结论。我希望完整看到它使用了什么数据、如何生成信号、收益来自哪里，以及更换时间窗口、参数和模型后还能保留多少效果。

我尤其关注量化研究中的过拟合和链路断裂问题。参数搜索很容易产生漂亮的样本内结果，研究过程也常常散落在不同代码、数据和临时输出中。因此，我保留弱因子、失败模型和表现退化的策略，同时把交易成本、收益归因、回撤与样本外验证放在收益旁边一起判断。失败实验同样构成研究结果，因为它们说明了哪些路径缺乏稳定证据。

我希望 `quant-research` 最终发展成一套可复用的研究框架，把数据快照、假设、信号、回测、验证和结论组织成固定流程。未来新增市场、策略和模型时，可以沿用同一套研究结构，让个人量化研究逐渐形成可积累、可比较、可复查的长期系统。

</details>

<details>
<summary><strong>crypto-trading-research</strong> — 主动交易能否赚回它增加的复杂度？</summary>

<br>

我做 `crypto-trading-research`，是为了回答一个与自己投资决策直接相关的问题：如果把手续费、滑点、换仓频率以及投入精力都考虑进去，长期持有 BTC 是否已经是成本最低、最省精力的策略。主动交易和机器学习模型看起来更加复杂，也可能产生更漂亮的局部结果，但复杂度本身无法证明它创造了额外价值。

因此，我把长期持有设为持续比较的基线，并依次研究经典指标、统计信号和机器学习模型。我尤其强调显式计算交易成本，因为高频换仓很容易让纸面优势消失。不同时间窗口和费用口径分别保留，模型的分类指标也需要继续转换成真实策略收益来检验。MA、RSI、布林带和 XGBoost 等实验即使表现较差，也会继续作为研究证据存在。

我希望它最终成为一个 BTC 决策证据库，持续加入新数据和不同市场阶段，反复检查长期持有与主动策略之间的差异。每次结论都会绑定具体数据窗口、费用假设和验证方式，为加密策略学习者提供一条可以完整复查的研究路径。

</details>

<details>
<summary><strong>ecommerce-user-analysis</strong> — 看见汇总指标背后的不同用户。</summary>

<br>

我做 `ecommerce-user-analysis`，是因为我想理解一组交易记录如何进一步变成清晰的用户分层。销售额、订单量和客单价能够描述业务整体表现，但这些汇总指标会把不同用户的价值与行为差异压缩在一起。产品和增长决策还需要回答更具体的问题：哪些用户贡献稳定、哪些用户正在流失、哪些用户值得重点培育，以及不同人群应该采用怎样的运营策略。

因此，我先通过 RFM 建立一套具有业务解释力的分层规则，再使用 K-Means 观察数据中的自然聚类结构。两种方法放在一起，可以同时保留清楚的业务语言和数据交叉验证能力。项目从一百多万条历史交易开始，依次完成清洗、探索分析、用户分群和可视化，并把结果继续转成留存、召回与转化方面的策略假设。

我主要希望它服务产品与增长分析者。未来，我希望它发展成一个电商增长分析台，持续呈现用户结构的变化、各分群的关键指标和增长实验结果，让用户分析从一次性报告逐步变成可以支持日常决策的工作系统。

</details>

<details>
<summary><strong>ai-chat-analytics</strong> — 把对话信号转换成产品优先级。</summary>

<br>

我做 `ai-chat-analytics`，是因为对话式 AI 产品已经积累了点赞、点踩、重试和追问等行为信号，但这些数字本身很难直接回答产品负责人最关心的问题：哪个场景应该优先改善，用户为什么不满意，以及一次优化是否真正改变了体验。尤其当大量问题被归入宽泛的「质量不足」时，分析虽然发现了异常，产品团队仍然缺少足够具体的原因判断。

因此，我把分析拆成数据生成、行为分析、问题归因、追问信号和洞察汇总五个连续阶段。项目使用固定随机种子生成合成会话快照，让分析过程可以公开复现，同时避免暴露真实用户数据。归因部分先采用透明的关键词规则建立可解释基线，并直接呈现它的能力边界：当前 71.2% 的 bad case 仍落入兜底类别，人工验证也尚未完成。这个结果提醒我，可靠的产品分析需要把未验证的部分同样暴露出来。

我主要希望它服务 AI 产品负责人，帮助他们把用户行为连接到场景优先级和优化方向。未来，我希望它发展成 AI 体验监控台，持续跟踪核心行为、问题归因和场景变化，加入告警与实验结果，让每一项产品优化都能够回到数据中接受验证。

</details>

---

<a id="agent-skills"></a>
## 🧠 Agent Skills

当一条有用的工作流反复出现时，我会把其中的判断沉淀成可复用 Skill。

| 项目 | 产品想法 | Stars |
|---|---|---:|
| [**readme-craft**](https://github.com/okht/readme-craft) | 从仓库证据出发创建和维护公开 README，并完成多语言与视觉验证 | [![Stars](https://img.shields.io/github/stars/okht/readme-craft?style=social)](https://github.com/okht/readme-craft) |
| [**desktop-organizer**](https://github.com/okht/desktop-organizer) | 通过 dry-run、明确批准、安全移动和结果验证整理 Windows 文件夹 | [![Stars](https://img.shields.io/github/stars/okht/desktop-organizer?style=social)](https://github.com/okht/desktop-organizer) |
| [**become-master**](https://github.com/okht/become-master) | 把陌生领域压缩成有优先级的谈资和 30 秒记忆卡 | [![Stars](https://img.shields.io/github/stars/okht/become-master?style=social)](https://github.com/okht/become-master) |
| [**ai-dev-context-framework**](https://github.com/okht/ai-dev-context-framework) | 在编码 Agent 的多次会话中保留产品意图、权限、决策和任务状态 | [![Stars](https://img.shields.io/github/stars/okht/ai-dev-context-framework?style=social)](https://github.com/okht/ai-dev-context-framework) |

<details>
<summary><strong>readme-craft</strong> — 让公开文档证明仓库真正具备的能力。</summary>

<br>

我做 `readme-craft`，源于自己整理公开项目时不断遇到同一组发布问题。每次都需要重新判断首屏结构、徽章配色、章节顺序、多语言导航、表格宽度和 Mermaid 尺寸；项目数量增加后，仅靠临时判断很难保持稳定。我希望建立一套可以重复使用的公开发布标准，让 README 的质量不再依赖某一次发挥。

我把「证据驱动设计」设为核心原则。Skill 会先检查代码、清单、版本、工作流、许可证和仓库状态，形成可以核查的事实，再组织文案、视觉与多语言内容。配套验证器负责检查链接、锚点、语言页面、图示样式和私人路径，渲染预览则继续验证真实页面中的布局效果。这样，视觉完整度和内容可信度可以沿着同一条工作流持续检查。

我主要希望它服务独立开发者和项目维护者，帮助他们为不同类型的公开项目建立清晰、可信且易于维护的入口。未来，我希望 `readme-craft` 发展成 README 维护系统，能够感知仓库变化、发现内容漂移，并在项目演进过程中持续提醒和修正公开文档。

</details>

<details>
<summary><strong>desktop-organizer</strong> — 在任何文件移动之前看清完整计划。</summary>

<br>

我做 `desktop-organizer`，源于自己对桌面整理的实际需求。文档、截图、安装包、压缩文件和代码项目长期堆在同一个空间里，手工整理需要反复判断，直接交给自动化又会带来错误分类、文件覆盖和误操作风险。只要处理对象是真实文件，我就希望在执行前看清每一次移动，并保留最后决定权。

因此，我把工作流设计成「检查、计划、批准、执行、验证」。系统默认只生成 dry-run 方案，得到明确批准后才会移动文件，执行结束后继续报告成功、跳过和失败的项目。它不提供删除与覆盖操作，发现目标冲突时会提前停止；快捷方式和系统文件保持原位，无法确定的内容进入待复核区。整个过程仅在本地完成，也不需要网络请求。

我主要希望它服务 Windows 桌面重度用户，让他们在保持控制感的前提下恢复清晰的工作空间。未来，我希望它发展成个性化分类系统，允许每个人保存自己的目录结构、判断规则和例外清单，让安全整理逐渐适应长期使用习惯。

</details>

<details>
<summary><strong>become-master</strong> — 用五分钟找到进入对话的落脚点。</summary>

<br>

我做 `become-master`，起源于一位做技术的朋友。他在专业能力上很投入，却不太擅长快速融入社交场景；和同事相处、与喜欢的人聊天时，他常常找不到共同话题，交流很容易冷下来。我发现，大量资料仍然无法解决他的临场问题，他需要一条能够在有限时间内找到高价值信息、进入对话并继续追问的路径。

因此，我把输入设计成「领域 + 真实场景」，再输出术语、产品、核心判断、谈资、常见误区和应对方式。这个 Skill 最重要的取舍是强制压缩：大量信息会被重新排列优先级，最终收束成一张 18 节点记忆卡，让用户可以在见面前迅速复习。它的价值在于帮助用户听懂话题、找到自然入口，并在知识有限时继续提出真诚的问题。

我主要希望它服务即将进入聚会、工作交流或关系沟通场景的临场准备者。未来，我希望它发展成个人社交准备助手，结合交流对象、关系阶段和具体场合，帮助用户发现可能的共同兴趣，准备自然的开场、追问和话题延续方式。

</details>

<details>
<summary><strong>ai-dev-context-framework</strong> — 让编码 Agent 在多次会话中保持同一个方向。</summary>

<br>

我做 `ai-dev-context-framework`，是因为编码 Agent 在跨会话开发中很容易失去连续性。产品意图、技术约束、架构选择和任务状态散落在聊天与临时文件里，新会话开始后往往需要重新解释；当项目变复杂时，Agent 还可能在维护进度的过程中触碰已经确认的重要决定。

我选择用 Markdown 契约来组织这套上下文。产品讨论先沉淀为 `SPEC.md`，随后生成 Agent 入口、任务队列，并按项目复杂度加入架构、数据、设计、问题、决策和交接文件。锁定区与生成区表达不同的维护权限，Full 和 Lite 两个版本则对应长期复杂项目与短周期项目。Markdown 让规则同时具备可读性、可迁移性和版本记录能力；当前约束仍依赖 Agent 主动遵循，这也是框架公开说明的能力边界。

我主要希望它服务复杂项目维护者，让需求、决定和进度在多次会话中持续可追溯。未来，我希望它发展成 Agent 项目治理层，进一步检查上下文一致性、权限边界、决策记录和恢复点，让复杂项目能够在长期人机协作中保持方向。

</details>

---

<a id="principles"></a>
## 🧭 我的产品原则

| 原则 | 实际含义 |
|---|---|
| **从亲身摩擦出发** | 一个项目应该始于我可以具体描述的问题 |
| **让证据保持可见** | 假设、成本、失败实验和能力边界应该和结果一起出现 |
| **让控制边界清楚** | 本地文件、私人账户和不可逆决定需要明确的权限规则 |
| **压缩交互界面** | 最小且有用的交互往往更适合长期使用 |
| **为复用而设计** | 一条重复工作流值得沉淀成工具、框架或 Skill |
| **保持长期主义** | 我重视能够随时间积累的系统、知识与资产 |

---

<a id="stack"></a>
## 🛠 我使用的工具

`Python` · `JavaScript` · `Jupyter Notebook` · `PowerShell` · `Markdown` · `Mermaid` · `Codex` · `Claude Code` · `AgentSkills`

---

<div align="center">

### **从真实问题出发，诚实衡量结果，保留能够长期积累的东西。**

感谢你来到这里。欢迎继续看看任何让你感兴趣的项目。

</div>
