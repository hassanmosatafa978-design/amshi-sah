import json
import os

base = "data/hadith/source/collections"
out_dir = "data/hadith/ready"
os.makedirs(out_dir, exist_ok=True)

books_to_convert = {
    "adab": "الأدب المفرد",
    "bulugh": "بلوغ المرام",
    "darimi": "سنن الدارمي",
    "mishkat": "مشكاة المصابيح",
    "riyadussalihin": "رياض الصالحين",
    "shamail": "الشمائل المحمدية",
}

for key, arabic_title in books_to_convert.items():
    source_path = os.path.join(base, key + ".json")

    with open(source_path, encoding="utf-8") as f:
        data = json.load(f)

    records = []
    books = data.get("books", [])

    for book in books:
        if not isinstance(book, dict):
            continue

        book_name = book.get("name_ar") or book.get("name_en") or arabic_title

        chapters = book.get("chapters", [])
        chapter_names = {}
        if isinstance(chapters, list):
            for chapter in chapters:
                if isinstance(chapter, dict):
                    chapter_names[str(chapter.get("chapter_number", ""))] = (
                        chapter.get("name_ar") or chapter.get("name_en") or ""
                    )

        hadiths = book.get("hadiths", [])
        if not isinstance(hadiths, list):
            continue

        for h in hadiths:
            if not isinstance(h, dict):
                continue

            text = (
                h.get("text_ar")
                or h.get("matn_ar")
                or ""
            ).strip()

            if not text:
                parts = [
                    h.get("isnad_ar", ""),
                    h.get("matn_ar", ""),
                    h.get("closing_ar", ""),
                ]
                text = " ".join(p.strip() for p in parts if isinstance(p, str) and p.strip())

            if not text:
                continue

            number = str(
                h.get("hadith_number")
                or h.get("reference")
                or len(records) + 1
            )

            chapter_number = str(h.get("chapter_number", ""))
            chapter_name = chapter_names.get(chapter_number, "")

            records.append({
                "title": f"{arabic_title} — حديث {number}",
                "text": text,
                "source": str(h.get("source_reference") or h.get("reference") or f"{key} {number}"),
                "number": number,
                "book": key,
                "book_name": book_name,
                "chapter": chapter_name,
                "category": "all"
            })

    output_path = os.path.join(out_dir, key + ".json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, separators=(",", ":"))

    print(f"{arabic_title}: تم تحويل {len(records)} حديثًا")

print("\nانتهى التحويل.")
