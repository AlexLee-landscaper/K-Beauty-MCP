# Example Claude Desktop Configuration

Add this to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "k-beauty": {
      "command": "uv",
      "args": [
        "--directory", 
        "/ABSOLUTE/PATH/TO/k-beauty-mcp",
        "run",
        "kbeauty_mcp.py"
      ]
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/k-beauty-mcp` with the actual path to your project directory.

## Example Queries

Once connected to Claude Desktop, try these queries:

- "What K-Beauty brands do you know about?"
- "Tell me about COSRX snail mucin products"
- "I have oily, acne-prone skin. Recommend a Korean skincare routine"
- "What are the benefits of ginseng in skincare?"
- "Compare Laneige Water Sleeping Mask with Sulwhasoo Concentrated Ginseng Cream"
- "Is niacinamide safe for sensitive skin?"
