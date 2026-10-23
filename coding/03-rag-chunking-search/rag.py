import json
import math
import re
from collections import Counter

import anthropic

client = anthropic.Anthropic()
with open("docs.json", encoding="utf-8") as f:
    DOCS = json.load(f)

QUESTIONS = [
    "즌다 마을 도서관은 일요일에 몇 시에 닫아?",
    "에다마메 축제 입장료는 얼마야?",
    "즌다 마을 3번 버스는 몇 분마다 와?",
    "즌다 마을 촌장 이름이 뭐야?",
]
SYSTEM = (
    "아래 자료만 보고 한 문장으로 답해라. "
    "자료에 없으면 '자료에 없다'고 답해라."
)


def embed(text):
    clean = re.sub(r"[^가-힣a-z0-9]", "", text.lower())
    return Counter(clean[i:i + 2] for i in range(len(clean) - 1))


def cosine(a, b):
    dot = sum(a[k] * b[k] for k in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


# 1. 청킹: 문장 하나 = 청크 하나
CHUNKS = []
for doc in DOCS:
    for s in re.split(r"(?<=[.!?])\s+", doc["text"]):
        CHUNKS.append({"id": doc["id"], "text": f"[{doc['title']}] {s}"})
# 2. 임베딩: 미리 한 번만 계산해 둔다
VECTORS = [embed(c["text"]) for c in CHUNKS]


def ask(question):
    # 3. 검색: 질문과 가장 비슷한 청크 3개
    q = embed(question)
    scores = [cosine(q, v) for v in VECTORS]
    ranked = sorted(range(len(CHUNKS)), key=lambda i: scores[i], reverse=True)
    top = [CHUNKS[i] for i in ranked[:3]]
    context = "\n".join(f"- {c['text']}" for c in top)
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1024,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"자료:\n{context}\n\n질문: {question}"}],
    )
    answer = "".join(b.text for b in response.content if b.type == "text")
    return top, answer.strip().replace("\n", " ")


for question in QUESTIONS:
    top, answer = ask(question)
    print(f"Q: {question}")
    print(f"  근거: {', '.join(c['id'] for c in top)}")
    print(f"  A: {answer}")
