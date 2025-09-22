# 🌸 K-Beauty MCP Server

AI-powered Korean Beauty and Skincare Assistant using Model Context Protocol (MCP)

## ✨ Features

### 📸 **NEW! AI Photo Skin Analysis**
- **Comprehensive skin scanning** using Claude's advanced image analysis
- **8-category analysis**: skin tone, pigmentation, acne, pores, blackheads, texture, aging signs, and special areas
- **Personalized K-Beauty solutions** with step-by-step care plans
- **Professional-grade recommendations** for products and treatments

### 🎯 **Core Tools**
1. **`analyze_skin_from_photo`** - AI-powered comprehensive skin analysis from photos
2. **`search_kbeauty_brands`** - Search and get detailed K-Beauty brand information
3. **`recommend_routine`** - Personalized skincare routine recommendations
4. **`analyze_ingredients`** - Scientific analysis of skincare ingredients
5. **`product_comparison`** - Compare multiple K-Beauty products
6. **`kbeauty_trends`** - Latest K-Beauty trends and market analysis
7. **`seasonal_skincare_guide`** - Season-specific skincare recommendations
8. **`dupes_finder`** - Find affordable alternatives for expensive products
9. **`skin_concern_matcher`** - Match skin concerns with effective solutions

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Claude Desktop App
- MCP library (`pip install mcp`)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AlexAI-MCP/K-Beauty-MCP.git
cd K-Beauty-MCP
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Claude Desktop**
Add to your Claude Desktop configuration file:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "k-beauty": {
      "command": "python",
      "args": [
        "/path/to/K-Beauty-MCP/server.py"
      ],
      "env": {
        "PYTHONPATH": "/path/to/K-Beauty-MCP"
      }
    }
  }
}
```

4. **Restart Claude Desktop**

## 💡 Usage Examples

### 📸 Photo Skin Analysis
```
Upload your skin photo and ask:
"analyze_skin_from_photo 도구로 피부 분석해줘"
```

### 🌸 Brand Search
```
search_kbeauty_brands: {"brand_name": "The Ordinary"}
```

### 💄 Routine Recommendation
```
recommend_routine: {
  "skin_type": "combination", 
  "skin_concerns": ["acne", "dark spots"],
  "budget": "mid-range"
}
```

### 🧪 Ingredient Analysis
```
analyze_ingredients: {
  "ingredients": ["niacinamide", "hyaluronic acid", "retinol"],
  "skin_type": "sensitive"
}
```

## 📸 Photo Analysis Features

### 🔍 **Comprehensive Skin Scanning**
- **Skin Tone Analysis**: Cool/warm/neutral tone detection + makeup recommendations
- **Pigmentation Analysis**: Age spots, acne marks, melasma detection
- **Acne/Blemish Analysis**: Active acne classification and severity assessment
- **Pore Analysis**: Size, distribution, and clogging evaluation
- **Blackhead/Whitehead Detection**: Location and removal priority
- **Texture Analysis**: Roughness, dead skin cells, skin smoothness
- **Aging Signs**: Fine lines, wrinkles, elasticity assessment
- **Special Areas**: Dark circles, puffiness, sensitivity indicators

### 🎯 **Personalized Solutions**
- **Immediate Solutions**: Priority issues + quick-fix products
- **Step-by-step Care Plans**: 1 week / 1 month / 3 month roadmaps
- **K-Beauty Product Recommendations**: Korean brand focus + budget options
- **Professional Care Guidance**: Dermatology and aesthetic recommendations

## 🛠️ Technical Details

### Architecture
- **MCP Protocol**: Compatible with MCP 1.9.0+
- **Transport**: stdio (standard input/output)
- **Image Analysis**: Leverages Claude's advanced vision capabilities
- **Web Search Integration**: Real-time K-Beauty information retrieval

### File Structure
```
K-Beauty-MCP/
├── server.py                      # Main server with photo analysis
├── requirements.txt                # Python dependencies
├── README.md                      # This file
├── PHOTO_ANALYSIS_GUIDE.md        # Detailed photo analysis guide
└── .gitignore                     # Git ignore rules
```

## 🌟 Key Benefits

✅ **Real-time Information**: Always up-to-date K-Beauty trends and products
✅ **AI-Powered Analysis**: Professional-grade skin assessment from photos
✅ **Personalized Recommendations**: Tailored to individual skin types and concerns
✅ **Budget-Conscious**: Options for all price ranges
✅ **Korean Beauty Focus**: Specialized in K-Beauty products and techniques
✅ **Step-by-step Guidance**: Clear, actionable skincare routines

## 🔄 Web Search Integration

The server uses Claude's web search capabilities to provide:
- Latest product information and prices
- Real-time reviews and ratings
- Current K-Beauty trends and innovations
- Updated ingredient research and findings
- Authentic purchase locations and retailers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Open an issue on GitHub
- Check the [Photo Analysis Guide](PHOTO_ANALYSIS_GUIDE.md) for detailed usage instructions

---

**Made with 💝 for K-Beauty enthusiasts worldwide**
