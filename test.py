from fontTools.ttLib import TTFont

font = TTFont("TajawalFixed-Regular.ttf")
name_table = font['name']

for name_record in name_table.names:
    name_id = name_record.nameID
    platform_id = name_record.platformID
    plat_enc_id = name_record.platEncID
    lang_id = name_record.langID
    name_string = name_record.string.decode(name_record.getEncoding()) # Correct decoding

    print(f"Name ID: {name_id}")
    print(f"Platform ID: {platform_id}")
    print(f"Platform Encoding ID: {plat_enc_id}")
    print(f"Language ID: {lang_id}")
    print(f"Name String: {name_string}")  # Print the actual name string
    print("-" * 20)