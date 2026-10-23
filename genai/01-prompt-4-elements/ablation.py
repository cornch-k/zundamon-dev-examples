import anthropic

client = anthropic.Anthropic()


def ask(prompt):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


task = "리스트 컴프리헨션을 설명해줘."
parts = {
    "역할": "너는 파이썬 강사다.",
    "대상": "읽는 사람은 반복문만 아는 입문자다.",
    "형식": "형식: 한 줄 정의, 예제 코드 1개(for문 버전과 비교), 주의할 점 1개.",
    "제약": "제약: 전체 300자 이내.",
}

for removed in [None, *parts]:
    kept = [text for name, text in parts.items() if name != removed]
    prompt = "\n".join([task, *kept])
    answers = [ask(prompt) for _ in range(3)]  # 답이 매번 달라지므로 3번씩 돌린다
    lengths = [len(a) for a in answers]
    label = "4요소 전부" if removed is None else f"{removed} 빼기"
    print(f"===== {label}: {lengths}자, 평균 {sum(lengths) // 3}자 =====")
    print(answers[0])
    print()
