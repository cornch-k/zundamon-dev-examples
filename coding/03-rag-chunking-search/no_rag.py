import anthropic

client = anthropic.Anthropic()

QUESTIONS = [
    "즌다 마을 도서관은 일요일에 몇 시에 닫아?",
    "에다마메 축제 입장료는 얼마야?",
    "즌다 마을 3번 버스는 몇 분마다 와?",
    "즌다 마을 촌장 이름이 뭐야?",
]

# 문서 없이 그냥 물어본다
for question in QUESTIONS:
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1024,
        system="한 문장으로 답해라.",
        messages=[{"role": "user", "content": question}],
    )
    answer = "".join(b.text for b in response.content if b.type == "text")
    print(f"Q: {question}")
    print(f"  A: {answer.strip().replace(chr(10), ' ')}")
