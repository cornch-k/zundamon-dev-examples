import json
import anthropic

client = anthropic.Anthropic()
SYSTEM = "답은 한국어 2문장 이내로 짧게 한다."
QUESTION = "내 메모 파일에서 찾아 줘. 발표는 언제, 어디서 하는 거야?"

# 도구의 '설명서'만 건넨다. 함수 본체는 아직 없다.
tools = [
    {"name": "search_files",
     "description": "키워드가 들어 있는 메모 파일 이름 목록을 돌려준다.",
     "input_schema": {"type": "object",
                      "properties": {"keyword": {"type": "string"}},
                      "required": ["keyword"]}},
    {"name": "read_file",
     "description": "메모 파일 하나의 내용을 돌려준다.",
     "input_schema": {"type": "object",
                      "properties": {"name": {"type": "string"}},
                      "required": ["name"]}},
]

# 딱 한 번만 호출한다
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    system=SYSTEM,
    tools=tools,
    messages=[{"role": "user", "content": QUESTION}],
)

print("stop_reason:", response.stop_reason)
print("content 블록:")
for block in response.content:
    if block.type == "text":
        print("  [text]", block.text.replace("\n", " ")[:40])
    elif block.type == "tool_use":
        args = json.dumps(block.input, ensure_ascii=False)
        print("  [tool_use]", block.name, args)
    else:
        print("  [" + block.type + "]")

answer = "".join(b.text for b in response.content if b.type == "text")
print("꺼낸 답 텍스트:", repr(answer[:40]))
