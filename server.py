#!/usr/bin/env python3
"""
K-Beauty MCP Server - Complete Version with Advanced Skin Analysis
Korean Beauty and Skincare Assistant with AI-Powered Photo Analysis
"""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.models import InitializationOptions, ServerCapabilities
from mcp.types import Tool, TextContent, ToolsCapability, ImageContent
from typing import Any, Dict, List

# Create server instance
server = Server("k-beauty-complete")

@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available K-Beauty tools"""
    return [
        Tool(
            name="analyze_skin_from_photo",
            description="Comprehensive AI-powered skin analysis from photo using Claude's vision capabilities. Analyzes skin tone, pigmentation, acne, blackheads, pores, texture, and provides personalized K-Beauty solutions",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_description": {
                        "type": "string",
                        "description": "User should upload an image and Claude will analyze it. This field is for any additional context about the photo (lighting conditions, skin concerns to focus on, etc.)"
                    },
                    "analysis_focus": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["skin_tone", "pigmentation", "acne", "blackheads", "pores", "texture", "wrinkles", "dark_circles", "overall_condition"]
                        },
                        "description": "Specific aspects to focus on during analysis"
                    },
                    "user_age": {
                        "type": "number",
                        "description": "User's age for age-appropriate recommendations"
                    },
                    "skin_type_self_assessment": {
                        "type": "string",
                        "enum": ["oily", "dry", "combination", "sensitive", "normal", "unknown"],
                        "description": "User's own assessment of their skin type"
                    }
                },
                "required": ["image_description"]
            }
        ),
        Tool(
            name="search_kbeauty_brands",
            description="Search for K-Beauty brands and get comprehensive brand information",
            inputSchema={
                "type": "object",
                "properties": {
                    "brand_name": {
                        "type": "string",
                        "description": "The K-Beauty brand name to search for"
                    }
                },
                "required": ["brand_name"]
            }
        ),
        Tool(
            name="recommend_routine",
            description="Get personalized K-Beauty skincare routine recommendations",
            inputSchema={
                "type": "object",
                "properties": {
                    "skin_type": {
                        "type": "string",
                        "enum": ["oily", "dry", "combination", "sensitive", "normal"],
                        "description": "Primary skin type"
                    },
                    "skin_concerns": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of skin concerns"
                    },
                    "budget": {
                        "type": "string",
                        "enum": ["budget", "mid-range", "luxury", "mixed"],
                        "description": "Budget preference"
                    }
                },
                "required": ["skin_type"]
            }
        ),
        Tool(
            name="analyze_ingredients",
            description="Analyze skincare ingredients and their benefits",
            inputSchema={
                "type": "object",
                "properties": {
                    "ingredients": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of ingredients to analyze"
                    },
                    "skin_type": {
                        "type": "string",
                        "enum": ["oily", "dry", "combination", "sensitive", "normal"],
                        "description": "Skin type for compatibility assessment"
                    }
                },
                "required": ["ingredients"]
            }
        ),
        Tool(
            name="product_comparison",
            description="Compare K-Beauty products",
            inputSchema={
                "type": "object",
                "properties": {
                    "products": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of products to compare"
                    },
                    "comparison_criteria": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Criteria for comparison (price, ingredients, effectiveness, etc.)"
                    }
                },
                "required": ["products"]
            }
        ),
        Tool(
            name="kbeauty_trends",
            description="Analyze current K-Beauty trends",
            inputSchema={
                "type": "object",
                "properties": {
                    "trend_type": {
                        "type": "string",
                        "enum": ["ingredients", "brands", "products", "techniques"],
                        "description": "Type of trend analysis"
                    },
                    "time_period": {
                        "type": "string",
                        "enum": ["current", "2024", "2025", "emerging"],
                        "description": "Time period for trend analysis"
                    }
                },
                "required": ["trend_type"]
            }
        ),
        Tool(
            name="seasonal_skincare_guide",
            description="Get season-specific K-Beauty recommendations",
            inputSchema={
                "type": "object",
                "properties": {
                    "season": {
                        "type": "string",
                        "enum": ["spring", "summer", "fall", "winter"],
                        "description": "Current season"
                    },
                    "climate": {
                        "type": "string",
                        "enum": ["humid", "dry", "temperate", "tropical"],
                        "description": "Local climate type"
                    },
                    "skin_type": {
                        "type": "string",
                        "enum": ["oily", "dry", "combination", "sensitive", "normal"],
                        "description": "Skin type"
                    }
                },
                "required": ["season", "skin_type"]
            }
        ),
        Tool(
            name="dupes_finder",
            description="Find affordable alternatives for expensive K-Beauty products",
            inputSchema={
                "type": "object",
                "properties": {
                    "target_product": {
                        "type": "string",
                        "description": "Expensive product to find dupes for"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Maximum price for dupe products"
                    }
                },
                "required": ["target_product"]
            }
        ),
        Tool(
            name="skin_concern_matcher",
            description="Match specific skin concerns with effective K-Beauty ingredients and products",
            inputSchema={
                "type": "object",
                "properties": {
                    "concerns": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of specific skin concerns"
                    },
                    "severity": {
                        "type": "string",
                        "enum": ["mild", "moderate", "severe"],
                        "description": "Severity level of concerns"
                    }
                },
                "required": ["concerns"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls"""
    
    if name == "analyze_skin_from_photo":
        image_description = arguments.get("image_description", "")
        analysis_focus = arguments.get("analysis_focus", ["overall_condition"])
        user_age = arguments.get("user_age")
        skin_type_self = arguments.get("skin_type_self_assessment", "unknown")
        
        analysis_request = f"""
📸 **Claude 이미지 분석 요청: 종합적인 피부 스캔**

{f"사용자 설명: {image_description}" if image_description else ""}
{f"나이: {user_age}세" if user_age else ""}
{f"자가 진단 피부 타입: {skin_type_self}" if skin_type_self != "unknown" else ""}
분석 포커스: {', '.join(analysis_focus)}

**업로드된 피부 사진을 다음 기준으로 상세히 분석해 주세요:**

## 🔍 **세부 피부 스캔 항목**

### 1. 피부톤 분석
- 피부 톤 (쿨톤/웜톤/뉴트럴)
- 피부 밝기 레벨
- 색조 균일성
- 추천 파운데이션/컨실러 색상

### 2. 색소침착 분석  
- 기미, 주근깨, 검버섯 위치와 정도
- 여드름 자국 (PIH/PIE)
- 멜라스마 여부
- 전체적인 색소 불균형 정도

### 3. 여드름/뾰루지 분석
- 활성 여드름 개수와 위치
- 여드름 타입 (화이트헤드/블랙헤드/염증성)
- 심각도 평가 (경미/중등도/심각)
- 여드름 흉터 유무

### 4. 모공 상태 분석
- 모공 크기 (작음/보통/큼)
- 모공 막힘 정도
- 모공이 두드러진 부위 (T존, 볼 등)
- 모공 모양과 상태

### 5. 블랙헤드/화이트헤드 분석
- 코, 턱, 이마 블랙헤드 분포
- 화이트헤드 위치와 개수
- 피지 플러그 상태
- 제거 필요 정도

### 6. 피부 질감 분석
- 매끄러움 vs 거칠기
- 각질 상태
- 피부 결 균일성
- 표면 텍스처 품질

### 7. 노화 징후 분석
- 잔주름 위치와 깊이
- 표정 주름 vs 나이 주름
- 탄력 저하 정도
- 처짐 여부

### 8. 기타 특이사항
- 다크서클 정도
- 눈가 부종
- 피부 건조/유분 상태
- 민감성 징후 (홍조, 자극)

## 🎯 **맞춤형 K-Beauty 솔루션 제공**

분석 결과를 바탕으로 다음 정보를 제공해 주세요:

### 즉시 개선 솔루션
- 가장 시급한 피부 문제 3가지
- 각 문제별 추천 성분
- 단기간 효과를 볼 수 있는 제품

### 단계별 케어 플랜
- 1주차: 즉시 시작할 기본 케어
- 1개월: 중점 관리 목표
- 3개월: 장기 개선 계획

### 제품 추천 (한국 브랜드 우선)
- 클렌저 추천
- 토너/에센스 추천  
- 세럼/앰플 추천
- 모이스처라이저 추천
- 선크림 추천
- 특별 관리 제품 (마스크, 필링 등)

### 피해야 할 것들
- 현재 피부 상태에 해로운 성분
- 피해야 할 제품 타입
- 잘못된 케어 습관

### 전문 케어 추천
- 피부과 시술 필요 여부
- 에스테틱 관리 추천
- 홈 케어 기기 활용법

이 모든 분석을 통해 사용자만의 **개인 맞춤형 K-Beauty 로드맵**을 제시해 주세요!
"""
        return [TextContent(type="text", text=analysis_request)]
    
    elif name == "search_kbeauty_brands":
        brand_name = arguments.get("brand_name", "")
        search_request = f"""
🔍 **웹 검색 요청: K-Beauty 브랜드 정보**

브랜드: **{brand_name}**

다음 정보를 웹에서 검색해 주세요:
1. 브랜드 히스토리와 배경
2. 인기 제품과 베스트셀러
3. 핵심 성분 및 특징
4. 가격대와 타겟 고객
5. 최근 리뷰와 평판
6. 정품 구매처

이 브랜드에 대한 포괄적이고 최신 정보를 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "recommend_routine":
        skin_type = arguments.get("skin_type")
        skin_concerns = arguments.get("skin_concerns", [])
        budget = arguments.get("budget", "mixed")
        
        result = f"## 🌸 개인 맞춤형 K-Beauty 스킨케어 루틴\n\n"
        result += f"**피부 타입:** {skin_type.title()}\n"
        if skin_concerns:
            result += f"**피부 고민:** {', '.join(skin_concerns)}\n"
        result += f"**예산:** {budget.title()}\n\n"
        
        # 피부 타입별 맞춤 루틴
        result += f"### 🌅 아침 루틴 ({skin_type} 피부용)\n"
        if skin_type == "oily":
            result += f"1. 저pH 젤 클렌저\n2. BHA 토너 (주 2-3회)\n3. 나이아신아마이드 세럼\n4. 가벼운 젤 모이스처라이저\n5. 논코메도제닉 선크림 SPF 50+\n\n"
        elif skin_type == "dry":
            result += f"1. 크림 타입 클렌저\n2. 히알루론산 토너\n3. 비타민 C 세럼\n4. 세라마이드 크림\n5. 보습 선크림 SPF 30+\n\n"
        else:
            result += f"1. 순한 클렌저\n2. 토너/에센스\n3. 비타민 C 세럼\n4. 보습 크림\n5. 선크림 SPF 30+\n\n"
        
        result += f"### 🌙 저녁 루틴\n"
        result += f"1. 오일 클렌저 (더블 클렌징)\n2. 워터 베이스 클렌저\n3. 토너\n4. 트리트먼트 세럼\n5. 아이크림\n6. 나이트 크림\n7. 슬리핑 마스크 (주 2-3회)\n\n"
        
        result += f"🔍 **'{budget}' 예산에 맞는 구체적인 제품 추천을 원하시면 웹 검색을 통해 최신 정보를 찾아드릴 수 있습니다.**"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "analyze_ingredients":
        ingredients = arguments.get("ingredients", [])
        skin_type = arguments.get("skin_type")
        
        search_request = f"""
🔍 **웹 검색 요청: 스킨케어 성분 분석**

분석할 성분들: **{', '.join(ingredients)}**
피부 타입: **{skin_type if skin_type else '모든 피부 타입'}**

다음 정보를 웹에서 검색해 주세요:
1. 각 성분의 효능과 효과
2. 권장 농도 및 사용법
3. 부작용이나 주의사항
4. 다른 성분과의 호환성
5. {skin_type} 피부에 적합성
6. 이 성분들이 포함된 추천 제품
7. 과학적 연구 결과 및 임상 데이터

이 성분들에 대한 상세하고 신뢰할 수 있는 정보를 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "product_comparison":
        products = arguments.get("products", [])
        comparison_criteria = arguments.get("comparison_criteria", ["price", "ingredients", "effectiveness"])
        
        search_request = f"""
🔍 **웹 검색 요청: K-Beauty 제품 비교**

비교할 제품들: **{', '.join(products)}**
비교 기준: **{', '.join(comparison_criteria)}**

각 제품에 대해 다음 정보를 웹에서 검색해 주세요:
1. 현재 가격과 구매처
2. 전성분 리스트 및 핵심 성분
3. 사용자 리뷰와 평점
4. 전문가 의견 및 피부과 의사 추천
5. 장점과 단점
6. 효과 지속 시간
7. 대체 제품 추천

비교표 형태로 상세한 분석을 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "kbeauty_trends":
        trend_type = arguments.get("trend_type")
        time_period = arguments.get("time_period", "current")
        
        search_request = f"""
🔍 **웹 검색 요청: K-Beauty 트렌드 분석**

트렌드 타입: **{trend_type}**
시기: **{time_period}**

다음 정보를 웹에서 검색해 주세요:
1. 최신 K-Beauty 혁신과 신제품 런칭
2. 트렌드 성분과 신기술
3. 인기 급상승 브랜드와 신흥 업체
4. 소셜미디어 뷰티 트렌드 (TikTok, Instagram)
5. 업계 보고서와 시장 분석
6. 계절별 트렌드와 2025년 예측
7. 글로벌 vs 한국 내수 트렌드 차이

현재의 포괄적인 트렌드 분석을 구체적 예시와 함께 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "seasonal_skincare_guide":
        season = arguments.get("season")
        climate = arguments.get("climate", "temperate")
        skin_type = arguments.get("skin_type")
        
        search_request = f"""
🔍 **웹 검색 요청: 계절별 K-Beauty 스킨케어 가이드**

계절: **{season}**
기후: **{climate}**
피부 타입: **{skin_type}**

다음 정보를 웹에서 검색해 주세요:
1. {season} 계절 피부 관리 포인트
2. {climate} 기후에 적합한 제품 타입
3. {skin_type} 피부의 계절별 변화
4. 추천 K-Beauty 제품 및 브랜드
5. 피해야 할 성분과 루틴
6. 전문가 추천 계절 케어 팁

계절과 기후, 피부 타입을 모두 고려한 맞춤형 가이드를 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "dupes_finder":
        target_product = arguments.get("target_product", "")
        max_price = arguments.get("max_price")
        
        search_request = f"""
🔍 **웹 검색 요청: K-Beauty 제품 대체재 찾기**

타겟 제품: **{target_product}**
최대 예산: **${max_price if max_price else '제한 없음'}**

다음 정보를 웹에서 검색해 주세요:
1. 타겟 제품의 핵심 성분 분석
2. 유사한 성분의 저가 대체재
3. 드럭스토어 K-Beauty 대안
4. Reddit, 뷰티 블로거 추천 듀프
5. 성분 대비 가격 효율성
6. 사용자 후기 비교
7. 구매 가능한 온라인 쇼핑몰

상세한 듀프 추천과 가격, 구매처 정보를 제공해 주세요.
"""
        return [TextContent(type="text", text=search_request)]
    
    elif name == "skin_concern_matcher":
        concerns = arguments.get("concerns", [])
        severity = arguments.get("severity", "moderate")
        
        # 기본 추천 제공
        result = f"## 🎯 피부 고민별 K-Beauty 솔루션\n\n"
        result += f"**고민:** {', '.join(concerns)}\n"
        result += f"**심각도:** {severity}\n\n"
        
        # 고민별 기본 가이드라인
        concern_mapping = {
            "acne": {
                "ingredients": ["살리실산 (BHA)", "나이아신아마이드", "센텔라 아시아티카", "티트리"],
                "avoid": "과도한 유분, 코메도제닉 성분",
                "routine": "더블 클렌징 → BHA 토너 → 나이아신아마이드 세럼 → 가벼운 보습"
            },
            "aging": {
                "ingredients": ["레티놀", "비타민 C", "펩타이드", "히알루론산"],
                "avoid": "과도한 스크럽, 알코올 기반 토너",
                "routine": "세안 → 비타민 C (아침) → 레티놀 (저녁) → 충분한 보습"
            },
            "pigmentation": {
                "ingredients": ["비타민 C", "나이아신아마이드", "알부틴", "kojic acid"],
                "avoid": "자극적인 필링, 향료",
                "routine": "세안 → 브라이트닝 세럼 → 보습 → 선크림 필수"
            },
            "dryness": {
                "ingredients": ["히알루론산", "세라마이드", "스쿠알란", "글리세린"],
                "avoid": "알코올 기반 제품, 과도한 세안",
                "routine": "순한 세안 → 히알루론산 → 오일/크림 → 슬리핑 마스크"
            },
            "sensitivity": {
                "ingredients": ["센텔라 아시아티카", "판테놀", "알로에", "무향료 포뮬라"],
                "avoid": "향료, 알코올, 강한 액티브 성분",
                "routine": "극순한 세안 → 진정 토너 → 배리어 강화 크림 → 물리적 선크림"
            }
        }
        
        for concern in concerns:
            concern_lower = concern.lower()
            for key, info in concern_mapping.items():
                if key in concern_lower or concern_lower in key:
                    result += f"### {concern.title()} 솔루션:\n\n"
                    result += f"**추천 성분:** {', '.join(info['ingredients'])}\n"
                    result += f"**피해야 할 것:** {info['avoid']}\n"
                    result += f"**기본 루틴:** {info['routine']}\n\n"
                    break
        
        # 웹 검색 요청도 추가
        search_request = f"""

🔍 **추가 웹 검색 요청: 피부 고민 맞춤 솔루션**

피부 고민: **{', '.join(concerns)}**
심각도: **{severity}**

다음 정보를 웹에서 검색해 주세요:
1. 각 고민에 효과적인 최신 K-Beauty 제품
2. 피부과 의사 추천 성분과 농도
3. 고민별 단계적 관리 방법
4. 실제 사용자 전후 사진과 후기
5. 브랜드별 특화 제품 라인
6. 예산대별 제품 추천
7. 주의사항과 사용 순서

구체적인 제품명과 사용법을 포함한 상세 가이드를 제공해 주세요.
"""
        result += search_request
        
        return [TextContent(type="text", text=result)]
    
    else:
        return [TextContent(type="text", text=f"알 수 없는 도구: {name}")]

async def main():
    """Main function"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="k-beauty-complete",
                server_version="3.0.0",
                capabilities=ServerCapabilities(
                    tools=ToolsCapability()
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
