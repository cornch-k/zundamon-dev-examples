import json
import anthropic

client = anthropic.Anthropic()

memo = "내일 3시 팀 회의. 금요일까지 보고서 제출. 토요일 전에 엄마 생신 선물 사기. 헬스장 등록 알아보기."

prompt = f"""다음 메모에서 할 일을 뽑아서 JSON으로만 답해줘.
형식: {{"todos": [{{"title": "...", "due": "...", "category": "업무 또는 개인"}}]}}
기한이 없으면 due는 "없음".

메모: {memo}"""

ok = 0
for i in range(10):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    try:
        json.loads(text)
        ok += 1
        print(f"{i + 1}번: 성공")
    except json.JSONDecodeError:
        print(f"{i + 1}번: 실패 → {text[:40]!r}")

print(f"10번 중 {ok}번 성공")
