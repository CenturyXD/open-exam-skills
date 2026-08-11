# ชุดเรียน: ข้อกำหนด/คำแนะนำประธานศาลฎีกาด้าน IT

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
cd skills/mindmap && python main.py -i ../../study/sc-president-it/mindmap.md -o ../../study/sc-president-it/mindmap.html
cd ../flashcards && python main.py -i ../../study/sc-president-it/flashcards.json -o ../../study/sc-president-it/flashcards.html
cd ../quiz && python main.py -i ../../study/sc-president-it/quiz.json -o ../../study/sc-president-it/quiz.html
```

## ขอบเขตเนื้อหา

- ข้อกำหนดประธานศาลฎีกา 2563
- ป.พ.พ. ม.34/1 · e-signature
- ข้อ 24-25 · ข้อ 30
