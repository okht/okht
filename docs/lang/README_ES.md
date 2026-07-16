<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=000000&center=true&vCenter=true&random=false&width=820&lines=Construyo%20a%20partir%20de%20problemas%20reales.;Agent%20%C2%B7%20C%C3%B3digo%20%C2%B7%20Datos.;Materializo%20ideas%20para%20que%20se%20puedan%20probar%20y%20reutilizar." alt="Introducción animada" />
</p>

<div align="center">

# 👋 Hola, soy CHT.

### *Gestor de producto · Desarrollador guiado por mis intereses*

<p align="center">
  <a href="https://www.polyu.edu.hk/"><img src="../../assets/education/the-hong-kong-polytechnic-university.png" alt="Universidad Politécnica de Hong Kong" height="42" /></a>
</p>

[![Seguidores en GitHub](https://img.shields.io/github/followers/okht?style=social&label=Seguidores)](https://github.com/okht) [![Estrellas totales de GitHub](https://img.shields.io/github/stars/okht?style=social&label=Stars)](https://github.com/okht?tab=repositories)

<br>

<table>
<tr><td align="left">

🧩 &nbsp;Creo software cuando una acción repetida merece un producto.<br>
📊 &nbsp;Uso datos cuando la intuición necesita evidencia.<br>
🧠 &nbsp;Creo Agent Skills cuando un flujo de trabajo merece acumular valor.

</td></tr>
</table>

### ✨ Convierto problemas reales en productos que se pueden usar, medir y mejorar.

**Curiosidad → criterio de producto → código o análisis → sistema reutilizable**

<br>

[👋 Acerca de mí](#about) · [💻 Software](#software-development) · [📊 Datos](#data-analytics) · [🧠 Agent Skills](#agent-skills) · [🧭 Principios](#principles) · [🛠 Herramientas](#stack)

[**English**](../../README.md) · [**简体中文**](README_ZH.md) · [**Español**](README_ES.md) · [**Deutsch**](README_DE.md) · [**日本語**](README_JA.md) · [**Русский**](README_RU.md) · [**Português**](README_PT.md) · [**한국어**](README_KO.md)

</div>

---

### 📬 Encuéntrame

[![Website](https://img.shields.io/badge/-cht.me-FFFFFF?style=for-the-badge)](https://cht.me)

---

<a id="about"></a>
## 👋 Acerca de mí

Hola, soy CHT. Me gradué en la Universidad Politécnica de Hong Kong. Soy gestor de producto y desarrollador guiado por mis intereses, y exploro agentes de IA, software y analítica de datos mediante proyectos de código abierto.

Me gusta partir de un problema real: una acción repetitiva, una pregunta de producto poco definida o un flujo de trabajo que pierde contexto una y otra vez. Lo convierto en un producto y después uso código y datos para hacerlo tangible y comprobable.

Este perfil recorre tres líneas de trabajo. Cada repositorio comienza con un problema concreto y refleja mi criterio de producto sobre los equilibrios, la evidencia y aquello en lo que el producto podría convertirse.

| Línea de trabajo | Lo que me importa |
|---|---|
| **Desarrollo de software** | Eliminar fricciones recurrentes con herramientas pequeñas y útiles |
| **Analítica de datos** | Hacer visibles los supuestos, costes, fallos y decisiones |
| **Agent Skills** | Convertir flujos repetibles en sistemas reutilizables |

---

<a id="software-development"></a>
## 💻 Desarrollo de software

Creo herramientas específicas para problemas que he encontrado de primera mano.

| Proyecto | Idea de producto | Estrellas |
|---|---|---:|
| [**clip-md**](https://github.com/okht/clip-md) | Guardar respuestas valiosas de IA como Markdown local con un clic y sin interrumpir el hilo de pensamiento | [![Estrellas](https://img.shields.io/github/stars/okht/clip-md?style=social&label=Estrellas)](https://github.com/okht/clip-md) |
| [**gmail-inbox-system-public**](https://github.com/okht/gmail-inbox-system-public) | Convertir Gmail en un centro prudente para varios buzones mediante etiquetas combinables y archivado protegido | [![Estrellas](https://img.shields.io/github/stars/okht/gmail-inbox-system-public?style=social&label=Estrellas)](https://github.com/okht/gmail-inbox-system-public) |
| [**okx-btc-daily-report-public**](https://github.com/okht/okx-btc-daily-report-public) | Recalcular las métricas de DCA de BTC que me importan a partir de datos de operaciones consultados con acceso de solo lectura y enviarlas por correo electrónico | [![Estrellas](https://img.shields.io/github/stars/okht/okx-btc-daily-report-public?style=social&label=Estrellas)](https://github.com/okht/okx-btc-daily-report-public) |

<details>
<summary><strong>clip-md</strong> — Copia lo que importa. Consérvalo como Markdown.</summary>

<br>

Creé `clip-md` después de sentir repetidamente la fricción de guardar contenido útil de IA. ChatGPT, Claude y otras herramientas suelen producir respuestas que merecen la pena conservar, y quería que pasaran a formar parte de mi base de conocimiento local. El flujo anterior exigía un editor, un archivo nuevo, una ubicación, un nombre y un guardado final. Esa secuencia era lo bastante larga como para interrumpir la idea que intentaba preservar.

Reduje la interacción central a una acción pequeña: copiar texto, usar el control que aparece cerca del puntero y guardarlo directamente como Markdown local. El nombrado automático también es una elección deliberada. La aplicación extrae palabras clave y recurre a una cadena de alternativas cuando la extracción es débil, con lo que elimina otra decisión y mantiene los archivos legibles y fáciles de buscar.

Quiero que `clip-md` sirva a quienes usan IA con frecuencia y a los trabajadores del conocimiento. Su rumbo se mantiene deliberadamente ligero: mejorar la fiabilidad, la adaptación a cada plataforma, la distribución firmada y esos detalles discretos que permiten que una herramienta de escritorio siga siendo útil durante mucho tiempo.

</details>

<details>
<summary><strong>gmail-inbox-system-public</strong> — Una bandeja de entrada, varios significados y automatización controlada.</summary>

<br>

Creé Gmail Inbox System después de redirigir varios buzones a Gmail. Tuve que cambiar menos entre cuentas, pero la bandeja empezó a perder el significado del origen y de la acción pendiente. Las notificaciones de aplicaciones, facturas, alertas de seguridad, mensajes personales y tareas pendientes llegaban en un único flujo, mientras que las etiquetas anteriores mezclaban origen, tipo de contenido y estado de una manera cada vez más difícil de mantener.

Separé el sistema de etiquetas en dimensiones combinables: aplicación, tipo, origen y estado expresan cada uno un único significado. Un mensaje puede conservar de dónde viene, qué contiene y qué acción requiere. La clasificación, la vista previa, los periodos de retención y las reglas de protección forman controles explícitos antes del archivado, mientras que los mensajes cuya clasificación es incierta permanecen visibles.

Quiero que este sistema se convierta en mi centro personal de correo electrónico, con Gmail como entrada unificada y resúmenes diarios generados por IA como futura capa. El repositorio público contiene reglas y ejemplos reutilizables que cuidan la privacidad; no contiene mensajes privados, credenciales de cuentas ni acceso a mis buzones activos.

</details>

<details>
<summary><strong>okx-btc-daily-report-public</strong> — Mi estrategia de DCA, medida según mis propios criterios.</summary>

<br>

Creé OKX BTC Daily Report porque sigo mi propia estrategia de DCA de BTC. El plan integrado de la plataforma de intercambio no coincidía con las reglas ni con el ritmo que quería, y su panel fijo no podía responder las preguntas que me importaban, como el rendimiento a 30 días, la inversión prevista frente a la real y el resultado después de ejecuciones y comisiones.

El flujo de trabajo lee datos de operaciones mediante acceso de solo lectura y vuelve a calcular vistas diarias, de 7 días, de 30 días y acumuladas con mis propias definiciones. Las ejecuciones parciales, las comisiones y las divisas de cotización hacen que el seguimiento manual se desvíe con el tiempo, así que las reglas deben ejecutarse de forma constante. Elegí el envío por correo electrónico porque el informe debe llegar dentro de una rutina existente sin obligarme a mantener otro panel.

Quiero que evolucione hacia una consola personal de datos de inversión que cubra más activos, periodos, métricas y visualizaciones. El repositorio público es una implementación de referencia saneada: no contiene claves de API, no tiene acceso a mi cuenta de OKX y no ejecuta operaciones.

</details>

---

<a id="data-analytics"></a>
## 📊 Analítica de datos

Uso el análisis para cuestionar la intuición, registrar la incertidumbre y facilitar la revisión de las decisiones.

> Los proyectos de inversión y trading documentan investigación personal. No ofrecen asesoría financiera.

| Proyecto | Idea de producto | Estrellas |
|---|---|---:|
| [**quant-research**](https://github.com/okht/quant-research) | Un marco de investigación reutilizable que registra supuestos, costes, experimentos fallidos y límites de validación | [![Estrellas](https://img.shields.io/github/stars/okht/quant-research?style=social&label=Estrellas)](https://github.com/okht/quant-research) |
| [**crypto-trading-research**](https://github.com/okht/crypto-trading-research) | Comprobar si las estrategias activas de BTC aportan suficiente valor para justificar su coste y esfuerzo frente a mantenerlo a largo plazo | [![Estrellas](https://img.shields.io/github/stars/okht/crypto-trading-research?style=social&label=Estrellas)](https://github.com/okht/crypto-trading-research) |
| [**ecommerce-user-analysis**](https://github.com/okht/ecommerce-user-analysis) | Convertir transacciones históricas en segmentos de clientes e hipótesis de crecimiento mediante RFM y K-Means | [![Estrellas](https://img.shields.io/github/stars/okht/ecommerce-user-analysis?style=social&label=Estrellas)](https://github.com/okht/ecommerce-user-analysis) |
| [**ai-chat-analytics**](https://github.com/okht/ai-chat-analytics) | Conectar el comportamiento conversacional, la atribución de problemas y las señales de seguimiento con las prioridades de producto de IA | [![Estrellas](https://img.shields.io/github/stars/okht/ai-chat-analytics?style=social&label=Estrellas)](https://github.com/okht/ai-chat-analytics) |

<details>
<summary><strong>quant-research</strong> — Conservar la evidencia, incluidos los fallos.</summary>

<br>

Creé `quant-research` para convertir ideas de inversión en hipótesis que los datos puedan cuestionar. Una estrategia puede parecer razonable y aun así depender de un único periodo favorable. Quiero ver qué datos utilizó, cómo formó las señales, de dónde procedieron los rendimientos y cuánto se mantiene al cambiar los periodos, parámetros y modelos.

Presto especial atención al sobreajuste y a las cadenas de investigación fragmentadas. Las búsquedas de parámetros pueden producir resultados atractivos dentro de la muestra, mientras que el código, los datos y los resultados temporales van perdiendo su conexión. Conservo factores débiles, modelos fallidos y estrategias deterioradas, y evalúo costes, atribución, caída máxima y comportamiento fuera de muestra junto al rendimiento. Un experimento fallido también revela qué camino carece de evidencia duradera.

Quiero que `quant-research` se convierta en un marco reutilizable para instantáneas, hipótesis, señales, pruebas históricas, validación y hallazgos registrados. Así, nuevos mercados y modelos pueden entrar en la misma estructura y hacer que mi investigación personal sea acumulativa, comparable y revisable.

</details>

<details>
<summary><strong>crypto-trading-research</strong> — ¿Puede la operativa activa con BTC compensar su complejidad?</summary>

<br>

Creé `crypto-trading-research` en torno a una pregunta que afecta directamente a mis decisiones: después de contar comisiones, deslizamiento, rotación y atención, ¿mantener BTC a largo plazo ya es la estrategia de menor coste y esfuerzo? La operativa activa y el aprendizaje automático pueden parecer sofisticados, aunque la complejidad por sí sola no demuestra valor adicional.

Uso la tenencia a largo plazo como referencia permanente y después comparo con ella indicadores clásicos, señales estadísticas y modelos de aprendizaje automático. Los costes son explícitos porque una rotación frecuente puede borrar una ventaja sobre el papel. Los periodos y supuestos de comisiones permanecen visibles, y las métricas del modelo todavía deben convertirse en rendimientos reales de la estrategia. Los experimentos con MA, RSI, Bollinger Bands y XGBoost permanecen en el repositorio incluso cuando sus resultados son débiles.

Quiero que el proyecto se convierta en una base de evidencia para decisiones sobre BTC que siga examinando la misma pregunta con datos nuevos y distintos regímenes de mercado. Cada conclusión permanece ligada a su periodo de muestra, supuesto de costes y método de validación para que otra persona pueda revisar todo el recorrido.

</details>

<details>
<summary><strong>ecommerce-user-analysis</strong> — Ver a los clientes ocultos dentro de las métricas agregadas.</summary>

<br>

Creé `ecommerce-user-analysis` para entender cómo los registros de transacciones se convierten en segmentos de clientes con significado. Los ingresos, el número de pedidos y el valor medio por pedido describen el negocio completo, pero comprimen las diferencias entre clientes fieles, clientes que se alejan, recién llegados prometedores y personas que necesitan una estrategia distinta.

Uso RFM para crear una segmentación de negocio interpretable y después K-Means para examinar la estructura natural de los datos. Juntos mantienen un lenguaje operativo claro y añaden una segunda perspectiva analítica. El proyecto parte de más de un millón de transacciones históricas, recorre la limpieza, exploración, segmentación y visualización, y convierte el resultado en hipótesis de retención, reactivación y conversión.

Quiero que evolucione hacia una consola de analítica de crecimiento para comercio electrónico que siga cómo cambian los segmentos, qué métricas importan para cada grupo y qué experimentos de crecimiento modifican realmente el comportamiento.

</details>

<details>
<summary><strong>ai-chat-analytics</strong> — Convertir señales conversacionales en prioridades de producto.</summary>

<br>

Creé `ai-chat-analytics` porque los 「me gusta」, 「no me gusta」, reintentos y preguntas de seguimiento no indican directamente a un equipo de producto de IA qué debe corregir primero, por qué los usuarios están insatisfechos o si una mejora cambió la experiencia. Etiquetas amplias como 「calidad general」 pueden localizar un problema y dejar su causa poco clara.

Dividí el trabajo en generación de datos sintéticos, análisis de comportamiento, atribución de problemas, señales de seguimiento y síntesis de hallazgos. Una semilla fija hace reproducible la instantánea pública sin exponer conversaciones reales. Las reglas transparentes de palabras clave establecen una referencia explicable y muestran su propio límite: el 71,2 % de los casos problemáticos actuales sigue dentro de una categoría genérica y la validación manual continúa incompleta.

Quiero que el proyecto sirva a responsables de producto de IA y crezca hasta convertirse en una consola de seguimiento de la experiencia con IA, con métricas continuas, calidad de atribución, alertas y resultados de experimentos conectados en un único lugar.

</details>

---

<a id="agent-skills"></a>
## 🧠 Agent Skills

Cuando se repite un flujo de trabajo útil, convierto el criterio que contiene en una Skill reutilizable.

| Proyecto | Idea de producto | Estrellas |
|---|---|---:|
| [**readme-craft**](https://github.com/okht/readme-craft) | Crear y mantener README públicos a partir de la evidencia del repositorio, con validación multilingüe y visual | [![Estrellas](https://img.shields.io/github/stars/okht/readme-craft?style=social&label=Estrellas)](https://github.com/okht/readme-craft) |
| [**desktop-organizer**](https://github.com/okht/desktop-organizer) | Organizar carpetas de Windows mediante un dry-run, aprobación explícita, movimientos seguros y verificación | [![Estrellas](https://img.shields.io/github/stars/okht/desktop-organizer?style=social&label=Estrellas)](https://github.com/okht/desktop-organizer) |
| [**become-master**](https://github.com/okht/become-master) | Comprimir un campo desconocido en temas de conversación priorizados y una ficha de repaso de 30 segundos | [![Estrellas](https://img.shields.io/github/stars/okht/become-master?style=social&label=Estrellas)](https://github.com/okht/become-master) |
| [**ai-dev-context-framework**](https://github.com/okht/ai-dev-context-framework) | Preservar la intención de producto, los permisos, las decisiones y el estado de las tareas entre sesiones con agentes de programación | [![Estrellas](https://img.shields.io/github/stars/okht/ai-dev-context-framework?style=social&label=Estrellas)](https://github.com/okht/ai-dev-context-framework) |

<details>
<summary><strong>readme-craft</strong> — Hacer que la documentación pública demuestre lo que puede hacer un repositorio.</summary>

<br>

Creé `readme-craft` después de tomar repetidamente las mismas decisiones de publicación en distintos proyectos públicos. La estructura de presentación, los colores de las insignias, el orden de las secciones, la navegación entre idiomas, el ancho de las tablas, el tamaño de Mermaid y las comprobaciones de privacidad exigían cada vez un nuevo criterio manual. Quería un estándar de publicación reutilizable cuya calidad pudiera mantenerse estable entre repositorios.

El diseño guiado por evidencia es el principio central. La Skill inspecciona código, manifiestos, versiones, flujos de trabajo, licencias y el estado del repositorio antes de escribir. Un validador comprueba enlaces, anclas, equivalencia entre idiomas, diagramas y rutas privadas, mientras que las vistas previas renderizadas cubren el diseño visual que no puede demostrarse inspeccionando únicamente el código fuente.

Quiero que `readme-craft` sirva a desarrolladores independientes y mantenedores, y que después crezca hasta convertirse en un sistema de mantenimiento de README capaz de detectar cambios en el repositorio y desviaciones de contenido con el tiempo.

</details>

<details>
<summary><strong>desktop-organizer</strong> — Ver cada movimiento antes de mover nada.</summary>

<br>

Creé `desktop-organizer` a partir de mi propia necesidad de limpiar un escritorio de Windows lleno de documentos, capturas de pantalla, instaladores, archivos comprimidos y proyectos de código. La clasificación manual requería decisiones repetidas, mientras que la automatización directa introducía riesgos de clasificación incorrecta, sobrescrituras y operaciones no deseadas sobre los archivos.

El flujo de trabajo consiste en inspeccionar, planificar, aprobar, ejecutar y verificar. Su modo predeterminado solo imprime un dry-run; cualquier movimiento requiere aprobación explícita. No elimina ni sobrescribe archivos, los conflictos detienen pronto la ejecución, los accesos directos y archivos del sistema permanecen en su sitio, los elementos dudosos entran en una bandeja de revisión y todo el trabajo se mantiene en local.

Quiero que sirva a usuarios intensivos del escritorio de Windows y evolucione hacia un sistema de clasificación personalizado en el que cada persona pueda conservar su propia taxonomía, reglas y listas de excepciones.

</details>

<details>
<summary><strong>become-master</strong> — Cinco minutos para orientarte en una conversación.</summary>

<br>

Creé `become-master` después de ver cómo un amigo cercano del sector tecnológico tenía dificultades para incorporarse a conversaciones sociales. Era capaz y curioso, pero las conversaciones con colegas o con alguien que le gustaba podían estancarse porque no encontraba rápidamente temas en común. Las búsquedas le daban mucha información y muy pocas prioridades.

La Skill comienza con un campo y una situación real, y después organiza términos, productos, criterios, temas de conversación, errores comunes y formas de retomar el hilo. Su elección más importante es la compresión forzada: un campo amplio termina condensado en una ficha de repaso de 18 nodos que puede consultarse justo antes de conversar. El rumbo que me importa es una preparación honesta, escuchar mejor y hacer preguntas más naturales.

Quiero que se convierta en un asistente personal de preparación social que use la relación y el contexto para ayudar a descubrir intereses comunes, preparar formas de iniciar la conversación y mantenerla en movimiento con naturalidad.

</details>

<details>
<summary><strong>ai-dev-context-framework</strong> — Mantener alineados a los agentes de programación entre sesiones.</summary>

<br>

Creé `ai-dev-context-framework` porque los agentes de programación pueden perder continuidad entre sesiones. La intención de producto, las restricciones técnicas, las decisiones de arquitectura y el estado de las tareas acaban dispersos entre conversaciones y archivos temporales. A medida que un proyecto crece, las actualizaciones rutinarias de progreso también pueden alcanzar decisiones que deben permanecer bajo el control del usuario.

Elegí contratos Markdown para la capa de contexto. La conversación de producto se convierte en `SPEC.md` y después el marco crea un punto de entrada para el agente, una cola de tareas y archivos adicionales de arquitectura, datos, diseño, incidencias, decisiones y transferencia de contexto cuando la complejidad del proyecto lo exige. Las regiones bloqueadas y generadas expresan límites de mantenimiento, mientras que las ediciones Full y Lite cubren proyectos de distintos tamaños. Las protecciones actuales siguen siendo convenciones que dependen del cumplimiento por parte del agente.

Quiero que el marco sirva a quienes mantienen proyectos complejos y crezca hasta convertirse en una capa de gobierno de proyectos con agentes que compruebe la coherencia del contexto, los límites de permisos, los registros de decisiones y los puntos fiables de reanudación.

</details>

---

<a id="principles"></a>
## 🧭 Cómo construyo

| Principio | Qué significa en la práctica |
|---|---|
| **Partir de una fricción vivida** | Un proyecto debe comenzar con un problema que pueda describir de forma concreta |
| **Hacer visible la evidencia** | Los supuestos, costes, experimentos fallidos y límites deben aparecer junto a los resultados |
| **Mantener claro el control** | Los archivos locales, las cuentas privadas y las decisiones irreversibles necesitan límites explícitos |
| **Comprimir la interfaz** | La interacción útil más pequeña suele ser la más duradera |
| **Diseñar para reutilizar** | Un flujo de trabajo repetido debe convertirse en una herramienta, un marco o una Skill |
| **Pensar a largo plazo** | Valoro los sistemas, conocimientos y activos que pueden acumular valor con el tiempo |

---

<a id="stack"></a>
## 🛠 Stack tecnológico

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000000)
![Jupyter](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![PowerShell](https://img.shields.io/badge/-PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Mermaid](https://img.shields.io/badge/-Mermaid-FF3670?style=for-the-badge&logo=mermaid&logoColor=white)
![Codex](https://img.shields.io/badge/-Codex-000000?style=for-the-badge&logo=openai&logoColor=white)
![Claude Code](https://img.shields.io/badge/-Claude%20Code-D97757?style=for-the-badge)
![AgentSkills](https://img.shields.io/badge/-AgentSkills-8B5CF6?style=for-the-badge)

---

<div align="center">

### **Construir desde problemas reales. Medir con honestidad. Conservar lo que acumula valor.**

Gracias por pasar por aquí. Explora cualquier proyecto que te llame la atención.

</div>
