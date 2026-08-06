# ชุดเรียน: กฎหมาย กฎ และระเบียบในการปฏิบัติราชการ

ชุดทบทวนสอบจากแหล่งราชการ (ราชกิจจานุเบกษา, สำนักงาน ก.พ., ก.พ.ร., สขร.)

## ไฟล์ในชุดนี้

| ไฟล์ | คำอธิบาย |
|------|----------|
| `SUMMARY.md` / `summary.html` | **สรุปเนื้อหาฉบับละเอียด (เริ่มที่นี่)** ครอบคลุม 10 หัวข้อ + แผนจำเร็ว |
| `SOURCES.md` | รายการแหล่งข้อมูลที่น่าเชื่อถือ |
| `mindmap.md` / `mindmap.html` | แผนที่ความคิด |
| `flashcards.json` / `flashcards.html` | บัตรคำท่องจำ |
| `quiz.json` / `quiz.html` | แบบทดสอบ 5 ชุด ชุดละ 30 ข้อ — เปิดแล้วเลือกชุดได้เอง |

## วิธีใช้

0. เปิด [เมนูหลัก](../index.html) แล้วเลือกอันที่ต้องการ
1. อ่าน `summary.html` (สรุปละเอียดทีละหมวด)
2. เปิด `mindmap.html` เพื่อดูภาพรวมโครงสร้าง
3. ท่องด้วย `flashcards.html`
4. ทดสอบด้วย `quiz.html` (เลือกชุด 1–5 ได้)

### อ่านบนมือถือ (Cloud)

- **เมนูหลัก:** https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/court-justice-admin-act-7242/study/index.html
- สรุปเนื้อหา: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/court-justice-admin-act-7242/study/civil-service-laws/summary.html
- แผนที่ความคิด: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/court-justice-admin-act-7242/study/civil-service-laws/mindmap.html
- บัตรคำ: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/court-justice-admin-act-7242/study/civil-service-laws/flashcards.html
- ข้อสอบ: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/court-justice-admin-act-7242/study/civil-service-laws/quiz.html

## สร้าง HTML ใหม่ (ถ้าแก้ไข JSON/Markdown)

```bash
# สรุป: แปลง SUMMARY.md → summary.html ด้วยสคริปต์ใน repo หรือแก้ summary.html ให้ตรงกับ SUMMARY.md
cd skills/mindmap && python main.py -i ../../study/civil-service-laws/mindmap.md -o ../../study/civil-service-laws/mindmap.html
cd ../flashcards && python main.py -i ../../study/civil-service-laws/flashcards.json -o ../../study/civil-service-laws/flashcards.html
cd ../quiz && python main.py -i ../../study/civil-service-laws/quiz.json -o ../../study/civil-service-laws/quiz.html
```

## ขอบเขตเนื้อหา

**ชุดหลัก**
- พ.ร.บ.ระเบียบข้าราชการพลเรือน พ.ศ. 2551
- ประมวลจริยธรรมข้าราชการพลเรือน พ.ศ. 2564
- พ.ร.ฎ.บริหารกิจการบ้านเมืองที่ดี พ.ศ. 2546
- พ.ร.บ.ความรับผิดทางละเมิดของเจ้าหน้าที่ พ.ศ. 2539
- พ.ร.บ.ข้อมูลข่าวสารของราชการ พ.ศ. 2540

**ชุดเสริม (มีในสรุป + ควิซ)**
- พ.ร.บ.วิธีปฏิบัติราชการทางปกครอง พ.ศ. 2539
- พ.ร.บ.การอำนวยความสะดวกในการพิจารณาอนุญาตฯ พ.ศ. 2558
- พ.ร.บ.จัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ พ.ศ. 2560
- ระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ
- พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA)
