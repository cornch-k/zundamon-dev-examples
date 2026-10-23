import json
import anthropic

client = anthropic.Anthropic()
SYSTEM = "답은 한국어 2문장 이내로 짧게 한다."
QUESTION = "내 메모 파일에서 찾아 줘. 발표는 언제, 어디서 하는 거야?"

with open("docs.json", encoding="utf-8") as f:
    DOCS = json.load(f)  # {파일 이름: 내용} 모양의 가상 메모 폴더


def run_tool(name, args):
    """도구를 실제로 실행하는 곳. (결과 문자열, 에러 여부)를 돌려준다."""
    if name == "search_files":
        hits = [n for n, body in DOCS.items() if args["keyword"] in n + body]
        return json.dumps(hits, ensure_ascii=False), False
    if name == "read_file":
        if args["name"] not in DOCS:
            return args["name"] + " 파일은 없다.", True
        return DOCS[args["name"]], False
    return "모르는 도구: " + name, True


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

messages = [{"role": "user", "content": QUESTION}]
for call in range(1, 11):  # 안전장치: API 호출은 최대 10번
    response = client.messages.create(model="claude-haiku-5-5", max_tokens=4096,
                                      system=SYSTEM, tools=tools, messages=messages)
    if response.stop_reason != "tool_use":
        break
    messages.append({"role": "assistant", "content": response.content})
    results = []
    for block in response.content:
        if block.type == "tool_use":
            output, is_error = run_tool(block.name, block.input)
            args = json.dumps(block.input, ensure_ascii=False)
            print(f"[{call}번째 호출] {block.name}({args})")
            print("    →", output.replace("\n", " ")[:40], "(에러)" if is_error else "")
            results.append({"type": "tool_result", "tool_use_id": block.id,
                            "content": output, "is_error": is_error})
    messages.append({"role": "user", "content": results})

answer = "".join(b.text for b in response.content if b.type == "text")
print("API 호출 횟수:", call, "/ stop_reason:", response.stop_reason)
print("최종 답:", answer)
