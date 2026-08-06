# ชุดเรียน: กฎหมาย กฎ และระเบียบในการปฏิบัติราชการ

ชุดทบทวนสอบจากแหล่งราชการ (ราชกิจจานุเบกษา, สำนักงาน ก.พ., ก.พ.ร., สขร.)

## ไฟล์ในชุดนี้

| ไฟล์ | คำอธิบาย |
|------|----------|
| `SOURCES.md` | รายการแหล่งข้อมูลที่น่าเชื่อถือ |
| `mindmap.md` / `mindmap.html` | แผนที่ความคิด |
| `flashcards.json` / `flashcards.html` | บัตรคำท่องจำ |
| `quiz.json` / `quiz.html` | แบบทดสอบปรนัย 15 ข้อ |

## วิธีใช้

1. อ่าน `SOURCES.md` เพื่อรู้แหล่งอ้างอิง
2. เปิด `mindmap.html` เพื่อดูภาพรวมโครงสร้าง
3. ท่องด้วย `flashcards.html`
4. ทดสอบด้วย `quiz.html`

## สร้าง HTML ใหม่ (ถ้าแก้ไข JSON/Markdown)

```bash
cd skills/mindmap && python main.py -i ../../study/civil-service-laws/mindmap.md -o ../../study/civil-service-laws/mindmap.html
cd ../flashcards && python main.py -i ../../study/civil-service-laws/flashcards.json -o ../../study/civil-service-laws/flashcards.html
cd ../quiz && python main.py -i ../../study/civil-service-laws/quiz.json -o ../../study/civil-service-laws/quiz.html
```

## ขอบเขตเนื้อหา

- พ.ร.บ.ระเบียบข้าราชการพลเรือน พ.ศ. 2551
- ประมวลจริยธรรมข้าราชการพลเรือน พ.ศ. 2564
- พ.ร.ฎ.บริหารกิจการบ้านเมืองที่ดี พ.ศ. 2546
- พ.ร.บ.ความรับผิดทางละเมิดของเจ้าหน้าที่ พ.ศ. 2539
- พ.ร.บ.ข้อมูลข่าวสารของราชการ พ.ศ. 2540
