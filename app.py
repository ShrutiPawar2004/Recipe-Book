import os
from datetime import datetime
from dotenv import load_dotenv
import streamlit as st

from tavily import TavilyClient
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# -------------------------------
# 1️⃣ Load environment variables
# -------------------------------
load_dotenv()

TAVILY_KEY = os.getenv("TAVILY_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

if not TAVILY_KEY or not HF_TOKEN:
    st.error("Please set TAVILY_API_KEY and HF_TOKEN as environment variables.")
    st.stop()

# -------------------------------
# 2️⃣ Initialize clients
# -------------------------------
tavily = TavilyClient(api_key=TAVILY_KEY)

endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    max_new_tokens=200,
)

llm = ChatHuggingFace(llm=endpoint)

# -------------------------------
# 3️⃣ Streamlit session memory
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# 4️⃣ Utility functions
# -------------------------------
def is_biography_question(query: str) -> bool:
    keywords = [
        "who is", "biography", "about", "profile",
        "professional footballer", "career"
    ]
    return any(k in query.lower() for k in keywords)


def get_web_context(query: str):
    results = tavily.search(query=query, max_results=3)
    context = []
    sources = []

    for r in results.get("results", []):
        context.append(r["content"])
        sources.append(r["url"])

    return context, sources


def build_prompt(query, context, history):
    today = datetime.now().strftime("%Y-%m-%d")

    history_text = ""
    for turn in history[-4:]:
        history_text += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"

    prompt = f"""
Today's date is {today}.

You are a fact-checking assistant.

STRICT RULES (NON-NEGOTIABLE):
- Answer ONLY using the web context provided.
- IGNORE all pretrained or internal knowledge.
- If the answer is not found in the web context, say:
  "I couldn't find reliable up-to-date information."
- DO NOT generate biographies unless explicitly asked.
- DO NOT guess or use outdated facts.
- Prefer the MOST RECENT information.

Conversation history:
{history_text}

Web context:
{context}

User question:
{query}

FINAL ANSWER (max 3 short sentences, clear and factual):
"""
    return prompt


def chatbot(query):
    # Force recency for vague biography questions
    if is_biography_question(query):
        query = f"{query} current club and status as of today"

    context, sources = get_web_context(query)

    prompt = build_prompt(query, context, st.session_state.chat_history)

    response = llm.invoke(prompt)

    clean_answer = response.content.strip()

    return clean_answer, sources


# -------------------------------
# 5️⃣ Streamlit UI
# -------------------------------
st.set_page_config(page_title="Fact-Safe RAG Chatbot", page_icon="🤖")
st.title("🤖 Fact-Safe RAG Chatbot")
st.caption("Web-grounded • Time-aware • No outdated hallucinations")

user_input = st.text_input("Ask a question (current facts only):")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        answer, sources = chatbot(user_input)

    # Save conversation
    st.session_state.chat_history.append({
        "user": user_input,
        "bot": answer
    })

    # Display answer
    st.markdown("### ✅ Answer")
    st.write(answer)

    # Display sources
    if sources:
        st.markdown("### 🔗 Sources")
        for s in sources:
            st.write(s)

# -------------------------------
# 6️⃣ Conversation history display
# -------------------------------
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### 🧠 Conversation History")

    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Bot:** {chat['bot']}")
