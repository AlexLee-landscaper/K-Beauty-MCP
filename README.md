# 🌸 K-Beauty MCP Server

A Model Context Protocol (MCP) server that provides comprehensive Korean Beauty (K-Beauty) information through **real-time web search** and curated knowledge.

## ✨ Features

### 🔍 **Real-Time Web Search Integration**
- Live search for K-Beauty products, brands, and ingredients
- Latest reviews and product information
- Up-to-date pricing and availability
- Current trends and recommendations

### 💄 **Comprehensive Brand Database**
- **Luxury Brands:** Sulwhasoo, Whoo, OHUI, Hera
- **Popular Brands:** Laneige, Innisfree, Etude House, The Face Shop
- **Indie/Effective:** COSRX, Beauty of Joseon, Purito, Dear Klairs
- **Global Favorites:** Dr. Jart+, Banila Co, Son & Park

### 🧪 **Ingredient Analysis Engine**
- **Star Ingredients:** Snail mucin, Ginseng, Centella asiatica, Propolis
- **Traditional Hanbang:** Rice water, Mugwort, Red bean, Bamboo
- **Modern Actives:** Niacinamide, Hyaluronic acid, Peptides, Ceramides
- Safety ratings and compatibility checks

### 💆‍♀️ **Personalized Skincare Routines**
- Korean 10-step routine customization
- Skin type-specific recommendations (oily, dry, combination, sensitive)
- Age-appropriate anti-aging routines
- Seasonal skincare adjustments

### 🌍 **Global Accessibility**
- **Multi-language Support:** English and Korean
- **Worldwide Availability:** No API keys required
- **Offline Capability:** Works with curated knowledge base

## 🚀 Quick Start

### Installation

```bash
# Clone or download to your desired location
cd /path/to/your/mcp/servers
git clone <your-repo-url> k-beauty-mcp
cd k-beauty-mcp

# Install dependencies
pip install -r requirements.txt
```

### Claude Desktop Configuration

Add to your Claude Desktop config file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "k-beauty": {
      "command": "python3",
      "args": ["/full/path/to/k-beauty-mcp/kbeauty_mcp.py"],
      "cwd": "/full/path/to/k-beauty-mcp"
    }
  }
}
```

**macOS/Linux config location:**
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows config location:**
```bash
%APPDATA%\Claude\claude_desktop_config.json
```

### Quick Test

Restart Claude Desktop and try these queries:

```
"Tell me about COSRX snail essence"
"Recommend a K-Beauty routine for sensitive skin"
"What are the benefits of ginseng in skincare?"
"Compare Sulwhasoo vs Laneige products"
```

## 🛠️ Available Tools

### 1. `search_kbeauty_brands`
Search and get information about K-Beauty brands
```
Input: Brand name or category
Output: Brand details, history, popular products
```

### 2. `get_product_info`
Get detailed product information
```
Input: Brand name, optional product name
Output: Product details, benefits, pricing, reviews
```

### 3. `analyze_ingredients`
Analyze skincare ingredients
```
Input: Ingredient name
Output: Benefits, safety, usage recommendations
```

### 4. `recommend_routine`
Get personalized skincare routines
```
Input: Skin type, concerns, routine type
Output: Step-by-step Korean skincare routine
```

### 5. `compare_products`
Compare multiple K-Beauty products
```
Input: List of products to compare
Output: Side-by-side comparison with pros/cons
```

## 💡 Example Interactions

### Brand Discovery
```
User: "What's a good affordable K-Beauty brand for beginners?"
Assistant: [Searches and provides COSRX, Beauty of Joseon recommendations]
```

### Product Research
```
User: "Tell me about Beauty of Joseon Glow Deep Serum"
Assistant: [Live search + curated info about ingredients, benefits, reviews]
```

### Routine Building
```
User: "I have oily, acne-prone skin. What's a good Korean routine?"
Assistant: [Customized 7-step routine with specific product recommendations]
```

### Ingredient Education
```
User: "Is snail mucin actually good for skin?"
Assistant: [Detailed analysis of snail secretion benefits, safety, best products]
```

## 🌟 What Makes This Special

### Real-Time Information
- **Live Web Search:** Always up-to-date product info and reviews
- **Current Pricing:** Latest prices and availability
- **Trend Tracking:** What's popular right now in K-Beauty

### Cultural Context
- **Traditional Hanbang:** Korean traditional medicine ingredients
- **Modern Innovation:** How Korean brands revolutionized skincare
- **Cultural Significance:** Understanding the philosophy behind K-Beauty

### Practical Guidance
- **Step-by-Step Routines:** Clear, actionable skincare guidance
- **Product Matching:** Find products that work together
- **Skin-Type Specific:** Recommendations tailored to your needs

## 🔧 Technical Details

### Architecture
- **Language:** Python 3.8+
- **Framework:** Model Context Protocol (MCP)
- **Search Engine:** DuckDuckGo API (no API key required)
- **Fallback Database:** Curated K-Beauty knowledge

### Dependencies
- `mcp>=1.0.0` - Model Context Protocol
- `aiohttp>=3.9.0` - Async HTTP client for web search
- `beautifulsoup4>=4.12.0` - HTML parsing (if needed)

### Performance
- **Response Time:** <2 seconds for most queries
- **Offline Mode:** Works without internet using curated data
- **Cache-Friendly:** Reuses common search results

## 🤝 Contributing

This is an open-source K-Beauty knowledge project! Contributions welcome:

1. **Brand Information:** Add new K-Beauty brands and products
2. **Ingredient Database:** Expand the ingredient knowledge base
3. **Cultural Context:** Add more Korean beauty traditions and practices
4. **Search Enhancement:** Improve web search accuracy and results

## 📝 License

MIT License - Feel free to use and modify!

## 🌸 About K-Beauty

Korean Beauty (K-Beauty) has revolutionized the global skincare industry with:

- **Innovation:** Glass skin, essences, cushion compacts
- **Ingredients:** Snail mucin, ginseng, centella asiatica
- **Philosophy:** Prevention over treatment, gentle yet effective
- **Accessibility:** High-quality products at various price points

This MCP server brings the wisdom of K-Beauty to Claude, helping you make informed skincare decisions with both traditional knowledge and modern innovations.

---

**Happy K-Beauty exploring! 🌸✨**
