# [코딩] 1편: AI 답을 JSON으로 고정하기

이 편에 필요한 것: Python 기초 문법(리스트·딕셔너리·for·함수), `pip install anthropic`, Anthropic API 키

## 파일

| 파일 | 하는 일 |
|---|---|
| `prompt_only.py` | 프롬프트로 "JSON으로만 답해줘"라고 부탁하고, 10번 중 몇 번 `json.loads`가 성공하는지 센다 |
| `schema_output.py` | 같은 일을 `output_config`의 JSON 스키마로 시키고, 결과를 업무/개인으로 나눠 출력한다 |
| `sample_output_*.txt` | 영상을 만들 때 실제로 나온 실행 결과 |

## 실행

저장소 맨 위의 README대로 준비한 뒤:

```bash
cd coding/01-json-structured-output
python prompt_only.py
python schema_output.py
```

각 파일은 API를 10번 호출합니다.

## 영상에서 나온 결과

- `prompt_only.py`: 10번 중 5번 성공. 실패한 5번은 모두 답이 ```` ```json ```` 코드 블록으로 감싸져 있었다.
- `schema_output.py`: 10번 중 10번 성공.

## 해 볼 만한 것

- 스키마에 `priority`(`높음`/`보통`/`낮음`) 키를 추가해 보기
- `due`를 `"format": "date"`로 바꾸고 메모에 날짜를 넣어 보기
- 메모를 길게 늘려서 할 일을 빠뜨리지 않는지 확인하기
