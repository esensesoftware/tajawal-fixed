from fontTools.ttLib import TTFont

weights = ["Black", "Bold", "ExtraBold", "ExtraLight", "Light", "Medium", "Regular"]

# font = TTFont("Tajawal-Regular.ttf")
# name_table = font['name']

# for name_record in name_table.names:
#     name_id = name_record.nameID
#     platform_id = name_record.platformID
#     plat_enc_id = name_record.platEncID
#     lang_id = name_record.langID
#     name_string = name_record.string.decode(name_record.getEncoding()) # Correct decoding

#     print(f"Name ID: {name_id}")
#     print(f"Platform ID: {platform_id}")
#     print(f"Platform Encoding ID: {plat_enc_id}")
#     print(f"Language ID: {lang_id}")
#     print(f"Name String: {name_string}")  # Print the actual name string
#     print("-" * 20)

for weight in weights:
    font = TTFont(f"Tajawal-{weight}.ttf")
    font['name'].setName("Tajawal Fixed", 1, 1, 0, 0)  # Example: Change font family name
    font['name'].setName(f"1.000;1bou;TajawalFixed-{weight}", 3, 1, 0, 0)  # Example: Change font family name
    font['name'].setName("Tajawal Fixed", 4, 1, 0, 0)  # Example: Change font family name
    font['name'].setName(f"TajawalFixed-{weight}", 6, 1, 0, 0)  # Example: Change font family name
    font['name'].setName("Tajawal Fixed", 16, 1, 0, 0)  # Example: Change font family name
    font['name'].setName("Tajawal Fixed", 1, 3, 1, 1033)  # Example: Change font family name
    font['name'].setName(f"1.000;1bou;TajawalFixed-{weight}", 3, 3, 1, 1033)  # Example: Change font family name
    font['name'].setName("Tajawal Fixed", 4, 3, 1, 1033)  # Example: Change font family name
    font['name'].setName(f"TajawalFixed-{weight}", 6, 3, 1, 1033)  # Example: Change font family name
    font['name'].setName("Tajawal Fixed", 16, 3, 1, 1033)  # Example: Change font family name
    font.save(f"TajawalFixed-{weight}.ttf")
    