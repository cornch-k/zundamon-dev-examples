import anthropic

client = anthropic.Anthropic()
SYSTEM = "답은 한국어 2문장 이내로 짧게 한다."
QUESTION = "내 메모 파일에서 찾아 줘. 발표는 언제, 어디서 하는 거야?"

# 도구 없이 그냥 물어본다
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    system=SYSTEM,
    messages=[{"role": "user", "content": QUESTION}],
)

answer = "".join(b.text for b in response.content if b.type == "text")
print("질문:", QUESTION)
print("stop_reason:", response.stop_reason)
print("답:")
lines = [line for line in answer.splitlines() if line.strip()]
for line in lines[:12]:
    print("  " + line)
if len(lines) > 12:
    print("  (이하 생략)")
