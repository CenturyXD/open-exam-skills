# ชุดเรียน: พ.ร.บ.ระเบียบข้าราชการพลเรือน พ.ศ. 2551

ชุดทบทวนสอบจากตัวบทและแหล่งราชการ

## ไฟล์ในชุดนี้

| ไฟล์ | คำอธิบาย |
|------|----------|
| `SUMMARY.md` | **สรุปเนื้อหาฉบับละเอียด (เริ่มที่นี่)** |
| `SOURCES.md` | แหล่งอ้างอิง |
| `mindmap.md` | แผนที่ความคิด |
| `flashcards.json` | บัตรคำ 20 ใบ |
| `quiz.json` | แบบทดสอบ 5 ชุด ชุดละ 30 ข้อ |

## วิธีใช้

1. อ่าน `SUMMARY.md`
2. ดูโครงใน `mindmap.md`
3. ท่องด้วย `flashcards.json`
4. ทดสอบด้วย `quiz.json` (เลือกชุด 1–5)

## สร้าง HTML (ถ้าต้องการ)

```bash
cd skills/mindmap && python main.py -i ../../study/civil-service-act-2551/mindmap.md -o ../../study/civil-service-act-2551/mindmap.html
cd ../flashcards && python main.py -i ../../study/civil-service-act-2551/flashcards.json -o ../../study/civil-service-act-2551/flashcards.html
cd ../quiz && python main.py -i ../../study/civil-service-act-2551/quiz.json -o ../../study/civil-service-act-2551/quiz.html
```

## ขอบเขตเนื้อหา

- พ.ร.บ.ระเบียบข้าราชการพลเรือน พ.ศ. 2551
- ม.4 นิยาม · ก.พ. vs ก.พ.ค.
- จรรยา ม.78 (5 ประเด็น) · ม.79
- วินัย ม.82/83/85
