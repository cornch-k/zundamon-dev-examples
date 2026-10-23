# [코딩] AI로 프로그램 만들기 2편: AI에게 함수를 쥐여 주기: 빈 답이던 게 루프 3번에 바뀐 장소까지 찾는 거다

이 편에 필요한 것: Python 기초 문법(리스트·딕셔너리·for·함수), pip install anthropic, Anthropic API 키, 1편의 messages.create 호출(몰라도 따라올 수 있다)

## 파일

- `no_tools.py`
- `one_call.py`
- `agent_loop.py`
- `sample_output_*.txt`: 영상을 만들 때 실제로 나온 실행 결과

## 실행

저장소 맨 위의 README대로 준비한 뒤:

```bash
cd coding/02-tool-use-agent-loop
python no_tools.py
python one_call.py
python agent_loop.py
```

AI의 답은 실행할 때마다 달라서, 결과가 영상과 조금 다를 수 있습니다.
