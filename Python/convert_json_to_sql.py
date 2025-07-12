import json
import uuid

with open("./translation.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("insert_translations_lang4.sql", "w", encoding="utf-8") as f:
    for key, value in data.items():
        id = str(uuid.uuid4())
        key = key.replace("'", "''")
        value = value.replace("'", "''")
        f.write(f"INSERT INTO tblshopresourcetext (Id, ResourceKey, Value, LanguageId) VALUES ('{id}', '{key}', '{value}', '4');\n")
