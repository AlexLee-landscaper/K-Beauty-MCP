# K-Beauty MCP Server 🌸

A Model Context Protocol (MCP) server providing comprehensive K-Beauty (Korean Beauty) information, ingredient analysis, and skincare routine recommendations.

## Features ✨

- **Brand Database**: Information on popular K-Beauty brands (Sulwhasoo, COSRX, Laneige, etc.)
- **Product Search**: Detailed product information including prices, benefits, and skin type recommendations
- **Ingredient Analysis**: Safety grades, benefits, and suitability analysis for skincare ingredients
- **Routine Recommendations**: Customized Korean skincare routines based on skin type and concerns
- **Product Comparison**: Side-by-side comparison of K-Beauty products
- **Multilingual Support**: English and Korean product/ingredient names

## Quick Start 🚀

### Prerequisites
- Python 3.10+
- uv package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/k-beauty-mcp.git
cd k-beauty-mcp

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv add mcp requests
```

### Running the Server

```bash
# Start the MCP server
python kbeauty_mcp.py
```

### Claude Desktop Integration

Add to your Claude Desktop configuration (`~/AppData/Roaming/Claude/claude_desktop_config.json` on Windows or `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

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

## Available Tools 🛠️

### 1. `search_kbeauty_brands`
Search and discover K-Beauty brands by name or category.

**Example**: "Find luxury K-Beauty brands" or "Tell me about COSRX"

### 2. `get_product_info`
Get detailed information about specific K-Beauty products.

**Example**: "Show me COSRX snail essence details" or "What products does Sulwhasoo offer?"

### 3. `analyze_ingredients`
Analyze skincare ingredients for safety, benefits, and suitability.

**Example**: "Is niacinamide safe?" or "Tell me about snail secretion benefits"

### 4. `recommend_routine`
Get personalized Korean skincare routine recommendations.

**Example**: "Recommend a routine for oily, acne-prone skin" or "I need an anti-aging routine"

### 5. `compare_products`
Compare multiple K-Beauty products side by side.

**Example**: "Compare Laneige Water Sleeping Mask vs Sulwhasoo First Care Serum"

## Sample Usage 💬

```
User: "I have dry, sensitive skin. What K-Beauty routine do you recommend?"

K-Beauty MCP will provide:
- Customized routine steps
- Product recommendations
- Specific tips for dry, sensitive skin
- Korean skincare philosophy explanation
```

```
User: "What's so special about snail mucin in Korean skincare?"

K-Beauty MCP will explain:
- Scientific benefits of snail secretion
- Popular snail-based products
- How to incorporate into routine
- Safety information
```

## Supported Brands 🏷️

- **Sulwhasoo (설화수)** - Luxury ginseng-based skincare
- **COSRX** - Effective, minimal ingredient products
- **Laneige (라네즈)** - Water science and hydration experts
- *(More brands being added)*

## Ingredient Database 🧪

Currently includes analysis for:
- Snail Secretion Filtrate
- Ginseng Extract  
- Niacinamide (Vitamin B3)
- Hyaluronic Acid
- *(Expanding database)*

## Contributing 🤝

We welcome contributions! Please feel free to:
- Add more K-Beauty brands and products
- Expand the ingredient database
- Improve routine recommendations
- Add new features

## License 📄

MIT License - feel free to use and modify!

## Roadmap 🗺️

- [ ] Real-time price integration
- [ ] More comprehensive brand database
- [ ] Ingredient interaction warnings
- [ ] Seasonal routine recommendations
- [ ] K-Beauty trend analysis
- [ ] Integration with beauty review platforms

---

**Made with ❤️ for K-Beauty enthusiasts worldwide**
