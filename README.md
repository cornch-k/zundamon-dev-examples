# 즌다몬과 배우는 개발 · 예제 코드

유튜브 영상에서 쓰는 예제 코드 모음입니다. 영상 화면에 나오는 코드와 줄 번호가 같습니다.

## 실행 준비

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=여기에_내_API_키
```

API 키는 [Anthropic Console](https://console.anthropic.com/)에서 발급받습니다. 키는 코드에 직접 쓰지 말고 환경 변수에 넣어 두세요.
예제를 실행하면 API 사용 요금이 조금 나옵니다.

## 시리즈 1: 생성형 AI 기법·사용법

| 편 | 주제 | 폴더 |
|---|---|---|
| 1 | 같은 질문, 다른 답: 좋은 프롬프트의 4요소 | [genai/01-prompt-4-elements](genai/01-prompt-4-elements) |

## 참고

- AI의 답은 실행할 때마다 달라집니다. 각 폴더의 `sample_output_*.txt`는 영상을 만들 때 실제로 나온 결과이고, 직접 실행하면 내용과 글자 수가 조금씩 다를 수 있습니다.
- 음성: Voiceger:Zundamon
- 立ち絵: 坂本アヒル
