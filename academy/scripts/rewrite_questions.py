#!/usr/bin/env python3
"""Rewrite quiz options: near-miss distractors of similar length; spread keys A–D."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "questions.json"

# First `select` entries are the correct answer(s); remaining are distractors.
# English and Spanish lists must be the same length and same correctness order.
OPTS: dict[str, dict[str, list[str]]] = {}


def add(qid: str, en: list[str], es: list[str]) -> None:
    assert len(en) == 4 and len(es) == 4, qid
    OPTS[qid] = {"en": en, "es": es}


add(
    "q001",
    [
        "Anthropic’s family of models plus the applications that sit on those models",
        "Anthropic’s family of models only; Chat, Cowork, and Code are unrelated third-party shells",
        "Anthropic’s applications (Chat, Cowork, Code) only; Haiku, Sonnet, and Opus come from another vendor",
        "Anthropic Partner Academy and Skilljar courses; the models are a separate Pearson product line",
    ],
    [
        "La familia de modelos de Anthropic más las aplicaciones que se apoyan en esos modelos",
        "Solo la familia de modelos; Chat, Cowork y Code son envoltorios de terceros sin relación de producto",
        "Solo las aplicaciones (Chat, Cowork, Code); Haiku, Sonnet y Opus vienen de otro proveedor",
        "Solo Partner Academy y Skilljar; los modelos son una línea aparte de Pearson",
    ],
)
add(
    "q002",
    [
        "Claude Cowork (or Code/SDK): Chat summarises in the thread and does not reorganise folders on disk",
        "Claude Chat: uploading a file already grants write access so it can create month-wise folders locally",
        "Claude Chat with stream=true: tokens are written as files next to the original deck as they arrive",
        "Anthropic Academy / Skilljar: finishing the module mounts a workspace that tidies Downloads for you",
    ],
    [
        "Claude Cowork (o Code/SDK): Chat resume en el hilo y no reorganiza carpetas en disco",
        "Claude Chat: subir un fichero ya da escritura local, así que puede crear carpetas por mes",
        "Claude Chat con stream=true: los tokens se escriben como ficheros junto a la presentación",
        "Anthropic Academy / Skilljar: terminar el módulo monta un espacio que ordena Downloads",
    ],
)
add(
    "q003",
    [
        "Chat is primary on the web; Cowork was taught as a desktop client; Code uniquely has CLI and IDE integration",
        "Cowork is the primary web app; Code exists only as a Chrome extension; Chat is CLI-only in class",
        "Chat, Cowork, and Code are identical tiles on claude.ai and also identical in every IDE side panel",
        "Code is web-only in class; Cowork is the only product that ships a CLI; Chat is desktop-only",
    ],
    [
        "Chat es el cliente web principal; Cowork se enseñó como escritorio; Code aporta CLI e IDE",
        "Cowork es la app web principal; Code solo existe como extensión de Chrome; Chat es solo CLI",
        "Chat, Cowork y Code son mosaicos idénticos en claude.ai y en cualquier panel de IDE",
        "Code es solo web; Cowork es el único con CLI; Chat es solo de escritorio",
    ],
)
add(
    "q004",
    [
        "The Messages API needs a console API key; that plane is separate from Chat login, billing, and rate limits",
        "Chat login and the console API key are the same credential, so a working Chat session proves the SDK is broken",
        "The SDK authenticates only inside Claude Cowork’s sandbox folder; notebooks outside that folder always 401",
        "Percipio completion is what mints API keys; until the LMS shows 100%, messages.create cannot authenticate",
    ],
    [
        "La API Messages pide una clave de consola; ese plano es distinto del login, facturación y límites de Chat",
        "El login de Chat y la clave de consola son la misma credencial: si Chat va, el SDK tiene que estar roto",
        "El SDK solo autentica dentro de la carpeta sandbox de Cowork; un notebook fuera siempre da 401",
        "Percipio es lo que emite claves; hasta el 100% en el LMS, messages.create no puede autenticar",
    ],
)
add(
    "q005",
    [
        "Claude Certified Developer, Foundation (CCDV-F): APIs, Code, MCP, prompting, a taste of Agent SDK",
        "Claude Certified Architect, Professional: developers skip Foundation and sit only the architect paper",
        "The Percipio completion badge: Anthropic treats LMS 100% as the proctored Pearson sitting",
        "Claude Certified Associate / business Foundation: prompting is the whole CCDV-F blueprint",
    ],
    [
        "Claude Certified Developer, Foundation (CCDV-F): APIs, Code, MCP, prompting y una cata de Agent SDK",
        "Claude Certified Architect, Professional: quien programa se salta Foundation y solo sienta architect",
        "La insignia Percipio: Anthropic trata el 100% del LMS como la convocatoria proctorizada Pearson",
        "Claude Certified Associate / Foundation de negocio: el prompting es todo el temario CCDV-F",
    ],
)
add(
    "q006",
    [
        "Job (1) can stay in Claude Chat if a summary or draft in the thread is enough",
        "Job (2) is Cowork’s job (agentic local workspace), not Chat’s",
        "Claude Chat will silently move files on disk whenever a PDF is uploaded for summarising",
        "Cowork can only run inside VS Code, so job (2) cannot start without an IDE session",
    ],
    [
        "El trabajo (1) puede quedarse en Claude Chat si basta un resumen o borrador en el hilo",
        "El trabajo (2) es de Cowork (espacio local agente), no de Chat",
        "Claude Chat mueve en silencio ficheros en disco cada vez que se sube un PDF para resumir",
        "Cowork solo corre dentro de VS Code, así que el (2) no arranca sin una sesión de IDE",
    ],
)
add(
    "q007",
    [
        "About 60 questions in 120 minutes, MCQ plus written scenarios — you do not ship a production app in an exam IDE",
        "A 48-hour take-home where you must publish a public MCP marketplace listing to pass",
        "Only a live pair-programming interview with Opus, scored by a human architect on a call",
        "Unlimited time, ten fill-in-the-blank regex items, no multiple choice at all",
    ],
    [
        "Unas 60 preguntas en 120 minutos, test más escenarios escritos: no se entrega una app de producción en un IDE de examen",
        "Un trabajo de 48 horas en casa donde hay que publicar un listing público en el marketplace MCP",
        "Solo una entrevista de programación en pareja con Opus, puntuada por un arquitecto en llamada",
        "Tiempo ilimitado, diez ítems de rellenar regex, sin opción múltiple",
    ],
)
add(
    "q008",
    [
        "Message Batches (async, classroom stem: up to a ~24-hour window) instead of a burst of interactive calls",
        "Fire 10,000 synchronous Messages.create calls in a tight parallel loop so the overnight job finishes in minutes",
        "Put all 10,000 PDFs in one user message and stream a single combined answer to minimise request count",
        "Switch Claude Chat to Cowork so the desktop five-hour usage bar becomes an unlimited batch queue",
    ],
    [
        "Message Batches (asíncrono; en clase, ventana ~24 h) en vez de un chorro de llamadas interactivas",
        "Lanzar 10.000 Messages.create síncronos en un bucle paralelo para acabar el lote en minutos",
        "Meter los 10.000 PDF en un solo mensaje de usuario y hacer stream de una respuesta combinada",
        "Pasar Chat a Cowork para que la barra de 5 h del escritorio se convierta en cola ilimitada",
    ],
)
add(
    "q009",
    [
        "The Messages API is stateless; the application must resend the history it wants the model to see",
        "The model server stores every API conversation for 90 days, so the empty follow-up should still recall the name",
        "Display names are stripped on every turn unless temperature is exactly 0, so the second cell cannot retain them",
        "Cowork connectors must be enabled on the API key before any Messages call can remember proper nouns",
    ],
    [
        "La API Messages es sin estado; la aplicación debe reenviar el historial que quiere que el modelo vea",
        "El servidor guarda cada conversación de API 90 días, así que el seguimiento vacío debería recordar el nombre",
        "Los nombres se eliminan en cada turno salvo con temperature 0, así que la segunda celda no puede retenerlos",
        "Hay que activar conectores de Cowork en la clave antes de que Messages recuerde nombres propios",
    ],
)
add(
    "q010",
    [
        "As a separate system parameter on create; user and assistant turns live in messages[]",
        "As a third role named system inside the messages array, mixed with user and assistant turns",
        "Only inside CLAUDE.md, which the Messages API reads automatically from the default GitHub branch",
        "As a tool named system_prompt that Claude must call first before any user text is considered",
    ],
    [
        "Como parámetro system aparte en create; los turnos user y assistant viven en messages[]",
        "Como un tercer rol system dentro del array messages, mezclado con user y assistant",
        "Solo dentro de CLAUDE.md, que la API Messages lee sola de la rama por defecto de GitHub",
        "Como una herramienta system_prompt que Claude debe invocar antes de leer el texto de usuario",
    ],
)
add(
    "q011",
    [
        "You show tokens as they arrive (perceived latency) via server-sent events; you still pay for output tokens",
        "Streaming makes the model more capable and halves output-token prices compared with a finished Message",
        "stream=true is required before any tool_use block can appear; non-streaming calls cannot use tools",
        "Non-streaming create is deprecated and the console rejects it, so streaming is the only legal path",
    ],
    [
        "Mostráis tokens al llegar (latencia percibida) con SSE; seguís pagando los tokens de salida",
        "El streaming hace el modelo más capaz y reduce a la mitad el precio de los tokens de salida",
        "stream=true es obligatorio para que aparezca tool_use; sin streaming no hay herramientas",
        "create sin streaming está deprecado y la consola lo rechaza: el streaming es el único camino legal",
    ],
)
add(
    "q012",
    [
        "Use structured-output / JSON guidance (schema or prefill+stop as taught) so the consumer gets a tight envelope",
        "Ask only in prose, then regex the essay; never constrain decoding because schemas reduce quality",
        "Set temperature to 2.0 so the JSON is more creative and still machine-parseable without a schema",
        "Put the JSON schema in a Cowork folder named /json and let Chat discover it without API parameters",
    ],
    [
        "Usad salida estructurada / JSON (esquema o prefill+stop) para que el consumidor reciba un sobre cerrado",
        "Pedid solo en prosa y extraed con regex; no constriñáis la decodificación porque el esquema baja calidad",
        "Poned temperature 2.0 para que el JSON sea más creativo y siga parseable sin esquema",
        "Dejad el esquema JSON en una carpeta Cowork /json y que Chat lo descubra sin parámetros de API",
    ],
)
add(
    "q013",
    [
        "You waste tokens (and may exceed the context window); RAG retrieves only useful chunks then augments the prompt",
        "PDFs cannot legally be sent to Claude, so the only compliant design is to paste OCR into Chat by hand",
        "Claude can only inspect images, never document text, so a 1,000-page PDF must be screenshotted page by page",
        "You must use Cowork Design instead of any Messages call whenever the source file is a PDF",
    ],
    [
        "Malgastáis tokens (y podéis superar la ventana); RAG recupera trozos útiles y luego aumenta el prompt",
        "Los PDF no se pueden enviar a Claude; el único diseño válido es pegar OCR a mano en Chat",
        "Claude solo ve imágenes, nunca texto de documento, así que hay que capturar las 1.000 páginas",
        "Hay que usar Cowork Design en vez de Messages siempre que el origen sea un PDF",
    ],
)
add(
    "q014",
    [
        "Mark a large invariant prefix (document + stable instructions) with cache_control so later questions pay cache-hit prices for a short TTL",
        "Stand up a permanent customer RAG database that Anthropic hosts forever after the first PDF upload",
        "Skip sending the new user question at all; cache_control replays the previous answer for any follow-up",
        "Flip a Claude Code permission mode that auto-approves bash whenever a PDF is in the project",
    ],
    [
        "Marcar un prefijo invariante (documento + instrucciones) con cache_control para pagar precio de acierto un TTL corto",
        "Montar una base RAG permanente de cliente que Anthropic aloje para siempre tras el primer PDF",
        "Dejar de enviar la pregunta nueva; cache_control reutiliza la respuesta anterior en cualquier seguimiento",
        "Activar un modo de permisos de Claude Code que autoaprueba bash si hay un PDF en el proyecto",
    ],
)
add(
    "q015",
    [
        "When the user provides screenshots, photos, or diagrams the model should inspect as image blocks",
        "Never; Claude cannot accept images on the Messages API, so vision is Chat-desktop only",
        "Only after Message Batches has failed three times on the same PDF text extraction job",
        "Only inside Percipio quizzes; production Messages calls must paste OCR instead of image blocks",
    ],
    [
        "Cuando el usuario aporta capturas, fotos o diagramas que el modelo debe inspeccionar como bloques de imagen",
        "Nunca; Claude no acepta imágenes en la API Messages, así que la visión es solo del Chat de escritorio",
        "Solo después de que Message Batches haya fallado tres veces en la misma extracción de PDF",
        "Solo en cuestionarios Percipio; en producción Messages hay que pegar OCR en vez de bloques de imagen",
    ],
)
add(
    "q016",
    [
        "The application must show which retrieved or attached passage supports a claim",
        "You want the model to invent legal-looking footnotes even when no passage was retrieved",
        "You need to disable the context window so answers cite a hidden system corpus",
        "You are only choosing Haiku versus Opus in the desktop model picker, with no documents attached",
    ],
    [
        "La aplicación debe mostrar qué pasaje recuperado o adjunto respalda cada afirmación",
        "Queréis que el modelo invente notas al pie con aspecto legal aunque no se haya recuperado ningún pasaje",
        "Necesitáis desactivar la ventana de contexto para citar un corpus oculto del sistema",
        "Solo estáis eligiendo Haiku u Opus en el selector de escritorio, sin documentos adjuntos",
    ],
)
add(
    "q017",
    [
        "Text in, vector out — used to index chunks and to embed the query for similarity search; Claude still generates the answer",
        "Text in, long essay out — the embedding model is the same generative Claude call with temperature 0",
        "It replaces Messages.create entirely; once vectors exist you never call Claude for the user-facing answer",
        "It stores API keys inside each vector so later queries can skip the console credential",
    ],
    [
        "Texto entra, vector sale: indexa trozos y embebe la consulta; Claude sigue generando la respuesta",
        "Texto entra, ensayo largo sale: el modelo de embeddings es la misma llamada generativa a Claude con temperature 0",
        "Sustituye por completo a Messages.create: con vectores ya no llamáis a Claude para la respuesta",
        "Guarda claves de API dentro de cada vector para que las consultas posteriores no usen la consola",
    ],
)
add(
    "q018",
    [
        "Retrieve finds a few matching chunks; augment appends them to the prompt; generate is still Claude",
        "You typically embed the corpus once (prep), not on every question",
        "RAG replaces Claude so you never call an LLM after the first index build",
        "Chunk size is a universal constant (always 512 characters) for every corpus and language",
    ],
    [
        "Retrieve encuentra unos trozos; augment los añade al prompt; generate sigue siendo Claude",
        "Normalmente embebeis el corpus una vez (preparación), no en cada pregunta",
        "RAG sustituye a Claude: tras el primer índice nunca volvéis a llamar a un LLM",
        "El tamaño de chunk es una constante universal (siempre 512 caracteres) para cualquier corpus",
    ],
)
add(
    "q019",
    [
        "Similarity search returns neighbours as vectors; you still need the original prose to augment the prompt",
        "Anthropic requires chunk text to be stored only as PNG screenshots of the embedding plot",
        "Storing original text next to embeddings is forbidden because it would leak the vector space",
        "Claude reads the vectors directly as thinking blocks, so the original sentences can be discarded",
    ],
    [
        "La búsqueda por similitud devuelve vecinos vectoriales; aún hace falta la prosa original para aumentar el prompt",
        "Anthropic exige guardar el texto del chunk solo como capturas PNG del gráfico de embeddings",
        "Guardar texto junto a embeddings está prohibido porque filtraría el espacio vectorial",
        "Claude lee los vectores como bloques de pensamiento, así que las frases originales se pueden borrar",
    ],
)
add(
    "q020",
    [
        "Anthropic SDK is conversations / Messages API; Agent SDK is orchestration (loops, tools, memory) around those calls",
        "They are the same package; Agent SDK is only a Percipio quiz name for messages.create",
        "Agent SDK is required before you can set temperature on any Messages call",
        "Anthropic SDK only runs inside Claude Cowork; Agent SDK is the only option in notebooks",
    ],
    [
        "El SDK de Anthropic es conversaciones / Messages; el Agent SDK orquesta bucles, tools y memoria alrededor",
        "Son el mismo paquete; Agent SDK es solo el nombre Percipio de messages.create",
        "El Agent SDK es obligatorio antes de poder fijar temperature en cualquier llamada Messages",
        "El SDK de Anthropic solo corre dentro de Cowork; en notebooks solo vale el Agent SDK",
    ],
)
add(
    "q021",
    [
        "Attach the high-value spec (and maybe a logo), not the entire backend tree, to save context tokens",
        "YAML files cannot consume tokens, so attaching OpenAPI is free while a README would be billed",
        "Cowork cannot parse YAML; the OpenAPI attachment was only decorative for the Design canvas",
        "OpenAPI files disable MCP for the rest of the session, which is why the trainer preferred YAML",
    ],
    [
        "Adjuntar la especificación de valor (y quizá un logo), no todo el árbol de backend, para ahorrar tokens de contexto",
        "Los YAML no consumen tokens, así que OpenAPI es gratis y un README sí se factura",
        "Cowork no parsea YAML; el adjunto OpenAPI era solo decorativo para el lienzo Design",
        "Los ficheros OpenAPI desactivan MCP el resto de la sesión, por eso el formador prefirió YAML",
    ],
)
add(
    "q022",
    [
        "Clarify → plan → execute → verify → deliver",
        "Explore → estimate → staff → implement → archive",
        "Prompt → retrieve → generate → cite → fine-tune",
        "Install → authenticate → list tools → skip verify → ship",
    ],
    [
        "Aclarar → planear → ejecutar → verificar → entregar",
        "Explorar → estimar → dotar → implementar → archivar",
        "Prompt → recuperar → generar → citar → afinar",
        "Instalar → autenticar → listar tools → saltar verificar → entregar",
    ],
)
add(
    "q023",
    [
        "Additional clients on the same models, not a fourth core GUI tile you should confuse with Chat, Cowork, and Code",
        "Replacements that make Chat, Cowork, and Code obsolete once Slack or Excel is connected",
        "The only supported way to obtain a console API key for Messages.create",
        "Required MCP servers; without them messages.create returns an empty completion",
    ],
    [
        "Clientes extra sobre los mismos modelos, no un cuarto mosaico GUI que se confunda con Chat, Cowork y Code",
        "Sustitutos que dejan obsoletos Chat, Cowork y Code en cuanto conectáis Slack o Excel",
        "La única vía soportada para obtener una clave de consola para Messages.create",
        "Servidores MCP obligatorios; sin ellos messages.create devuelve una completion vacía",
    ],
)
add(
    "q024",
    [
        "Tools let the application supply live or private context (clock, DB, APIs) the weights do not contain, via a model-initiated handshake",
        "Tools delete the need for a system prompt because schemas replace standing instructions",
        "Tools exist only to generate images inside Cowork Design and do not apply to Messages.create",
        "Pasting extra text is always cheaper than any tool_result, so tools are only for exam vocabulary",
    ],
    [
        "Las tools dan contexto vivo o privado (reloj, BD, APIs) que los pesos no tienen, con un apretón iniciado por el modelo",
        "Las tools eliminan el system prompt porque los esquemas sustituyen las instrucciones fijas",
        "Las tools solo sirven para generar imágenes en Cowork Design y no aplican a Messages.create",
        "Pegar texto extra siempre es más barato que un tool_result, así que las tools son solo vocabulario de examen",
    ],
)
add(
    "q025",
    [
        "Append each user line and each assistant reply to a messages list you own, then pass that list on the next create",
        "Keep standing instructions in the system parameter on every request (or cache that prefix)",
        "Assume the HTTP server remembers the notebook kernel between process restarts without any storage you own",
        "Store conversation memory by fine-tuning a new Claude checkpoint after every user sentence",
    ],
    [
        "Añadir cada línea de usuario y cada respuesta del asistente a una lista messages vuestra y pasarla en el siguiente create",
        "Mantener las instrucciones fijas en system en cada petición (o cachear ese prefijo)",
        "Asumir que el servidor HTTP recuerda el kernel del notebook entre reinicios sin almacenamiento propio",
        "Guardar memoria afinando un checkpoint nuevo de Claude después de cada frase del usuario",
    ],
)
add(
    "q026",
    [
        "Pro, Max, Team, or Enterprise — UST is on Team/Enterprise; still download builds from the company portal when policy says so",
        "Any anonymous HTTP client with no Claude account, because Code authenticates only via local git",
        "Architect Professional certification must already be held before the Code installer will run",
        "Only a Percipio learner seat; Team/Enterprise plans are reserved for Architect tracks",
    ],
    [
        "Pro, Max, Team o Enterprise — UST va en Team/Enterprise; seguid bajando builds del portal de empresa si lo pide la política",
        "Cualquier cliente HTTP anónimo sin cuenta Claude, porque Code autentica solo con git local",
        "Hay que tener ya Architect Professional para que el instalador de Code arranque",
        "Solo un asiento Percipio; Team/Enterprise están reservados a las vías Architect",
    ],
)
add(
    "q027",
    [
        "In the org workspace / secret store — not git, not CLAUDE.md, not the Cowork thread",
        "In a committed .env on the default branch so teammates can npm install without a vault",
        "Inside CLAUDE.md so the model can rotate keys when it sees a 401",
        "Pasted into Cowork chat alongside the client corpus so the agent can export them later",
    ],
    [
        "En el workspace / almacén de secretos de la org — no git, no CLAUDE.md, no el hilo de Cowork",
        "En un .env confirmado en la rama por defecto para que el equipo haga npm install sin bóveda",
        "Dentro de CLAUDE.md para que el modelo rote claves cuando vea un 401",
        "Pegados en el chat de Cowork junto al corpus del cliente para que el agente los exporte luego",
    ],
)
add(
    "q028",
    [
        "Halt generation when a chosen delimiter appears so the client receives a bounded payload (for example closing a fence)",
        "Increase the context window to 1M for every model on the next request",
        "Bill thinking tokens at cache-hit prices regardless of whether thinking is enabled",
        "Authenticate MCP OAuth by placing the stop string in the Authorization header",
    ],
    [
        "Detener la generación al aparecer un delimitador elegido para que el cliente reciba un payload acotado (p. ej. cerrar una valla)",
        "Subir la ventana de contexto a 1M en todos los modelos en la siguiente petición",
        "Facturar tokens de pensamiento a precio de acierto de caché aunque el pensamiento esté apagado",
        "Autenticar OAuth de MCP poniendo la cadena de stop en la cabecera Authorization",
    ],
)
add(
    "q029",
    [
        "The model still only sees the messages (and tools/system) you send; the UI is your application",
        "The model now knows about your buttons and CSS because FastAPI injects the DOM into the context window",
        "You no longer need max_tokens; Streamlit caps output using the browser tab title",
        "Skilljar injects the UI into the context window automatically whenever the notebook kernel is running",
    ],
    [
        "El modelo solo ve los messages (y tools/system) que enviáis; la UI es vuestra aplicación",
        "El modelo ya conoce botones y CSS porque FastAPI inyecta el DOM en la ventana de contexto",
        "Ya no hace falta max_tokens; Streamlit recorta la salida con el título de la pestaña",
        "Skilljar inyecta la UI en la ventana de contexto siempre que el kernel del notebook esté en marcha",
    ],
)
add(
    "q030",
    [
        "Academy teaches vocabulary; the booked, proctored sitting is the credential — Percipio completion is not the Anthropic exam",
        "Completing Academy jargon courses is identical to being Anthropic certified on Pearson",
        "You cannot book Pearson until Percipio shows 100%, because Anthropic reads the LMS as the exam score",
        "CCDV-F is awarded automatically after four UST Zoom attendance ticks, with no Pearson sitting",
    ],
    [
        "Academy enseña vocabulario; la convocatoria proctorizada es la credencial — completar Percipio no es el examen de Anthropic",
        "Terminar los cursos de jerga de Academy es idéntico a estar certificado Anthropic en Pearson",
        "No podéis reservar Pearson hasta el 100% en Percipio, porque Anthropic lee el LMS como nota de examen",
        "CCDV-F se concede al marcar cuatro asistencias Zoom de UST, sin convocatoria Pearson",
    ],
)
add(
    "q031",
    [
        "Embedding neighbourhood (e.g. cosine similarity); the user’s wording need not appear verbatim",
        "Exact string equality with the user’s full sentence, like a SQL WHERE clause on the chunk text",
        "Sorting PDF filenames alphabetically and returning the first file as the only hit",
        "Always using BM25 only, never vectors, because Foundation forbids embedding models",
    ],
    [
        "Vecindario de embeddings (p. ej. similitud coseno); el enunciado del usuario no tiene que aparecer literal",
        "Igualdad exacta de cadena con la frase completa, como un WHERE SQL sobre el texto del chunk",
        "Ordenar nombres de PDF alfabéticamente y devolver el primer fichero como único acierto",
        "Usar siempre solo BM25, nunca vectores, porque Foundation prohíbe modelos de embeddings",
    ],
)
add(
    "q032",
    [
        "You re-pay input for the document and you re-pay thinking tokens; cache the stable prefix and keep thinking targeted",
        "Thinking cannot run unless Cowork is open, so the API combination is invalid rather than merely expensive",
        "Extended thinking refunds all input tokens automatically, so pairing it with a huge PDF is the cheap path",
        "PDFs disable thinking in the API contract, so the client should omit thinking whenever a document is attached",
    ],
    [
        "Volvéis a pagar el documento de entrada y los tokens de pensamiento; cachead el prefijo estable y usad thinking con tino",
        "El pensamiento no corre si Cowork no está abierto, así que la combinación de API es inválida más que cara",
        "El pensamiento extendido devuelve todos los tokens de entrada, así que juntarlo con un PDF enorme es lo barato",
        "Los PDF desactivan thinking en el contrato de API, así que el cliente debe omitirlo si hay documento",
    ],
)
add(
    "q033",
    [
        "In the client (history, project, product memory toggles) that resends needed context on the next turn",
        "In the stateless model server, which keeps a session id forever after the first Chat message",
        "Only in MongoDB Atlas, which Chat queries automatically for every logged-in workspace",
        "In the five-hour usage bar, which serialises yesterday’s thread until the meter resets",
    ],
    [
        "En el cliente (historial, proyecto, interruptores de memoria) que reenvía el contexto necesario en el siguiente turno",
        "En el servidor de modelo sin estado, que guarda un session id para siempre tras el primer mensaje de Chat",
        "Solo en MongoDB Atlas, que Chat consulta solo en cada workspace con sesión iniciada",
        "En la barra de uso de cinco horas, que serializa el hilo de ayer hasta que el contador se reinicia",
    ],
)
add(
    "q034",
    [
        "They are capability/cost/latency tiers in the Claude family; pick the smallest model that meets quality, and confirm live SKUs on the models page",
        "They are permission modes in Claude Code (ask / accept edits / bypass), not model SKUs you can pass to the API",
        "Opus is always free on Team plans; Haiku is always the most expensive SKU because it is the fastest",
        "Only Cowork can use Opus; the Messages API is restricted to Haiku regardless of the console picker",
    ],
    [
        "Son tramos de capacidad/coste/latencia de la familia Claude; elegid el modelo más pequeño que cumpla calidad y confirmen SKU vigentes",
        "Son modos de permiso de Claude Code (ask / accept edits / bypass), no SKU de modelo para la API",
        "Opus es siempre gratis en Team; Haiku es siempre el SKU más caro porque es el más rápido",
        "Solo Cowork puede usar Opus; la API Messages está limitada a Haiku da igual el selector de consola",
    ],
)
add(
    "q035",
    [
        "2017 transformer architecture; generative models that produce content, not only a true/false label",
        "A 1990s expert system of handwritten if-then rules with no learned attention",
        "Discriminative-only logistic regression that outputs a class label and never free text",
        "A SQL stored-procedure engine that plans queries instead of generating tokens",
    ],
    [
        "Arquitectura transformer de 2017; modelos generativos que producen contenido, no solo una etiqueta verdadero/falso",
        "Un sistema experto de los 90 con reglas if-then escritas a mano y sin atención aprendida",
        "Regresión logística solo discriminativa que saca una clase y nunca texto libre",
        "Un motor de procedimientos SQL que planifica consultas en vez de generar tokens",
    ],
)
add(
    "q036",
    [
        "How many tokens one turn’s payload may carry (system, tools, skills, history, new message)",
        "How many dollars your Team plan can spend per calendar year across Chat, Cowork, and API",
        "The five-hour Chat usage reset only; API calls do not share a token cap per request",
        "The number of MCP servers you may install from the marketplace on a Team seat",
    ],
    [
        "Cuántos tokens puede llevar la carga de un turno (system, tools, skills, historial, mensaje nuevo)",
        "Cuántos dólares puede gastar el plan Team al año entre Chat, Cowork y API",
        "Solo el reinicio de uso de Chat cada cinco horas; las llamadas API no tienen tope de tokens por petición",
        "Cuántos servidores MCP podéis instalar del marketplace con un asiento Team",
    ],
)
add(
    "q037",
    [
        "Context window answers “can this turn’s payload fit?”",
        "The product usage bar answers “have I exhausted my plan’s rolling allowance?” — a different meter",
        "/context refills the Team usage bar when the chip hits 100%, which is why the numbers should sum",
        "API rate limits and billing are the same counter as /context free space, so adding them is the right check",
    ],
    [
        "La ventana de contexto responde «¿cabe la carga de este turno?»",
        "La barra de uso del producto responde «¿he agotado la franquicia rodante del plan?» — es otro contador",
        "/context recarga la barra Team cuando el chip llega al 100%, por eso las cifras deberían sumar",
        "Los límites de API y la facturación son el mismo contador que el espacio libre de /context",
    ],
)
add(
    "q038",
    [
        "Low temperature when extracting structured facts; higher when drafting creative prose",
        "Always 2.0 for JSON schemas so the decoder explores more valid keys",
        "Temperature is ignored unless streaming is on, so batch jobs should leave it unset",
        "Haiku requires temperature 0; Opus requires 1; Sonnet ignores the field",
    ],
    [
        "Temperature baja al extraer hechos estructurados; más alta al redactar prosa creativa",
        "Siempre 2.0 para esquemas JSON para que el decodificador explore más claves válidas",
        "Temperature se ignora si no hay streaming, así que los lotes deben dejarla sin fijar",
        "Haiku exige temperature 0; Opus exige 1; Sonnet ignora el campo",
    ],
)
add(
    "q039",
    [
        "A thinking object on the request (type enabled plus a token budget; class minimum 1024) so Claude allocates internal reasoning before the visible answer",
        "Few-shotting a fake chain of thought in the user prompt only — there is no API parameter for thinking",
        "Turning Cowork to plan mode, which is what the API reads as extended thinking",
        "Setting stream=false, which silently enables a thinking budget equal to max_tokens",
    ],
    [
        "Un objeto thinking en la petición (type enabled más presupuesto de tokens; en clase mínimo 1024) para razonar antes de la respuesta visible",
        "Meter una cadena de pensamiento falsa en el prompt de usuario: no hay parámetro de API para thinking",
        "Pasar Cowork a plan mode, que es lo que la API interpreta como pensamiento extendido",
        "Poner stream=false, que activa en silencio un presupuesto de thinking igual a max_tokens",
    ],
)
add(
    "q040",
    [
        "Generated content billed like output — leaving thinking on for every trivial ask is expensive",
        "Always free and never counted in max_tokens, so you should enable thinking on every request",
        "Billed only as cache writes; follow-up questions with thinking on are therefore cache hits",
        "Refunded if the user does not expand the thinking block in the client UI",
    ],
    [
        "Contenido generado facturado como salida: dejar thinking en cada pregunta trivial sale caro",
        "Siempre gratis y nunca cuenta en max_tokens, así que conviene activarlo en todas las peticiones",
        "Solo se factura como escritura de caché; los seguimientos con thinking son por tanto aciertos de caché",
        "Se devuelve el importe si el usuario no despliega el bloque thinking en la UI",
    ],
)
add(
    "q041",
    [
        "Cover the thinking budget plus the user-visible answer",
        "Be smaller than the thinking budget so the model is forced to skip the visible answer",
        "Be ignored; only temperature interacts with extended thinking",
        "Equal the Team weekly usage cap so thinking cannot overrun billing",
    ],
    [
        "Cubrir el presupuesto de thinking más la respuesta visible para el usuario",
        "Ser menor que el presupuesto de thinking para obligar al modelo a saltarse la respuesta visible",
        "Ignorarse; solo temperature interactúa con el pensamiento extendido",
        "Igualar el tope semanal Team para que thinking no desborde la facturación",
    ],
)
add(
    "q042",
    [
        "Switching SKU / window (e.g. a 1M Sonnet option when offered) — it is not a permission mode and not /compact",
        "Approving bash without hooks; /model is the permission picker under another name",
        "Installing MCP servers from the marketplace; /model is how Code binds Figma",
        "Resetting the five-hour usage bar to zero without starting a new session",
    ],
    [
        "Cambiar SKU / ventana (p. ej. Sonnet 1M si se ofrece): no es un modo de permiso ni /compact",
        "Aprobar bash sin hooks; /model es el selector de permisos con otro nombre",
        "Instalar servidores MCP del marketplace; /model es cómo Code enlaza Figma",
        "Poner a cero la barra de cinco horas sin abrir una sesión nueva",
    ],
)
add(
    "q043",
    [
        "Bring it in via tools, MCP, RAG, or (expensively) custom training — not hope the model memorised UST’s directory",
        "Assume the weights already contain last week’s unpublished wiki because the mix includes “the web”",
        "Only raise temperature so the model samples internal facts that were not in the pretraining mix",
        "Disable the system prompt so unpublished pages are not filtered out of the residual stream",
    ],
    [
        "Meterlo con tools, MCP, RAG o (caro) entrenamiento a medida — no esperar que el modelo memorice el directorio de UST",
        "Asumir que los pesos ya contienen el wiki inédito de la semana pasada porque la mezcla incluye «la web»",
        "Solo subir temperature para muestrear hechos internos que no estaban en el preentrenamiento",
        "Quitar el system prompt para que las páginas inéditas no se filtren del residual stream",
    ],
)
add(
    "q044",
    [
        "Prefer a small, cheap, low-latency model (Haiku-class) for (A) if evals pass",
        "Prefer a more capable model (Opus-class or current flagship) for (B) where mistakes are expensive",
        "Always use the largest model for (A) because batch jobs should maximise spend to improve embeddings",
        "Model choice cannot be made in the API; only Chat’s picker can select Haiku versus Opus",
    ],
    [
        "Preferir un modelo pequeño, barato y de baja latencia (clase Haiku) para (A) si las evals pasan",
        "Preferir un modelo más capaz (clase Opus o flagship vigente) para (B), donde el error sale caro",
        "Usar siempre el modelo más grande para (A) porque los lotes deben maximizar gasto para mejorar embeddings",
        "La elección de modelo no se puede hacer en la API; solo el selector de Chat elige Haiku u Opus",
    ],
)
add(
    "q045",
    [
        "Summarises history so later turns fit the context window; it does not refill the Team usage bar",
        "Pays your API invoice by collapsing billed tokens into a single cache write",
        "Is the same as prompt caching TTL on the Messages API, including the five-minute hit window",
        "Disables all tools for the rest of the session so the summary stays inside the window",
    ],
    [
        "Resume el historial para que los turnos siguientes quepan en la ventana; no recarga la barra de uso Team",
        "Paga la factura de API compactando tokens facturados en una sola escritura de caché",
        "Es lo mismo que el TTL de prompt caching en Messages, incluida la ventana de acierto de cinco minutos",
        "Desactiva todas las tools el resto de la sesión para que el resumen quepa en la ventana",
    ],
)
add(
    "q046",
    [
        "Every user/assistant pair and pinned skill is resent; they occupy the window every turn unless you compact or drop them",
        "They are billed only after output starts, so /context free space is unrelated to pinned skills",
        "Skills run only on the local GPU and never enter the payload, so the shrink is a display bug",
        "Free space is a UI estimate you can ignore; the server always accepts the full thread plus skills",
    ],
    [
        "Cada par user/assistant y cada skill anclada se reenvían; ocupan la ventana cada turno salvo que compactéis o las quitéis",
        "Solo se facturan cuando empieza la salida, así que el espacio libre de /context no tiene que ver con skills ancladas",
        "Las skills corren solo en la GPU local y nunca entran en la carga, así que el encogimiento es un bug de UI",
        "El espacio libre es una estimación de UI que se puede ignorar; el servidor acepta siempre el hilo completo",
    ],
)
add(
    "q047",
    [
        "Cache write is typically dearer than a later cache hit; output and thinking still bill if they occur",
        "Cache hits are more expensive than first writes by design, so you should bust the cache every turn",
        "Cache deletes max_tokens on the next request so you must raise it after the first write",
        "Cache is billed as Cowork folder storage on disk, not as API token traffic",
    ],
    [
        "La escritura de caché suele ser más cara que un acierto posterior; la salida y el thinking se facturan si ocurren",
        "Los aciertos de caché son más caros que la primera escritura a propósito, así que hay que invalidar cada turno",
        "La caché borra max_tokens en la siguiente petición, así que hay que subirlo tras la primera escritura",
        "La caché se factura como almacenamiento de carpeta Cowork en disco, no como tráfico de tokens de API",
    ],
)
add(
    "q048",
    [
        "thinking may show a plain-language plan; redacted_thinking is an opaque safety payload you cannot decode; text is the user-visible answer",
        "thinking is the user-visible final essay; redacted_thinking is the JSON schema for structured output",
        "They are identical fields and always both empty unless stream=true",
        "redacted_thinking means the API key was revoked mid-request and the call should be retried",
    ],
    [
        "thinking puede mostrar un plan en lenguaje claro; redacted_thinking es un payload opaco de seguridad; text es la respuesta visible",
        "thinking es el ensayo final visible; redacted_thinking es el esquema JSON de la salida estructurada",
        "Son campos idénticos y siempre vacíos salvo que stream=true",
        "redacted_thinking significa que la clave de API se revocó a mitad de petición y hay que reintentar",
    ],
)
add(
    "q049",
    [
        "Steer with prompting, smaller attachments, and by not stuffing CLAUDE.md with encyclopedias; /context is observability",
        "Add the Chat usage chip to /context free space until the sum equals 2k tokens",
        "Disable the transformer architecture in /config so each turn is capped at 2k regardless of SKU",
        "Set temperature to −1, which the API treats as a hard 2k output cap",
    ],
    [
        "Orientar con prompting, adjuntos más pequeños y sin llenar CLAUDE.md de enciclopedias; /context es observabilidad",
        "Sumar el chip de uso de Chat al espacio libre de /context hasta que den 2k tokens",
        "Desactivar la arquitectura transformer en /config para topar cada turno en 2k da igual el SKU",
        "Poner temperature en −1, que la API interpreta como tope duro de 2k de salida",
    ],
)
add(
    "q050",
    [
        "The same Claude model family; the clients differ in workspace, tools, and how history is held",
        "Three unrelated model vendors with no shared family and separate training mixes",
        "Only local Llama weights with no network calls to Anthropic",
        "Message Batches exclusively; interactive Chat is a different non-Claude product",
    ],
    [
        "La misma familia de modelos Claude; los clientes cambian en espacio de trabajo, tools y cómo se guarda el historial",
        "Tres proveedores de modelos sin familia compartida ni mezcla de entrenamiento común",
        "Solo pesos Llama locales, sin llamadas de red a Anthropic",
        "Exclusivamente Message Batches; el Chat interactivo es otro producto que no es Claude",
    ],
)
add(
    "q051",
    [
        "A model plus tools plus a loop that can plan, call tools, observe results, and continue until a stop condition",
        "Any Messages.create call with temperature 0, which Foundation defines as an agent",
        "A vector embedding compared with cosine similarity, with no tool loop required",
        "The Skilljar course player, because it sequences videos without a human in the loop",
    ],
    [
        "Un modelo más tools más un bucle que planea, llama tools, observa resultados y sigue hasta una condición de parada",
        "Cualquier Messages.create con temperature 0, que Foundation define como agente",
        "Un embedding vectorial comparado con similitud coseno, sin bucle de tools",
        "El reproductor de cursos Skilljar, porque secuenciavídeos sin humano en el bucle",
    ],
)
add(
    "q052",
    [
        "Assistants complete a line; Code can plan a repo, run tests, open PRs, and talk to Jira/Figma via tools",
        "There is no difference: both are line-completion models with the same permission modes",
        "Line completion requires Architect Professional; Claude Code is the Foundation-only editor",
        "Claude Code cannot edit files; it only comments in the chat panel like an IDE assistant",
    ],
    [
        "Los asistentes completan una línea; Code puede planear un repo, lanzar tests, abrir PR y hablar con Jira/Figma vía tools",
        "No hay diferencia: ambos son modelos de completar línea con los mismos modos de permiso",
        "Completar línea exige Architect Professional; Claude Code es el editor solo de Foundation",
        "Claude Code no puede editar ficheros; solo comenta en el panel de chat como un asistente de IDE",
    ],
)
add(
    "q053",
    [
        "Plan mode produces a reviewable to-do list you can edit before execution; direct execution skips that board and goes",
        "Plan mode is a different LLM vendor selected in /model, not a Claude Code workflow",
        "Direct execution is the only mode that can call MCP; plan mode is read-only documentation",
        "Plan mode refills usage limits by summarising the board into a cache write",
    ],
    [
        "Plan mode produce una lista de tareas revisable que podéis editar antes de ejecutar; la ejecución directa se salta ese tablero",
        "Plan mode es otro proveedor de LLM elegido en /model, no un flujo de Claude Code",
        "La ejecución directa es el único modo que puede llamar MCP; plan mode es documentación de solo lectura",
        "Plan mode recarga los límites de uso resumiendo el tablero en una escritura de caché",
    ],
)
add(
    "q054",
    [
        "A way to expose tools (schemas or MCP) so the model can request actions",
        "An application loop that executes tool_use, returns tool_result, and calls the model again until it stops",
        "Fine-tuning a new Claude checkpoint on every tool_result so the next loop has weights that include the observation",
        "Deleting the system prompt so the agent has no policy and can choose tools more freely",
    ],
    [
        "Una forma de exponer tools (esquemas o MCP) para que el modelo pida acciones",
        "Un bucle de aplicación que ejecuta tool_use, devuelve tool_result y vuelve a llamar al modelo hasta que para",
        "Afinar un checkpoint nuevo de Claude en cada tool_result para que el siguiente bucle tenga los pesos de la observación",
        "Borrar el system prompt para que el agente no tenga política y elija tools con más libertad",
    ],
)
add(
    "q055",
    [
        "Orchestration helpers (memory, tool loops) above raw messages.create — not a reason to skip learning Messages",
        "Replacing the Messages API with CSV files that the Agent SDK polls instead of HTTP",
        "The Pearson proctoring client, rebranded for labs so you can skip the Messages notebook",
        "A Cowork-only desktop theme; Agent SDK does not run against the API",
    ],
    [
        "Ayudas de orquestación (memoria, bucles de tools) encima de messages.create — no una razón para saltarse Messages",
        "Sustituir la API Messages por CSV que el Agent SDK consulta en vez de HTTP",
        "El cliente de proctoring de Pearson, reetiquetado para laboratorios y así saltarse el notebook de Messages",
        "Un tema de escritorio solo de Cowork; el Agent SDK no habla con la API",
    ],
)
add(
    "q056",
    [
        "On the agent markdown / agent config, not solely in the global permission picker",
        "Only by changing Haiku to Opus, because permission modes are model SKUs",
        "In Percipio, which pushes permission YAML into every UST Claude Code install",
        "By setting temperature to 0, which Foundation treats as bypass for grep",
    ],
    [
        "En el markdown / config del agente, no solo en el selector global de permisos",
        "Solo cambiando Haiku por Opus, porque los modos de permiso son SKU de modelo",
        "En Percipio, que empuja YAML de permisos a cada instalación UST de Claude Code",
        "Poniendo temperature 0, que Foundation trata como bypass para grep",
    ],
)
add(
    "q057",
    [
        "Pausing when the goal needs a human choice (format, multi-select vs single); a callback collects the answer and the loop continues",
        "Bypassing Anthropic’s usage policy by routing the question to a local unfiltered model",
        "Replacing all tools with a single bash so the human never has to choose among schemas",
        "Compacting the context window by asking the user to summarise the thread",
    ],
    [
        "Pausar cuando el objetivo necesita una elección humana (formato, multi vs simple); un callback recoge la respuesta y el bucle sigue",
        "Saltar la política de uso de Anthropic desviando la pregunta a un modelo local sin filtro",
        "Sustituir todas las tools por un solo bash para que el humano no elija entre esquemas",
        "Compactar la ventana de contexto pidiendo al usuario que resuma el hilo",
    ],
)
add(
    "q058",
    [
        "Common host capabilities are available without rewriting a clock function; you still add custom/MCP tools for your systems",
        "You never need custom tools or MCP for proprietary data once built-ins are enabled",
        "The model server becomes stateful for the rest of the calendar day after the first built-in call",
        "Eval graders are disabled whenever a built-in tool is bound, so labs should avoid them",
    ],
    [
        "Hay capacidades comunes del host sin reescribir un reloj; igual añadís tools custom/MCP para vuestros sistemas",
        "Nunca hacen falta tools custom ni MCP para datos propios una vez activados los built-in",
        "El servidor de modelo pasa a tener estado el resto del día natural tras la primera llamada built-in",
        "Los evaluadores se desactivan si hay una tool built-in enlazada, así que los labs deben evitarlas",
    ],
)
add(
    "q059",
    [
        "A permission / policy hook: the host decides whether a proposed tool call may run before execution",
        "A prompt-cache TTL that expires tool schemas after five minutes",
        "An embedding model that scores tool names against the user sentence",
        "The Pearson lock-down browser used during the Foundation sitting",
    ],
    [
        "Un gancho de permiso / política: el host decide si la llamada a tool propuesta puede ejecutarse",
        "Un TTL de prompt cache que caduca los esquemas de tools a los cinco minutos",
        "Un modelo de embeddings que puntúa nombres de tools contra la frase del usuario",
        "El navegador de bloqueo de Pearson usado en la convocatoria Foundation",
    ],
)
add(
    "q060",
    [
        "Agentic client features: the workspace agent can continue multi-step local work without you sitting in Chat",
        "Proof that Cowork is the Messages API with a different base URL",
        "The only supported way to use Haiku; Sonnet and Opus cannot run scheduled Cowork jobs",
        "Replacements for git hooks, so you should disable pre-commit when Cowork is installed",
    ],
    [
        "Funciones de cliente agente: el agente del espacio puede seguir trabajo local de varios pasos sin estar en Chat",
        "Prueba de que Cowork es la API Messages con otra URL base",
        "La única forma soportada de usar Haiku; Sonnet y Opus no pueden correr trabajos programados de Cowork",
        "Sustitutos de los hooks de git, así que hay que desactivar pre-commit si Cowork está instalado",
    ],
)
add(
    "q061",
    [
        "While still in plan mode, before you accept execution",
        "After execution has started, by editing the frozen to-do invisibly so Playwright keeps running",
        "Never; plans cannot include test runners, so the swap is impossible until after delivery",
        "Only by switching to Chat and pasting the plan as a new user message",
    ],
    [
        "Todavía en plan mode, antes de aceptar la ejecución",
        "Cuando la ejecución ya ha empezado, editando en invisible el to-do congelado para que Playwright siga",
        "Nunca; los planes no pueden incluir runners de test, así que el cambio es imposible hasta entregar",
        "Solo pasando a Chat y pegando el plan como un mensaje de usuario nuevo",
    ],
)
add(
    "q062",
    [
        "Modes are a policy for how often the tool loop pauses for consent; they are not a different model",
        "Auto / bypass-style still leaves enterprise responsibility with you; hooks become mandatory rather than nice-to-have",
        "Opus in auto mode is a safer model family than Haiku in ask mode because SKU implies permission",
        "Accept-edits mode is a substitute for CLAUDE.md, so you can delete project instructions",
    ],
    [
        "Los modos son una política de cuántas veces el bucle de tools para a pedir consentimiento; no son otro modelo",
        "Auto / bypass sigue dejando la responsabilidad de empresa en vosotros; los hooks pasan a ser obligatorios",
        "Opus en auto es una familia más segura que Haiku en ask porque el SKU implica el permiso",
        "Accept-edits sustituye a CLAUDE.md, así que podéis borrar las instrucciones de proyecto",
    ],
)
add(
    "q063",
    [
        "Whatever your app persisted and put back into the context window (or a dedicated memory store) — not magically inside the stateless model",
        "Automatically equal to the prompt-cache TTL, so memory expires when the cache write expires",
        "The same as cosine similarity in Atlas; retrieve the last user sentence as a vector and you have memory",
        "Disabled whenever tools are bound, because tool_result replaces the need to store history",
    ],
    [
        "Lo que vuestra app persistió y volvió a meter en la ventana (o en un almacén de memoria) — no magia dentro del modelo sin estado",
        "Automáticamente igual al TTL de prompt cache, así que la memoria caduca con la escritura de caché",
        "Lo mismo que la similitud coseno en Atlas: recuperar la última frase como vector ya es memoria",
        "Desactivada si hay tools enlazadas, porque tool_result sustituye guardar historial",
    ],
)
add(
    "q064",
    [
        "Map tool name → function, run it, append a user tool_result bound to the tool id, then call Messages again",
        "Show the incomplete essay to the user as the final answer and exit the loop",
        "Fine-tune Opus on the tool schema before the next HTTP request",
        "Switch the base URL to Cowork automatically so the desktop agent finishes the tool call",
    ],
    [
        "Mapear nombre de tool → función, ejecutarla, añadir un tool_result de usuario ligado al id, y volver a llamar a Messages",
        "Mostrar el ensayo incompleto al usuario como respuesta final y salir del bucle",
        "Afinar Opus con el esquema de la tool antes de la siguiente petición HTTP",
        "Cambiar la URL base a Cowork para que el agente de escritorio termine la llamada",
    ],
)
add(
    "q065",
    [
        "An agent planning over third-party tools: you consent, the model chooses get-design-context-style tools, results land for generation",
        "Fine-tuning Claude on Figma pixels so later Messages calls no longer need the MCP server",
        "Replacing CLAUDE.md with OAuth; once Figma is connected, project instructions are ignored",
        "A required step for every Hello World Messages.create, even without a design file",
    ],
    [
        "Un agente que planea sobre tools de terceros: consentís, el modelo elige tools tipo get-design-context y los resultados alimentan la generación",
        "Afinar Claude con píxeles de Figma para que las siguientes llamadas Messages ya no necesiten el servidor MCP",
        "Sustituir CLAUDE.md por OAuth; al conectar Figma se ignoran las instrucciones de proyecto",
        "Un paso obligatorio en cada Hello World de Messages.create, aunque no haya fichero de diseño",
    ],
)
add(
    "q066",
    [
        "Lead with the task and action verbs: “Write three paragraphs about how solar panels work.”",
        "Keep a rambling story about solar panels sounding neat and hope Claude infers the deliverable",
        "Repeat the same vague paragraph twelve times so the context window teaches the task by occupancy",
        "Remove all verbs so the model invents the assignment from nouns alone",
    ],
    [
        "Empezar por la tarea y verbos de acción: «Escribíd tres párrafos sobre cómo funcionan los paneles solares.»",
        "Dejar una historia vaga sobre lo bonitos que suenan los paneles y esperar que Claude infiera el entregable",
        "Repetir el mismo párrafo vago doce veces para que la ventana de contexto enseñe la tarea por ocupación",
        "Quitar todos los verbos para que el modelo invente el encargo solo con nombres",
    ],
)
add(
    "q067",
    [
        "Label documents, rules, and untrusted user input so instructions and data stay distinct",
        "Compile the prompt into Java bytecode that the Messages API executes server-side",
        "Increase temperature automatically whenever a closing tag is present",
        "Create MCP servers; each XML tag is compiled into a tool schema",
    ],
    [
        "Etiquetar documentos, reglas y entrada no fiable para que instrucciones y datos no se mezclen",
        "Compilar el prompt a bytecode Java que la API Messages ejecuta en el servidor",
        "Subir temperature automáticamente cuando hay una etiqueta de cierre",
        "Crear servidores MCP; cada etiqueta XML se compila a un esquema de tool",
    ],
)
add(
    "q068",
    [
        "When the output format is brittle and examples teach the shape better than adjectives",
        "Always, even for “what is 2+2”, because more tokens in the prompt always improve accuracy",
        "Never, because Claude cannot read examples in the user or assistant roles",
        "Only inside thinking budgets; few-shot outside a thinking block is ignored",
    ],
    [
        "Cuando el formato de salida es frágil y los ejemplos enseñan la forma mejor que los adjetivos",
        "Siempre, incluso en «qué es 2+2», porque más tokens en el prompt siempre mejoran la precisión",
        "Nunca, porque Claude no puede leer ejemplos en los roles user o assistant",
        "Solo dentro de presupuestos de thinking; el few-shot fuera de un bloque thinking se ignora",
    ],
)
add(
    "q069",
    [
        "Constraints are the spec — under 1000 words, a revealing action, a supporting character make an exam-ready version",
        "Claude refuses all stories, so the prompt is weak because narrative is out of policy",
        "Stories require Cowork; Messages.create cannot generate fiction without a folder attachment",
        "max_tokens cannot apply to prose, so length constraints in the prompt have no effect",
    ],
    [
        "Las restricciones son la especificación: menos de 1000 palabras, una acción reveladora, un personaje de apoyo",
        "Claude rechaza todas las historias, así que el prompt es débil porque la narrativa está fuera de política",
        "Las historias exigen Cowork; Messages.create no genera ficción sin una carpeta adjunta",
        "max_tokens no aplica a la prosa, así que limitar longitud en el prompt no tiene efecto",
    ],
)
add(
    "q070",
    [
        "XML tags around untrusted input and source documents",
        "Prefill plus stop sequences when the consumer needs a tight JSON or fenced envelope",
        "Putting standing role instructions only in a random user message and never in system",
        "Raising temperature to maximise JSON schema obedience",
    ],
    [
        "Etiquetas XML alrededor de entrada no fiable y documentos fuente",
        "Prefill más stop sequences cuando el consumidor necesita un JSON o una valla cerrados",
        "Poner las instrucciones de rol solo en un mensaje de usuario al azar y nunca en system",
        "Subir temperature para maximizar la obediencia al esquema JSON",
    ],
)
add(
    "q071",
    [
        "Specific, measurable instructions beat rambling curiosity",
        "The exam forbids the word geothermal, so the rewrite is mainly about banned vocabulary",
        "Stats require vision even when they are text, so the specific prompt still needs image blocks",
        "Three is the only legal number of countries Claude may list under Foundation policy",
    ],
    [
        "Las instrucciones específicas y medibles ganan a la curiosidad vaga",
        "El examen prohíbe la palabra geotérmica, así que la reescritura va sobre vocabulario vetado",
        "Las estadísticas exigen visión aunque sean texto, así que el prompt específico aún necesita bloques de imagen",
        "Tres es el único número legal de países que Claude puede listar según Foundation",
    ],
)
add(
    "q072",
    [
        "The system parameter (or CLAUDE.md analogue in Code), not mixed into every noisy user paste",
        "The tool_result of get_current_date_time, which Foundation uses as the standing policy channel",
        "The Pearson NDA, which the model reads automatically when the API key is from a Team org",
        "A BM25 index of role adjectives retrieved on every user turn instead of a system prompt",
    ],
    [
        "El parámetro system (o el análogo CLAUDE.md en Code), no mezclado en cada pegado ruidoso de usuario",
        "El tool_result de get_current_date_time, que Foundation usa como canal de política permanente",
        "El NDA de Pearson, que el modelo lee solo si la clave de API es de una org Team",
        "Un índice BM25 de adjetivos de rol recuperado en cada turno en vez de un system prompt",
    ],
)
add(
    "q073",
    [
        "You place an assistant message (for example a markdown fence) so generation continues from that seed",
        "You delete the user role so the next token is forced to be a system instruction",
        "You must use Cowork Design; prefill is not a Messages API pattern",
        "You disable stop sequences forever so the prefill can run past any delimiter",
    ],
    [
        "Colocáis un mensaje assistant (por ejemplo una valla markdown) para que la generación siga desde esa semilla",
        "Elimináis el rol user para que el siguiente token sea una instrucción de sistema",
        "Hay que usar Cowork Design; el prefill no es un patrón de la API Messages",
        "Desactiváis para siempre las stop sequences para que el prefill pase cualquier delimitador",
    ],
)
add(
    "q074",
    [
        "Build an eval set, run it, grade (not only boolean), and revise — scores can go down",
        "Ship it to production with no samples because Foundation treats prompt draft as the credential",
        "Fine-tune a new judge model from scratch before any eval run is allowed",
        "Ask Percipio to grade it; the LMS score is what Pearson will mirror",
    ],
    [
        "Montar un set de eval, ejecutarlo, puntuar (no solo booleanos) y revisar — la nota puede bajar",
        "Mandarlo a producción sin muestras porque Foundation trata el borrador de prompt como credencial",
        "Afinar un modelo juez nuevo desde cero antes de permitir cualquier eval",
        "Pedir a Percipio que lo puntúe; la nota del LMS es lo que Pearson copiará",
    ],
)
add(
    "q075",
    [
        "Both the general technique and the Claude control (stop sequences, structured output, extended thinking parameter)",
        "Only the generic pattern, never Claude-specific controls, because the exam is vendor-neutral",
        "Only Percipio multiple choice about GPT, because CCDV-F is scored against OpenAI names",
        "Only Cowork folder names; prompting techniques are Architect Professional only",
    ],
    [
        "Tanto la técnica general como el control de Claude (stop sequences, salida estructurada, parámetro de thinking)",
        "Solo el patrón genérico, nunca controles de Claude, porque el examen es agnóstico de proveedor",
        "Solo test Percipio sobre GPT, porque CCDV-F se puntúa con nombres de OpenAI",
        "Solo nombres de carpetas Cowork; las técnicas de prompting son de Architect Professional",
    ],
)
add(
    "q076",
    [
        "Redundant cost: you already allocated a thinking block — keep the user prompt as the task spec",
        "Required or thinking will not run; the API ignores the thinking object without a CoT few-shot",
        "The only way to get redacted_thinking in the response payload",
        "How prompt cache TTLs are set; the CoT few-shot is parsed as cache_control",
    ],
    [
        "Coste redundante: ya asignasteis un bloque thinking — dejad el prompt de usuario como especificación de la tarea",
        "Obligatorio o thinking no corre; la API ignora el objeto thinking sin un few-shot de CoT",
        "La única forma de obtener redacted_thinking en el payload de respuesta",
        "Así se fija el TTL de prompt cache; el few-shot de CoT se parsea como cache_control",
    ],
)
add(
    "q077",
    [
        "A host-language function and a schema (name, description, input schema) passed in the tools array",
        "Only a CLAUDE.md paragraph with no schema, because Code infers JSON from prose",
        "A Pearson voucher and a Percipio badge, which bind tools to the API key",
        "A vector index and a BM25 index, nothing else — tools are a retrieval feature",
    ],
    [
        "Una función en el lenguaje del host y un esquema (nombre, descripción, input) en el array tools",
        "Solo un párrafo en CLAUDE.md sin esquema, porque Code infiere JSON a partir de la prosa",
        "Un vale Pearson y una insignia Percipio, que enlazan tools a la clave de API",
        "Un índice vectorial y uno BM25, nada más: las tools son una función de recuperación",
    ],
)
add(
    "q078",
    [
        "The model chooses among tools using names and descriptions; a vague blurb causes wrong or extra calls",
        "JSON Schema forbids the word data, so the tool cannot be bound until the description is renamed",
        "Tools cannot run if the description is under 500 words; vague short blurbs are rejected by the API",
        "Cowork deletes tools whose descriptions are shorter than the matching CLAUDE.md section",
    ],
    [
        "El modelo elige tools por nombre y descripción; un texto vago provoca llamadas extra o equivocadas",
        "JSON Schema prohíbe la palabra data, así que la tool no se enlaza hasta renombrar la descripción",
        "Las tools no corren si la descripción tiene menos de 500 palabras; los textos cortos los rechaza la API",
        "Cowork borra tools cuya descripción es más corta que la sección equivalente de CLAUDE.md",
    ],
)
add(
    "q079",
    [
        "Claude stops with tool_use and emits a tool_use block (id, name, model-chosen input); it has not finished the user-facing sentence",
        "Your code runs the function and returns a tool_result as user content bound to the same tool id",
        "Tool results must be sent with role assistant so the model thinks it already executed bash",
        "The model executes Python inside Anthropic’s GPU on your laptop filesystem during the first response",
    ],
    [
        "Claude para con tool_use y emite un bloque (id, nombre, input elegido); aún no ha cerrado la frase para el usuario",
        "Vuestro código ejecuta la función y devuelve un tool_result como contenido user ligado al mismo id",
        "Los tool_result deben ir con rol assistant para que el modelo crea que ya ejecutó bash",
        "El modelo ejecuta Python en la GPU de Anthropic sobre el sistema de ficheros del portátil en la primera respuesta",
    ],
)
add(
    "q080",
    [
        "The model, using names, descriptions, and the user text",
        "You must hard-code a router in that first HTTP request that names exactly one tool",
        "Pearson VUE, which injects the chosen tool name into the Messages response",
        "MongoDB Atlas, which always selects the tool whose name sorts first in the collection",
    ],
    [
        "El modelo, usando nombres, descripciones y el texto del usuario",
        "Tenéis que cablear un router en esa primera petición HTTP que nombre exactamente una tool",
        "Pearson VUE, que inyecta el nombre de tool elegido en la respuesta Messages",
        "MongoDB Atlas, que siempre elige la tool cuyo nombre va primero en la colección",
    ],
)
add(
    "q081",
    [
        "N sources × M AI apps becoming N×M point-to-point SDKs; instead, servers expose tools once and clients consume the protocol",
        "Replacing HTTPS with FTP so tool payloads can stream as files",
        "Making the Messages API stateful by storing tool schemas on Anthropic’s servers for 90 days",
        "Training Haiku on Figma only; MCP is a fine-tune format, not an integration protocol",
    ],
    [
        "N fuentes × M apps de IA acabando en SDKs punto a punto N×M; en su lugar, los servidores exponen tools una vez y los clientes consumen el protocolo",
        "Sustituir HTTPS por FTP para que los payloads de tools circulen como ficheros",
        "Hacer con estado la API Messages guardando esquemas de tools 90 días en servidores de Anthropic",
        "Entrenar Haiku solo con Figma; MCP es un formato de fine-tune, no un protocolo de integración",
    ],
)
add(
    "q082",
    [
        "Server connects to the data source and exposes tools; client lives in the AI app, lists tools, and lets Claude choose",
        "Client stores the database; server is only Pearson’s exam harness",
        "They are the same process as prompt cache; MCP is an alias for cache_control",
        "Server is always Claude Chat; client is always Cowork, regardless of where you installed the connector",
    ],
    [
        "El servidor se conecta a la fuente de datos y expone tools; el cliente vive en la app de IA, lista tools y deja elegir a Claude",
        "El cliente guarda la base de datos; el servidor es solo el arnés de examen de Pearson",
        "Son el mismo proceso que la prompt cache; MCP es un alias de cache_control",
        "El servidor es siempre Claude Chat; el cliente es siempre Cowork, da igual dónde instalasteis el conector",
    ],
)
add(
    "q083",
    [
        "Ad-hoc tools live inside one app; MCP moves the same idea to a server other clients (Code, Cowork, even other IDEs) can share",
        "MCP cannot expose tools, only CSS themes for the Code side panel",
        "Ad-hoc tools are illegal on the Messages API; you may only bind MCP servers",
        "MCP requires Architect Professional; Foundation labs may only use notebook functions",
    ],
    [
        "Las tools ad hoc viven en una app; MCP lleva la misma idea a un servidor que otros clientes (Code, Cowork, otros IDE) pueden compartir",
        "MCP no puede exponer tools, solo temas CSS para el panel de Code",
        "Las tools ad hoc son ilegales en la API Messages; solo se pueden enlazar servidores MCP",
        "MCP exige Architect Professional; los labs Foundation solo pueden usar funciones de notebook",
    ],
)
add(
    "q084",
    [
        "Not appear among callable tools until you connect, authenticate, and confirm status",
        "Still appear in every plan with full OAuth, because listing does not require a live connection",
        "Automatically fine-tune Opus on the last Figma file in the recents list",
        "Resize the context window to 1M for the rest of the session as a side effect of the disconnect",
    ],
    [
        "No aparecer entre las tools invocables hasta que conectéis, autenticéis y confirméis el estado",
        "Seguir apareciendo en cada plan con OAuth completo, porque listar no exige conexión viva",
        "Afinar Opus automáticamente con el último fichero Figma de recientes",
        "Redimensionar la ventana de contexto a 1M el resto de la sesión como efecto de la desconexión",
    ],
)
add(
    "q085",
    [
        "A local proprietary server (e.g. stdio on the same host as the client)",
        "A vendor-provided server (Figma, Playwright, …) or your server wrapping third-party HTTP",
        "A Pearson exam server that grades CCDV-F automatically when MCP is enabled",
        "A prompt-cache replica that stores vectors forever instead of exposing tools",
    ],
    [
        "Un servidor propietario local (p. ej. stdio en el mismo host que el cliente)",
        "Un servidor de proveedor (Figma, Playwright, …) o el vuestro envolviendo HTTP de terceros",
        "Un servidor de examen Pearson que puntúa CCDV-F solo al activar MCP",
        "Una réplica de prompt cache que guarda vectores para siempre en vez de exponer tools",
    ],
)
add(
    "q086",
    [
        "Receive the smallest tool set that can read the DB and send mail; keep debug/search tools off the plaintext path",
        "Get unconstrained Bash plus a public “help” MCP that sees plaintext addresses for easier debugging",
        "Disable all tools and paste the CRM into Chat so PII never touches a schema",
        "Put SMTP passwords in CLAUDE.md so the agent can rotate them without a secret store",
    ],
    [
        "Recibir el conjunto mínimo de tools que lea la BD y envíe correo; dejar tools de debug/búsqueda fuera de la ruta en claro",
        "Tener Bash sin restricciones más un MCP público de «ayuda» que vea direcciones en claro para depurar",
        "Desactivar todas las tools y pegar el CRM en Chat para que el PII no toque un esquema",
        "Poner contraseñas SMTP en CLAUDE.md para que el agente las rote sin almacén de secretos",
    ],
)
add(
    "q087",
    [
        "Bound per request — you may attach one tool this turn and five the next",
        "Permanent server state for 90 days after first use, so later calls inherit the first tools array",
        "Ignored unless Cowork is running on the same machine as the notebook kernel",
        "Stored inside the embedding model so RAG can retrieve tool schemas by cosine similarity",
    ],
    [
        "Se enlazan por petición: podéis adjuntar una tool este turno y cinco el siguiente",
        "Estado permanente del servidor 90 días tras el primer uso, así que las llamadas posteriores heredan el primer array",
        "Se ignoran salvo que Cowork esté en la misma máquina que el kernel del notebook",
        "Se guardan en el modelo de embeddings para que RAG recupere esquemas por similitud coseno",
    ],
)
add(
    "q088",
    [
        "Anyone with the repo can spend your quota and reach customer data; use workspaces and secret stores",
        "Git cannot store text files named .env, so the commit would have failed anyway",
        "Claude automatically rotates keys committed to main within five minutes, so the risk is theoretical",
        "Skilljar scans and encrypts all GitHub remotes for UST, so committed keys are already vaulted",
    ],
    [
        "Quien tenga el repo puede gastar la cuota y llegar a datos de cliente; usad workspaces y almacenes de secretos",
        "Git no puede guardar ficheros de texto llamados .env, así que el commit habría fallado igual",
        "Claude rota solo las claves confirmadas en main en cinco minutos, así que el riesgo es teórico",
        "Skilljar escanea y cifra todos los remotos GitHub de UST, así que las claves ya están en una bóveda",
    ],
)
add(
    "q089",
    [
        "It runs locally in the Claude Code lifecycle and can block dangerous tool arguments before they execute",
        "It fine-tunes Opus to refuse bash by adding the hook text to the pretraining mix",
        "It increases the context window so rm -rf fits beside the rest of the thread",
        "It is the same as prompt caching: the hook is a cache_control marker on tool schemas",
    ],
    [
        "Corre en local en el ciclo de Claude Code y puede bloquear argumentos peligrosos de tools antes de ejecutarlos",
        "Afina Opus para rechazar bash metiendo el texto del hook en la mezcla de preentrenamiento",
        "Aumenta la ventana de contexto para que rm -rf quepa junto al resto del hilo",
        "Es lo mismo que prompt caching: el hook es un marcador cache_control en los esquemas de tools",
    ],
)
add(
    "q090",
    [
        "Data minimisation: do not retrieve full customer rows to answer “how many open tickets?”",
        "Allow/deny: the agent may have DB + email tools but not unconstrained Bash; mask PII in logs and third-party MCP",
        "Paste the full CRM into a public Slack MCP for easier debugging of address formats",
        "Hooks can make a disallowed usage-policy use case allowed if the regex is clever enough",
    ],
    [
        "Minimización de datos: no recuperar filas completas de cliente para responder «¿cuántos tickets abiertos?»",
        "Allow/deny: el agente puede tener tools de BD + correo pero no Bash libre; enmascarar PII en logs y MCP de terceros",
        "Pegar el CRM entero en un MCP público de Slack para depurar mejor los formatos de dirección",
        "Los hooks pueden convertir en permitido un caso vetado por la política de uso si la regex es hábil",
    ],
)
add(
    "q091",
    [
        "Short-circuit before query so you do not pay for a refusal you could make locally; they complement Claude’s safety training",
        "Run after you have already paid for a full Opus refusal, so the validator can learn from the model text",
        "Replace Anthropic’s usage policy entirely; a local regex is the credential’s source of truth",
        "Be pasted unaudited from a random GitHub into a bank agent because open-source validators are always safe",
    ],
    [
        "Cortar antes de la consulta para no pagar un rechazo que podéis hacer en local; complementan el entrenamiento de seguridad de Claude",
        "Correr después de haber pagado ya un rechazo completo de Opus, para que el validador aprenda del texto del modelo",
        "Sustituir por completo la política de uso de Anthropic; una regex local es la fuente de verdad de la credencial",
        "Pegarse sin auditar desde un GitHub al azar en un agente bancario porque los validadores open source siempre son seguros",
    ],
)
add(
    "q092",
    [
        "The action is irreversible (send offer letter, delete production data)",
        "You are printing “hello world” in a scratch file already gitignored",
        "You want to disable all evals so the agent is not slowed by graders",
        "You are only computing cosine similarity between two in-memory vectors",
    ],
    [
        "La acción es irreversible (enviar una carta de oferta, borrar datos de producción)",
        "Estáis imprimiendo «hello world» en un fichero temporal ya en gitignore",
        "Queréis desactivar todas las evals para que el agente no lo ralenticen los evaluadores",
        "Solo estáis calculando similitud coseno entre dos vectores en memoria",
    ],
)
add(
    "q093",
    [
        "Before logs, tickets, or MCP servers see the text — after generation, before exfiltration paths",
        "Only in CLAUDE.md as a suggestion the model may skip when the user is in a hurry",
        "Inside the Pearson exam NDA, which redacts PII from Messages responses automatically",
        "Only on Haiku, never on Sonnet, because larger models are assumed already safe",
    ],
    [
        "Antes de que logs, tickets o servidores MCP vean el texto: después de generar, antes de las vías de exfiltración",
        "Solo en CLAUDE.md como sugerencia que el modelo puede saltarse si el usuario tiene prisa",
        "Dentro del NDA del examen Pearson, que redacta PII de las respuestas Messages automáticamente",
        "Solo en Haiku, nunca en Sonnet, porque se asume que los modelos grandes ya son seguros",
    ],
)
add(
    "q094",
    [
        "Hooks are deterministic local policy; the model can still narrate a secret if you put it in context, but disk writes can be blocked",
        ".env files cannot be hooked because Claude Code ignores hidden paths in the lifecycle",
        "CLAUDE.md runs in the kernel, so hoping it is obeyed is equivalent to a file-permission bit",
        "Hooks bill more tokens than a second LLM format pass, so CLAUDE.md is the cheaper control",
    ],
    [
        "Los hooks son política local determinista; el modelo aún puede narrar un secreto si lo ponéis en contexto, pero se pueden bloquear escrituras a disco",
        "Los .env no admiten hooks porque Claude Code ignora rutas ocultas en el ciclo de vida",
        "CLAUDE.md corre en el kernel, así que confiar en que se obedezca equivale a un bit de permiso de fichero",
        "Los hooks facturan más tokens que un segundo paso LLM de formato, así que CLAUDE.md es el control más barato",
    ],
)
add(
    "q095",
    [
        "Anthropic’s strengthen-guardrails guidance and classroom RAI expect jailbreak, PII, and destructive-tool tests",
        "Evals are illegal for Foundation developers; only Architect Professional may test abuse cases",
        "Abuse cases refill usage bars, so they are a billing trick rather than a safety practice",
        "Pearson only scores happy-path items, so abuse evals cannot affect certification readiness",
    ],
    [
        "La guía de reforzar barreras de Anthropic y la RAI de clase esperan pruebas de jailbreak, PII y tools destructivas",
        "Las evals son ilegales para desarrolladores Foundation; solo Architect Professional puede probar abusos",
        "Los casos de abuso recargan las barras de uso, así que son un truco de facturación más que una práctica de seguridad",
        "Pearson solo puntúa el camino feliz, así que las evals de abuso no afectan a la preparación",
    ],
)
add(
    "q096",
    [
        "What is auto-approved versus when the loop pauses; start from current Code docs because UI strings change",
        "Which transformer architecture is used (Haiku versus a local Llama build)",
        "Whether Haiku can see images; permission modes are the vision feature flag",
        "Your Skilljar completion percentage, which Code reads before enabling auto mode",
    ],
    [
        "Qué se autoaprueba frente a cuándo el bucle pausa; partid de la documentación vigente de Code porque los textos de UI cambian",
        "Qué arquitectura transformer se usa (Haiku frente a un build Llama local)",
        "Si Haiku puede ver imágenes; los modos de permiso son el flag de visión",
        "Vuestro porcentaje de Skilljar, que Code lee antes de activar el modo auto",
    ],
)
add(
    "q097",
    [
        "A post-tool-use hook running npx prettier on disk does not consume generation tokens the way a second LLM rewrite does",
        "CLAUDE.md is still the right place for architecture, stack choice, and “never invent OpenAPI fields” — things Prettier cannot know",
        "Put Prettier indent rules only in CLAUDE.md so the model rewrites the file in a billed pass as the ideal design",
        "Hooks are skills you slash; they do not fire on Edit/Write unless you type /prettier every time",
    ],
    [
        "Un hook post-tool-use que corre npx prettier en disco no consume tokens de generación como una segunda reescritura LLM",
        "CLAUDE.md sigue siendo el sitio para arquitectura, stack y «no inventéis campos OpenAPI»: cosas que Prettier no puede saber",
        "Poner las reglas de indentación de Prettier solo en CLAUDE.md para que el modelo reescriba el fichero en un paso facturado",
        "Los hooks son skills que se invocan con barra; no saltan en Edit/Write salvo que escribáis /prettier cada vez",
    ],
)
add(
    "q098",
    [
        "Observability of how the window is eaten (system, tools, skills, messages, auto-compact buffer) so you can compact, start a new session, or pick a larger SKU",
        "A budget governor that hard-caps spend at 2k tokens per turn regardless of model",
        "The Cowork usage bar, aliased inside Code so both products share one meter",
        "An MCP marketplace search that lists servers whose schemas fit the remaining window",
    ],
    [
        "Observabilidad de cómo se come la ventana (system, tools, skills, messages, buffer de auto-compact) para compactar, abrir sesión nueva o elegir un SKU mayor",
        "Un gobernador de presupuesto que topa el gasto en 2k tokens por turno da igual el modelo",
        "La barra de uso de Cowork, alias dentro de Code para que ambos productos compartan contador",
        "Una búsqueda del marketplace MCP que lista servidores cuyos esquemas caben en la ventana restante",
    ],
)
add(
    "q099",
    [
        "Draft a prompt → build an eval set → run → grade with a score → revise (repeat)",
        "Book Pearson → pay → screenshot → forget → recertify",
        "Fine-tune → deploy → skip metrics → celebrate → delete logs",
        "Only LLM-as-judge nested three deep with no code graders and no labelled set",
    ],
    [
        "Borrar un prompt → montar un set de eval → ejecutar → puntuar → revisar (repetir)",
        "Reservar Pearson → pagar → captura → olvidar → recertificar",
        "Afinar → desplegar → saltarse métricas → celebrar → borrar logs",
        "Solo LLM-as-judge anidado tres veces, sin evaluadores de código ni set etiquetado",
    ],
)
add(
    "q100",
    [
        "For shape, types, and “exactly one sentence” — cheap and repeatable; it will not know if facts are true",
        "For brand voice in literary translation where no metric exists — code graders are always better than a judge",
        "Never; Foundation forbids regex and unit tests as exam-style graders",
        "Only when temperature is 2.0, because high entropy is what code graders were designed to catch",
    ],
    [
        "Para forma, tipos y «exactamente una frase»: barato y repetible; no sabrá si los hechos son verdaderos",
        "Para la voz de marca en traducción literaria sin métrica: los evaluadores de código siempre ganan a un juez",
        "Nunca; Foundation prohíbe regex y tests unitarios como evaluadores tipo examen",
        "Solo con temperature 2.0, porque la entropía alta es lo que los evaluadores de código se diseñaron para pillar",
    ],
)

# Fix typo in q099 ES: "Borrar" should be "Borrador/Redactar"
OPTS["q099"]["es"][0] = (
    "Redactar un prompt → montar un set de eval → ejecutar → puntuar → revisar (repetir)"
)
# Fix q051 typo
OPTS["q051"]["es"][3] = (
    "El reproductor de cursos Skilljar, porque secuenciavídeos sin humano en el bucle".replace(
        "secuenciavídeos", "secuencia vídeos"
    )
)


def place(options: list[str], n_correct: int, targets: list[int]) -> tuple[list[str], list[int]]:
    dest: list[str | None] = [None] * 4
    for i, t in enumerate(targets):
        dest[t] = options[i]
    wrongs = options[n_correct:]
    wi = 0
    for j in range(4):
        if dest[j] is None:
            dest[j] = wrongs[wi]
            wi += 1
    return [x for x in dest if x is not None], list(targets)


def main() -> None:
    bank = json.loads(SRC.read_text())
    missing = [q["id"] for q in bank if q["id"] not in OPTS]
    extra = [k for k in OPTS if k not in {q["id"] for q in bank}]
    if missing or extra:
        raise SystemExit(f"id mismatch missing={missing} extra={extra}")

    singles = [q for q in bank if q["select"] == 1]
    multis = [q for q in bank if q["select"] != 1]
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    for i, q in enumerate(singles):
        target = [i % 4]
        n = q["select"]
        spec = OPTS[q["id"]]
        for lang in ("en", "es"):
            opts, correct = place(spec[lang], n, target)
            q[lang]["options"] = opts
            q[lang]["correct"] = correct

    for i, q in enumerate(multis):
        pair = pairs[i % 6]
        n = q["select"]
        spec = OPTS[q["id"]]
        for lang in ("en", "es"):
            opts, correct = place(spec[lang], n, list(pair))
            q[lang]["options"] = opts
            q[lang]["correct"] = correct

    # sanity
    for q in bank:
        assert q["en"]["correct"] == q["es"]["correct"], q["id"]
        assert len(q["en"]["options"]) == 4
        assert q["select"] == len(q["en"]["correct"])

    sc = Counter(q["en"]["correct"][0] for q in singles)
    print("single letters", {chr(65 + k): v for k, v in sorted(sc.items())})
    mc = Counter(tuple(q["en"]["correct"]) for q in multis)
    print("multi pairs", mc)

    ratios = []
    for q in bank:
        lens = [len(o) for o in q["en"]["options"]]
        ratios.append(max(lens) / max(min(lens), 1))
    print("max length ratio", round(max(ratios), 2), "median", round(sorted(ratios)[len(ratios) // 2], 2))
    over = [q["id"] for q in bank if max(len(o) for o in q["en"]["options"]) / max(min(len(o) for o in q["en"]["options"]), 1) > 2.2]
    print("ratio>2.2", over)

    SRC.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n")
    print("wrote", SRC)


if __name__ == "__main__":
    main()
