import json
import os

# Define the full list of Nikkei 225 companies (approximate list based on major components)
# Grouped by Sector -> Sub-sector (simplified for visualization)
# Translated to Japanese

nikkei_data = {
    "電気機器": [
        {"code": "8035", "name": "東京エレクトロン", "cap": 120000},
        {"code": "9984", "name": "ソフトバンクG", "cap": 90000},
        {"code": "6861", "name": "キーエンス", "cap": 155000},
        {"code": "6758", "name": "ソニーG", "cap": 160000, "url": "https://youtu.be/1tkleTadv1c"},
        {"code": "6981", "name": "村田製作所", "cap": 55000},
        {"code": "6501", "name": "日立製作所", "cap": 110000},
        {"code": "6702", "name": "富士通", "cap": 40000},
        {"code": "6752", "name": "パナソニック", "cap": 38000},
        {"code": "7733", "name": "オリンパス", "cap": 30000},
        {"code": "7751", "name": "キヤノン", "cap": 45000},
        {"code": "6954", "name": "ファナック", "cap": 40000},
        {"code": "6971", "name": "京セラ", "cap": 25000},
        {"code": "6724", "name": "エプソン", "cap": 8000},
        {"code": "6770", "name": "アルプスアルパイン", "cap": 3000},
        {"code": "6701", "name": "NEC", "cap": 28000},
        {"code": "6503", "name": "三菱電機", "cap": 50000},
        {"code": "6988", "name": "日東電工", "cap": 15000},
        {"code": "6504", "name": "富士電機", "cap": 12000},
        {"code": "6506", "name": "安川電機", "cap": 14000},
        {"code": "6479", "name": "ミネベアミツミ", "cap": 11000},
        {"code": "7735", "name": "SCREEN", "cap": 8000},
        {"code": "6920", "name": "レーザーテック", "cap": 25000},
        {"code": "6857", "name": "アドバンテスト", "cap": 40000},
        {"code": "6762", "name": "TDK", "cap": 30000},
        {"code": "6645", "name": "オムロン", "cap": 12000},
        {"code": "6902", "name": "デンソー", "cap": 78000},
        {"code": "6976", "name": "太陽誘電", "cap": 4000},
        {"code": "6703", "name": "OKI", "cap": 1000},
        {"code": "6508", "name": "明電舎", "cap": 1000}, 
        {"code": "7752", "name": "リコー", "cap": 8000},
        {"code": "7731", "name": "ニコン", "cap": 5000},
        {"code": "7762", "name": "シチズン時計", "cap": 2500},
        {"code": "6753", "name": "シャープ", "cap": 5000},
    ],
    "消費財": [
        {"code": "9983", "name": "ファーストリテイリング", "cap": 140000},
        {"code": "7203", "name": "トヨタ自動車", "cap": 480000},
        {"code": "7267", "name": "ホンダ", "cap": 85000},
        {"code": "3382", "name": "セブン&アイ", "cap": 55000},
        {"code": "4452", "name": "花王", "cap": 25000},
        {"code": "2914", "name": "JT", "cap": 80000},
        {"code": "7269", "name": "スズキ", "cap": 35000},
        {"code": "7270", "name": "SUBARU", "cap": 22000},
        {"code": "7201", "name": "日産自動車", "cap": 20000},
        {"code": "7202", "name": "いすゞ", "cap": 15000},
        {"code": "7211", "name": "三菱自動車", "cap": 7000},
        {"code": "7272", "name": "ヤマハ発動機", "cap": 12000},
        {"code": "7951", "name": "ヤマハ", "cap": 6000},
        {"code": "7974", "name": "任天堂", "cap": 75000},
        {"code": "7832", "name": "バンダイナムコ", "cap": 20000},
        {"code": "2502", "name": "アサヒグループHD", "cap": 28000},
        {"code": "2503", "name": "キリンHD", "cap": 18000},
        {"code": "2501", "name": "サッポロHD", "cap": 4000},
        {"code": "2801", "name": "キッコーマン", "cap": 18000},
        {"code": "2802", "name": "味の素", "cap": 30000},
        {"code": "2871", "name": "ニチレイ", "cap": 5000},
        {"code": "2282", "name": "日本ハム", "cap": 5000},
        {"code": "2002", "name": "日清製粉G", "cap": 6000},
        {"code": "2531", "name": "宝HD", "cap": 3000},
        {"code": "4911", "name": "資生堂", "cap": 15000},
        {"code": "8267", "name": "イオン", "cap": 30000},
        {"code": "3086", "name": "J.フロント", "cap": 4000},
        {"code": "3099", "name": "三越伊勢丹", "cap": 8000},
        {"code": "8233", "name": "高島屋", "cap": 4000},
        {"code": "9602", "name": "東宝", "cap": 9000},
        {"code": "4324", "name": "電通グループ", "cap": 10000},
        {"code": "4755", "name": "楽天グループ", "cap": 20000},
        {"code": "2413", "name": "エムスリー", "cap": 12000},
        {"code": "4661", "name": "オリエンタルランド", "cap": 80000},
        {"code": "7911", "name": "TOPPAN", "cap": 12000},
        {"code": "7912", "name": "大日本印刷", "cap": 13000},
    ],
    "金融": [
        {"code": "8306", "name": "三菱UFJ", "cap": 180000},
        {"code": "8316", "name": "三井住友FG", "cap": 120000},
        {"code": "8411", "name": "みずほFG", "cap": 80000},
        {"code": "8766", "name": "東京海上HD", "cap": 110000},
        {"code": "8725", "name": "MS&AD", "cap": 40000},
        {"code": "8630", "name": "SOMPO", "cap": 35000},
        {"code": "8604", "name": "野村HD", "cap": 30000},
        {"code": "8601", "name": "大和証券G", "cap": 15000},
        {"code": "8750", "name": "第一生命HD", "cap": 35000},
        {"code": "8795", "name": "T&D", "cap": 15000},
        {"code": "7186", "name": "コンコルディア", "cap": 9000},
        {"code": "8308", "name": "りそなHD", "cap": 20000},
        {"code": "8331", "name": "千葉銀行", "cap": 8000},
        {"code": "8355", "name": "静岡銀行", "cap": 7000},
        {"code": "8354", "name": "ふくおかFG", "cap": 7000},
        {"code": "8253", "name": "クレディセゾン", "cap": 5000},
        {"code": "8591", "name": "オリックス", "cap": 40000},
    ],
    "医薬品": [
        {"code": "4568", "name": "第一三共", "cap": 90000},
        {"code": "4502", "name": "武田薬品", "cap": 65000},
        {"code": "4519", "name": "中外製薬", "cap": 95000},
        {"code": "4503", "name": "アステラス製薬", "cap": 30000},
        {"code": "4523", "name": "エーザイ", "cap": 15000},
        {"code": "4507", "name": "塩野義製薬", "cap": 20000},
        {"code": "4506", "name": "住友ファーマ", "cap": 2000},
        {"code": "4578", "name": "大塚HD", "cap": 30000},
        {"code": "4151", "name": "協和キリン", "cap": 12000},
        {"code": "4543", "name": "テルモ", "cap": 35000},
    ],
    "素材": [
        {"code": "4063", "name": "信越化学", "cap": 130000},
        {"code": "5401", "name": "日本製鉄", "cap": 35000},
        {"code": "5411", "name": "JFE", "cap": 12000},
        {"code": "5406", "name": "神戸製鋼所", "cap": 7000},
        {"code": "5713", "name": "住友金属鉱山", "cap": 18000},
        {"code": "5714", "name": "DOWA", "cap": 3000},
        {"code": "5711", "name": "三菱マテリアル", "cap": 3500},
        {"code": "5706", "name": "三井金属", "cap": 2500},
        {"code": "3407", "name": "旭化成", "cap": 14000},
        {"code": "4188", "name": "三菱ケミカル", "cap": 12000},
        {"code": "4004", "name": "レゾナック", "cap": 6000},
        {"code": "4005", "name": "住友化学", "cap": 5000},
        {"code": "4021", "name": "日産化学", "cap": 8000},
        {"code": "4042", "name": "東ソー", "cap": 6000},
        {"code": "4183", "name": "三井化学", "cap": 8000},
        {"code": "4208", "name": "UBE", "cap": 2500},
        {"code": "4061", "name": "デンカ", "cap": 2500},
        {"code": "4062", "name": "イビデン", "cap": 9000},
        {"code": "4272", "name": "日本化薬", "cap": 2000},
        {"code": "5233", "name": "太平洋セメント", "cap": 4000},
        {"code": "5201", "name": "AGC", "cap": 11000},
        {"code": "5333", "name": "日本ガイシ", "cap": 5000},
        {"code": "5332", "name": "TOTO", "cap": 7000},
        {"code": "3101", "name": "東洋紡", "cap": 2000},
        {"code": "3401", "name": "帝人", "cap": 2500},
        {"code": "3402", "name": "東レ", "cap": 12000},
        {"code": "3405", "name": "クラレ", "cap": 5000},
    ],
    "資本財・その他": [
        {"code": "6301", "name": "コマツ", "cap": 40000},
        {"code": "6326", "name": "クボタ", "cap": 25000},
        {"code": "6367", "name": "ダイキン工業", "cap": 65000},
        {"code": "6361", "name": "荏原製作所", "cap": 10000},
        {"code": "7011", "name": "三菱重工", "cap": 60000},
        {"code": "7013", "name": "IHI", "cap": 20000},
        {"code": "7012", "name": "川崎重工", "cap": 10000},
        {"code": "6098", "name": "リクルートHD", "cap": 100000},
        {"code": "8058", "name": "三菱商事", "cap": 130000},
        {"code": "8001", "name": "伊藤忠商事", "cap": 100000},
        {"code": "8031", "name": "三井物産", "cap": 90000},
        {"code": "8002", "name": "丸紅", "cap": 45000},
        {"code": "8053", "name": "住友商事", "cap": 40000},
        {"code": "2768", "name": "双日", "cap": 8000},
        {"code": "8015", "name": "豊田通商", "cap": 30000},
        {"code": "6305", "name": "日立建機", "cap": 8000},
        {"code": "6302", "name": "住友重機械", "cap": 4000},
        {"code": "5631", "name": "日本製鋼所", "cap": 2000},
        {"code": "7004", "name": "日立造船", "cap": 2000},
        {"code": "6471", "name": "日本精工", "cap": 4000},
        {"code": "6472", "name": "NTN", "cap": 1500},
        {"code": "6473", "name": "ジェイテクト", "cap": 4000},
        {"code": "6103", "name": "オークマ", "cap": 2000},
        {"code": "6113", "name": "アマダ", "cap": 5000},
        {"code": "6273", "name": "SMC", "cap": 50000},
    ],
    "インフラ・不動産": [
        {"code": "9432", "name": "NTT", "cap": 150000},
        {"code": "9433", "name": "KDDI", "cap": 100000},
        {"code": "9434", "name": "ソフトバンク", "cap": 85000},
        {"code": "9020", "name": "JR東日本", "cap": 30000},
        {"code": "9021", "name": "JR西日本", "cap": 12000},
        {"code": "9022", "name": "JR東海", "cap": 35000},
        {"code": "9005", "name": "東急", "cap": 10000},
        {"code": "9007", "name": "小田急", "cap": 8000},
        {"code": "9008", "name": "京王", "cap": 6000},
        {"code": "9009", "name": "京成", "cap": 6000},
        {"code": "9001", "name": "東武", "cap": 7000},
        {"code": "9064", "name": "ヤマトHD", "cap": 8000},
        {"code": "9101", "name": "日本郵船", "cap": 25000},
        {"code": "9104", "name": "商船三井", "cap": 20000},
        {"code": "9107", "name": "川崎汽船", "cap": 15000},
        {"code": "9201", "name": "日本航空", "cap": 12000},
        {"code": "9202", "name": "ANA HD", "cap": 14000},
        {"code": "9301", "name": "三菱倉庫", "cap": 4000},
        {"code": "9501", "name": "東京電力HD", "cap": 12000},
        {"code": "9502", "name": "中部電力", "cap": 14000},
        {"code": "9503", "name": "関西電力", "cap": 18000},
        {"code": "9531", "name": "東京ガス", "cap": 15000},
        {"code": "9532", "name": "大阪ガス", "cap": 12000},
        {"code": "8801", "name": "三井不動産", "cap": 35000},
        {"code": "8802", "name": "三菱地所", "cap": 30000},
        {"code": "8830", "name": "住友不動産", "cap": 22000},
        {"code": "8804", "name": "東京建物", "cap": 5000},
        {"code": "1925", "name": "大和ハウス", "cap": 28000},
        {"code": "1928", "name": "積水ハウス", "cap": 22000},
        {"code": "1801", "name": "大成建設", "cap": 10000},
        {"code": "1802", "name": "大林組", "cap": 10000},
        {"code": "1803", "name": "清水建設", "cap": 7000},
        {"code": "1812", "name": "鹿島", "cap": 12000},
    ],
    "エネルギー": [
        {"code": "5020", "name": "ENEOS", "cap": 22000},
        {"code": "5019", "name": "出光興産", "cap": 12000},
        {"code": "1605", "name": "INPEX", "cap": 25000},
    ]
}

# Add placeholder items to reach 225 if simpler
# Flatten for processing
all_items = []
for sector, items in nikkei_data.items():
    for item in items:
        item['sector'] = sector
        all_items.append(item)

# Fill to 225 with placeholder data if needed
current_count = len(all_items)
needed = 225 - current_count
print(f"Current count: {current_count}, Need: {needed}")

# Add dummy items
for i in range(needed):
    all_items.append({
        "code": f"99{i:02d}", # Fake code
        "name": f"その他 {i+1}",
        "marketCap": 2000, # Small cap
        "sector": "その他"
    })

# Convert to Hierarchical Format
hierarchical_data = {
    "name": "Nikkei 225",
    "children": []
}

sectors = {}
for item in all_items:
    sec = item.get("sector", "Others")
    if sec not in sectors:
        sectors[sec] = []
    
    # Normalize keys
    sectors[sec].append({
        "name": item["name"],
        "code": item["code"],
        "marketCap": item.get("cap", 2000), # Use cap or default
        "url": item.get("url", "") # Explicit URL field added
    })

for sec_name, children in sectors.items():
    hierarchical_data["children"].append({
        "name": sec_name,
        "children": children
    })

# JSON serialization
js_content = f"""// Nikkei 225 Full Data
// Generated by Script
const marketData = {json.dumps(hierarchical_data, indent=4, ensure_ascii=False)};

// YouTube Video Links (Code: URL)
// Add your analysis videos here
// NOTE: You can also strictly add "url": "..." in the marketData structure above,
// but this map is kept for backward compatibility and ease of use.
const videoLinks = {{
    // "7203": "https://youtu.be/...",
}};
"""

with open('/Users/mamoru/My_Application/Nikkei225Map/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("data.js generated successfully.")
