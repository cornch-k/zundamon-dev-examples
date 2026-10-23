import anthropic

client = anthropic.Anthropic()


def ask(prompt):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    # 답에는 생각(thinking) 블록도 섞여 오므로 text 블록만 모은다
    return "".join(block.text for block in response.content if block.type == "text")


vague = "리스트 컴프리헨션 설명해줘"

specific = """너는 파이썬 강사다.
반복문만 아는 입문자에게 리스트 컴프리헨션을 설명해줘.
형식: 한 줄 정의, 예제 코드 1개(for문 버전과 비교), 주의할 점 1개.
제약: 전체 300자 이내."""

for name, prompt in [("막연한 요청", vague), ("구체적인 요청", specific)]:
    answer = ask(prompt)
    print(f"===== {name} ({len(answer)}자) =====")
    print(answer)
    print()
