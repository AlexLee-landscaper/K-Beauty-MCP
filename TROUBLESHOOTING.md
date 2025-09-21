# 🔧 Troubleshooting Guide

## 일반적인 문제 및 해결책

### 1. 종속성 충돌 오류
```bash
ERROR: Cannot install fastapi 0.104.1 and mcp 1.0.0 because these package versions have conflicting dependencies.
```

**해결책:**
```bash
python3 -m pip install mcp aiohttp beautifulsoup4 requests --upgrade
```

### 2. Claude Desktop 연결 실패
**증상**: MCP 서버가 "연결 오류"로 표시됨

**해결책:**
1. JSON 구문 검증:
   ```bash
   python3 -m json.tool ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. 경로 확인:
   ```bash
   ls -la /Users/iyong-ug/Desktop/k-beauty-mcp/kbeauty/kbeauty_mcp.py
   ```

3. Python 경로 확인:
   ```bash
   which python3
   ```

### 3. UV vs Python3 실행
❌ **작동하지 않음:**
```json
"command": "uv",
"args": ["--directory", "/path", "run", "kbeauty_mcp.py"]
```

✅ **작동함:**
```json
"command": "python3",
"args": ["/full/path/to/kbeauty_mcp.py"],
"cwd": "/full/path/to/directory"
```

### 4. 백업 및 복원
**백업 생성:**
```bash
mkdir -p ~/Library/Application\ Support/Claude/backups
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/Library/Application\ Support/Claude/backups/claude_config_backup_$(date +%Y%m%d_%H%M%S).json
```

**복원:**
```bash
cp ~/Library/Application\ Support/Claude/backups/claude_config_backup_YYYYMMDD_HHMMSS.json \
   ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 5. 실행 권한 확인
```bash
chmod +x /Users/iyong-ug/Desktop/k-beauty-mcp/kbeauty/kbeauty_mcp.py
```

## 🆘 긴급 복구 스크립트
```python
def emergency_restore():
    import os, glob, shutil
    backup_dir = "~/Library/Application Support/Claude/backups"
    config_path = "~/Library/Application Support/Claude/claude_desktop_config.json"
    
    backups = glob.glob(os.path.expanduser(f"{backup_dir}/claude_config_backup_*.json"))
    if backups:
        latest = max(backups, key=os.path.getctime)
        shutil.copy2(latest, os.path.expanduser(config_path))
        print(f"✅ 복원 완료: {latest}")
    else:
        print("❌ 백업을 찾을 수 없습니다")
```
