# ชุดเรียน: ระเบียบ ประกาศ คำสั่ง ของสำนักงานศาลยุติธรรม

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
cd skills/mindmap && python main.py -i ../../study/oj-regulations/mindmap.md -o ../../study/oj-regulations/mindmap.html
cd ../flashcards && python main.py -i ../../study/oj-regulations/flashcards.json -o ../../study/oj-regulations/flashcards.html
cd ../quiz && python main.py -i ../../study/oj-regulations/quiz.json -o ../../study/oj-regulations/quiz.html
```

## ขอบเขตเนื้อหา

- ระเบียบ ประกาศ คำสั่ง ของสำนักงานศาลยุติธรรม
- นิติบุคคลอิสระ · เลขาธิการ
- ศาลอิเล็กทรอนิกส์ · e-Filing
