import json, re
from pathlib import Path

base = Path("data/adhkar")
base.mkdir(parents=True, exist_ok=True)

sections = {
    "after-prayer": {
        "title": "أذكار بعد الصلاة",
        "items": [
            {"text":"أستغفر الله","count":3,"source":"صحيح مسلم، 591","grade":"صحيح"},
            {"text":"اللهم أنت السلام ومنك السلام تباركت يا ذا الجلال والإكرام.","count":1,"source":"صحيح مسلم، 591","grade":"صحيح"},
            {"text":"سبحان الله","count":33,"source":"صحيح مسلم، 595","grade":"صحيح"},
            {"text":"الحمد لله","count":33,"source":"صحيح مسلم، 595","grade":"صحيح"},
            {"text":"الله أكبر","count":33,"source":"صحيح مسلم، 595","grade":"صحيح"},
            {"text":"لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير.","count":1,"source":"صحيح مسلم، 595","grade":"صحيح"}
        ]
    },
    "sleep": {
        "title": "أذكار النوم",
        "items": [
            {"text":"باسمك اللهم أموت وأحيا.","count":1,"source":"صحيح البخاري، 6324","grade":"صحيح"},
            {"text":"باسمك ربي وضعت جنبي، وبك أرفعه، إن أمسكت نفسي فارحمها، وإن أرسلتها فاحفظها بما تحفظ به عبادك الصالحين.","count":1,"source":"صحيح البخاري، 6320؛ صحيح مسلم، 2714","grade":"صحيح"},
            {"text":"اللهم قني عذابك يوم تبعث عبادك.","count":3,"source":"سنن أبي داود، 5045","grade":"يُراجع تخريجه قبل الاعتماد النهائي"}
        ]
    },
    "waking": {
        "title": "أذكار الاستيقاظ",
        "items": [
            {"text":"الحمد لله الذي أحيانا بعدما أماتنا وإليه النشور.","count":1,"source":"صحيح البخاري، 6324","grade":"صحيح"}
        ]
    },
    "food": {
        "title": "أذكار الطعام والشراب",
        "items": [
            {"text":"بسم الله.","count":1,"source":"سنن أبي داود، 3767؛ جامع الترمذي، 1858","grade":"ورد في السنة"},
            {"text":"بسم الله أوله وآخره.","count":1,"source":"سنن أبي داود، 3767؛ جامع الترمذي، 1858","grade":"ورد عند نسيان التسمية في أول الطعام"}
        ]
    },
    "travel": {
        "title": "دعاء السفر",
        "items": [
            {"text":"اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ، وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ. اللَّهُمَّ إِنَّا نَسْأَلُكَ فِي سَفَرِنَا هَذَا الْبِرَّ وَالتَّقْوَى، وَمِنَ الْعَمَلِ مَا تَرْضَى. اللَّهُمَّ هَوِّنْ عَلَيْنَا سَفَرَنَا هَذَا وَاطْوِ عَنَّا بُعْدَهُ. اللَّهُمَّ أَنْتَ الصَّاحِبُ فِي السَّفَرِ، وَالْخَلِيفَةُ فِي الْأَهْلِ. اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ وَعْثَاءِ السَّفَرِ، وَكَآبَةِ الْمَنْظَرِ، وَسُوءِ الْمُنْقَلَبِ فِي الْمَالِ وَالْأَهْلِ.","count":1,"source":"صحيح مسلم، 1342","grade":"صحيح"}
        ]
    },
    "distress": {
        "title": "أدعية الكرب والهم",
        "items": [
            {"text":"لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ.","count":1,"source":"القرآن الكريم، الأنبياء: 87","grade":"آية قرآنية"},
            {"text":"حَسْبِيَ اللَّهُ لَا إِلَهَ إِلَّا هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيمِ.","count":1,"source":"القرآن الكريم، التوبة: 129","grade":"آية قرآنية"}
        ]
    },
    "daily": {
        "title": "أذكار يومية متنوعة",
        "items": [
            {"text":"رَبِّ زِدْنِي عِلْمًا.","count":1,"source":"القرآن الكريم، طه: 114","grade":"دعاء قرآني"},
            {"text":"رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ.","count":1,"source":"القرآن الكريم، البقرة: 201","grade":"دعاء قرآني"}
        ]
    }
}

for key, data in sections.items():
    path = base / f"{key}.json"
    if not path.exists():
        for i, item in enumerate(data["items"], 1):
            item["id"] = i
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("تم إنشاء:", path)
    else:
        print("موجود مسبقًا، لم يتغير:", path)

page = Path("pages/adhkar.html")
html = page.read_text(encoding="utf-8")

old_tabs = re.compile(r'<div class="tabs">.*?</div>\s*(<div class="progress-box">)', re.S)
new_tabs = '''<div class="tabs">
<label for="categorySelect">اختار قسم الأذكار:</label>
<select id="categorySelect" style="width:100%;margin-top:10px;background:#0e1812;color:#f1f5f2;border:1px solid #174f35;border-radius:10px;padding:12px;font-size:16px">
<option value="morning">🌅 أذكار الصباح</option>
<option value="evening">🌇 أذكار المساء</option>
<option value="after-prayer">🕌 أذكار بعد الصلاة</option>
<option value="sleep">🌙 أذكار النوم</option>
<option value="waking">☀️ أذكار الاستيقاظ</option>
<option value="food">🍽️ أذكار الطعام والشراب</option>
<option value="travel">🚗 دعاء السفر</option>
<option value="distress">🤲 أدعية الكرب والهم</option>
<option value="daily">📿 أدعية قرآنية متنوعة</option>
</select>
</div>

\\1'''

html, n = old_tabs.subn(new_tabs, html, count=1)
if n != 1:
    raise SystemExit("لم أستطع تحديد مكان أزرار الصباح والمساء. لم أعدّل الصفحة.")

html = html.replace(
    "const morningBtn = document.getElementById('morningBtn');\nconst eveningBtn = document.getElementById('eveningBtn');",
    "const categorySelect = document.getElementById('categorySelect');"
)
html = html.replace(
    "  morningBtn.classList.toggle('active', type === 'morning');\n  eveningBtn.classList.toggle('active', type === 'evening');",
    "  categorySelect.value = type;"
)
html = html.replace(
    "morningBtn.addEventListener('click', () => loadAdhkar('morning'));\neveningBtn.addEventListener('click', () => loadAdhkar('evening'));",
    "categorySelect.addEventListener('change', () => loadAdhkar(categorySelect.value));"
)
page.write_text(html, encoding="utf-8")
print("تم تحديث واجهة صفحة الأذكار.")
