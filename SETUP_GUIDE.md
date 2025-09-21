# 🛠️ K-Beauty MCP 설정 가이드

## ✅ 성공적인 설정 방법 (2025년 9월)

### 1. 종속성 설치
```bash
cd /path/to/k-beauty-mcp/kbeauty
python3 -m pip install mcp aiohttp beautifulsoup4 requests --upgrade
```

### 2. Claude Desktop 설정
`~/Library/Application Support/Claude/claude_desktop_config.json`에 추가:

```json
{
  "mcpServers": {
    "k-beauty": {
      "command": "python3",
      "args": ["/full/path/to/k-beauty-mcp/kbeauty/kbeauty_mcp.py"],
      "cwd": "/full/path/to/k-beauty-mcp/kbeauty"
    }
  }
}
```

### 3. 검증된 환경
- **macOS**: ✅ 테스트 완료
- **Python**: 3.12.8 (권장)
- **MCP**: 1.14.1 (최신)

### 4. 문제 해결
- 종속성 충돌 시: `--upgrade` 플래그 사용
- `uv` 대신 `python3` 직접 실행 권장
- Claude Desktop 재시작 필수

### 5. 테스트 명령어
```
"Tell me about COSRX snail essence"
"Recommend a K-Beauty routine for sensitive skin"
```

---
**설정 완료일**: 2025년 9월 21일  
**테스트 환경**: macOS, Python 3.12.8, MCP 1.14.1
