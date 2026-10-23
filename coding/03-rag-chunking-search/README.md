# [코딩] AI로 프로그램 만들기 3편: 내 문서로 답하게 하기: 모른다던 AI가 문서를 붙이니 3개를 맞힌 거다

이 편에 필요한 것: Python 기초 문법(리스트·딕셔너리·for문·함수), pip install anthropic, Anthropic API 키(search.py는 키 없이 실행된다)

## 파일

- `no_rag.py`
- `search.py`
- `rag.py`
- `sample_output_*.txt`: 영상을 만들 때 실제로 나온 실행 결과

## 실행

저장소 맨 위의 README대로 준비한 뒤:

```bash
cd coding/03-rag-chunking-search
python no_rag.py
python search.py
python rag.py
```

AI의 답은 실행할 때마다 달라서, 결과가 영상과 조금 다를 수 있습니다.
