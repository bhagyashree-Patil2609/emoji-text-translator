import unicodedata
from frontend import create_app

# ---------------------------
# Build Emoji Dictionary
# ---------------------------
emoji_dict = {}

for i in range(0x1F300, 0x1FAFF):
    try:
        char = chr(i)
        name = unicodedata.name(char)
        emoji_dict[name.lower()] = char
    except:
        continue


# ---------------------------
# Emoji ➝ Name
# ---------------------------
def emoji_to_name(text):
    result = []
    for char in text:
        try:
            name = unicodedata.name(char).title()
            result.append(f"{char} → {name}")
        except:
            continue

    return "\n".join(result) if result else "No valid emoji found"


# ---------------------------
# Name ➝ Emoji
# ---------------------------
def name_to_emoji(text):
    text = text.lower().strip()

    country_dict = {
        "india": "IN",
        "usa": "US",
        "japan": "JP",
        "china": "CN",
        "germany": "DE",
        "france": "FR",
        "uk": "GB"
    }

    # Country name
    if text in country_dict:
        code = country_dict[text]
        return chr(127397 + ord(code[0])) + chr(127397 + ord(code[1]))

    # Country code
    if len(text) == 2 and text.isalpha():
        code = text.upper()
        return chr(127397 + ord(code[0])) + chr(127397 + ord(code[1]))

    # Normal emoji search
    results = []
    for name, emoji in emoji_dict.items():
        if text in name:
            results.append(f"{emoji} ({name.title()})")

    return "\n".join(results[:10]) if results else "No matching emoji found"


# ---------------------------
# Create & Launch App
# ---------------------------
app = create_app(emoji_to_name, name_to_emoji)

if __name__ == "__main__":
    app.launch()
