# ชุดเรียน: กฎหมาย กฎ ระเบียบ นโยบาย IT ทั่วไป

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
cd skills/mindmap && python main.py -i ../../study/it-laws-policies/mindmap.md -o ../../study/it-laws-policies/mindmap.html
cd ../flashcards && python main.py -i ../../study/it-laws-policies/flashcards.json -o ../../study/it-laws-policies/flashcards.html
cd ../quiz && python main.py -i ../../study/it-laws-policies/quiz.json -o ../../study/it-laws-policies/quiz.html
```

## ขอบเขตเนื้อหา

- พ.ร.บ.ธุรกรรมฯ 2544
- พ.ร.บ.คอมพิวเตอร์ 2550/2560
- PDPA · Cybersecurity Act · CIA triad
- ความสัมพันธ์กับศาล e-justice
