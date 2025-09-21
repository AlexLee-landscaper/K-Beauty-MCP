# 🌸 K-Beauty MCP Server

> **Claude를 위한 K-Beauty 전문가 도우미**

Claude와 함께 K-Beauty 제품을 검색하고 개인 맞춤 스킨케어 루틴을 추천받으세요!

## ✨ 주요 기능

- 📱 **AI 피부 분석** - 셀카로 개인 맞춤 루틴 추천
- 🔍 **실시간 제품 검색** - 58개 K-Beauty 브랜드 정보  
- 🧪 **성분 분석** - 48개 핵심 성분 상세 정보
- 💆‍♀️ **맞춤 루틴** - 10단계 한국식 스킨케어

## 🚀 빠른 시작

```bash
pip install -r requirements.txt
```

Claude Desktop 설정에 추가:
```json
{
  "mcpServers": {
    "k-beauty": {
      "command": "python3", 
      "args": ["./kbeauty_mcp.py"]
    }
  }
}
```

## 💬 사용 예시

```
"COSRX 달팽이 에센스에 대해 알려줘"
"민감성 피부 K-Beauty 루틴 추천해줘" 
"설화수와 라네즈 제품 비교해줘"
```

## 📚 문서

- [📖 상세 설정 가이드](SETUP_GUIDE.md)
- [🔧 문제해결](TROUBLESHOOTING.md)  
- [🌸 소개 및 기능](INTRO.md)

---

**K-Beauty의 모든 것을 Claude와 함께! 🌸✨**
