import json
import math
import re
from collections import Counter

with open("docs.json", encoding="utf-8") as f:
    DOCS = json.load(f)

QUESTIONS = [
    "즌다 마을 도서관은 일요일에 몇 시에 닫아?",
    "에다마메 축제 입장료는 얼마야?",
    "즌다 마을 3번 버스는 몇 분마다 와?",
    "즌다 마을 촌장 이름이 뭐야?",
]


def make_chunks(by_sentence):
    """청킹: 문서 통째로 한 청크, 또는 문장 하나씩 한 청크"""
    chunks = []
    for doc in DOCS:
        parts = re.split(r"(?<=[.!?])\s+", doc["text"]) if by_sentence else [doc["text"]]
        for part in parts:
            chunks.append({"id": doc["id"], "text": f"[{doc['title']}] {part}"})
    return chunks


def embed(text):
    """장난감 임베딩: 글자를 2개씩 묶어 몇 번 나오는지 센다"""
    clean = re.sub(r"[^가-힣a-z0-9]", "", text.lower())
    return Counter(clean[i:i + 2] for i in range(len(clean) - 1))


def cosine(a, b):
    """두 벡터가 같은 방향일수록 1에 가깝다"""
    dot = sum(a[k] * b[k] for k in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def search(question, chunks, k=3):
    q = embed(question)
    scored = [(cosine(q, embed(c["text"])), c) for c in chunks]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:k]


for by_sentence in [False, True]:
    chunks = make_chunks(by_sentence)
    label = "문장 하나씩" if by_sentence else "문서 통째로"
    print(f"===== {label}: 청크 {len(chunks)}개 =====")
    for question in QUESTIONS:
        top = search(question, chunks)
        total = sum(len(c["text"]) for _, c in top)
        score, best = top[0]
        print(f"Q: {question}")
        print(f"  상위 3개: {' '.join(c['id'] for _, c in top)}  (합계 {total}자)")
        print(f"  1위 {score:.2f} {best['text'][:30]}")
