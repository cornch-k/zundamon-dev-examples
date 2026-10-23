import json
import anthropic

client = anthropic.Anthropic()

memo = "내일 3시 팀 회의. 금요일까지 보고서 제출. 토요일 전에 엄마 생신 선물 사기. 헬스장 등록 알아보기."

schema = {
    "type": "object",
    "properties": {
        "todos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "due": {"type": "string"},
                    "category": {"type": "string", "enum": ["업무", "개인"]},
                },
                "required": ["title", "due", "category"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["todos"],
    "additionalProperties": False,
}

ok = 0
for i in range(10):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"다음 메모에서 할 일을 뽑아줘. 기한이 없으면 due는 \"없음\".\n\n메모: {memo}"}],
        output_config={"format": {"type": "json_schema", "schema": schema}},
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    data = json.loads(text)
    ok += 1

print(f"10번 중 {ok}번 성공")

for todo in data["todos"]:
    print(f"[{todo['category']}] {todo['title']} (기한: {todo['due']})")

by_category = {"업무": [], "개인": []}
for todo in data["todos"]:
    by_category[todo["category"]].append(todo["title"])

for category, titles in by_category.items():
    print(f"{category} {len(titles)}개: {', '.join(titles)}")
