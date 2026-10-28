import json
from pathlib import Path

base = Path("data/adhkar")

ayat = (
    "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ "
    "لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ لَهُ مَا فِي "
    "السَّمَاوَاتِ وَمَا فِي الْأَرْضِ مَنْ ذَا الَّذِي "
    "يَشْفَعُ عِنْدَهُ إِلَّا بِإِذْنِهِ يَعْلَمُ مَا "
    "بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ "
    "بِشَيْءٍ مِنْ عِلْمِهِ إِلَّا بِمَا شَاءَ وَسِعَ "
    "كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ وَلَا يَئُودُهُ "
    "حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ"
)

extras = [
    {
        "text": ayat,
        "count": 1,
        "source": "القرآن الكريم، البقرة: 255",
        "grade": "آية قرآنية"
    },
    {
        "text": "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العليم.",
        "count": 3,
        "source": "سنن أبي داود 5088",
        "grade": "يحتاج مراجعة التخريج"
    },
    {
        "text": "رضيت بالله ربًا، وبالإسلام دينًا، وبمحمد ﷺ نبيًا.",
        "count": 3,
        "source": "سنن أبي داود 5072",
        "grade": "يحتاج مراجعة التخريج"
    },
    {
        "text": "اللهم إني أسألك العفو والعافية في الدنيا والآخرة.",
        "count": 1,
        "source": "دعاء وارد في السنة؛ يلزم استكمال النص وتوثيقه قبل اعتماده",
        "grade": "نص مختصر"
    }
]

for name in ("morning", "evening"):
    path = base / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    texts = {x["text"] for x in data["items"]}
    next_id = max(x["id"] for x in data["items"]) + 1

    for extra in extras:
        if extra["text"] not in texts:
            item = dict(extra)
            item["id"] = next_id
            data["items"].append(item)
            texts.add(item["text"])
            next_id += 1

    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(data["title"], len(data["items"]), "أذكار")
