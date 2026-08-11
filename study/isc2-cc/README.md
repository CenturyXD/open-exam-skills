# ชุดเรียน: ISC² Certified in Cybersecurity (CC)

ชุดทบทวนสอบ certification ระดับ entry ของ ISC² จาก Official Exam Outline และ Study Pack

## ไฟล์ในชุดนี้

| ไฟล์ | คำอธิบาย |
|------|----------|
| `SUMMARY.md` / `summary.html` | **สรุปฉบับละเอียด (เริ่มที่นี่)** |
| `SOURCES.md` | รายการแหล่งข้อมูลอย่างเป็นทางการ + น้ำหนักโดเมน |
| `mindmap.md` / `mindmap.html` | แผนที่ความคิด 5 โดเมน |
| `flashcards.json` / `flashcards.html` | บัตรคำท่องจำ 40 ใบ |
| `quiz.json` / `quiz.html` | แบบทดสอบปรนัย 20 ข้อ |

## วิธีใช้

1. อ่าน `summary.html`
2. ดูโครงใน `mindmap.html`
3. ท่องด้วย `flashcards.html`
4. ทดสอบด้วย `quiz.html`

### อ่านบนมือถือ / เปิดผ่าน URL (htmlpreview)

- **สรุป:** https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/isc2-cc-study-pack-bed1/study/isc2-cc/summary.html
- แผนที่ความคิด: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/isc2-cc-study-pack-bed1/study/isc2-cc/mindmap.html
- บัตรคำ: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/isc2-cc-study-pack-bed1/study/isc2-cc/flashcards.html
- ข้อสอบ: https://htmlpreview.github.io/?https://github.com/CenturyXD/open-exam-skills/blob/cursor/isc2-cc-study-pack-bed1/study/isc2-cc/quiz.html

## สร้าง HTML ใหม่ (ถ้าแก้ไข JSON/Markdown)

```bash
cd skills/mindmap && python main.py -i ../../study/isc2-cc/mindmap.md -o ../../study/isc2-cc/mindmap.html
cd ../flashcards && python main.py -i ../../study/isc2-cc/flashcards.json -o ../../study/isc2-cc/flashcards.html
cd ../quiz && python main.py -i ../../study/isc2-cc/quiz.json -o ../../study/isc2-cc/quiz.html
```

## ขอบเขตเนื้อหา (โครงปัจจุบันจนถึงก่อน 1 ก.ย. 2026)

1. Security Principles (26%)
2. BC, DR & Incident Response Concepts (10%)
3. Access Controls Concepts (22%)
4. Network Security (24%)
5. Security Operations (18%)

## เส้นทางเตรียมสอบแนะนำ

1. สมัครสมาชิก Candidate ของ ISC² และเรียน Official Self-Paced Training (ฟรีภายใต้ One Million Certified pledge)
2. ทบทวน Official Exam Outline ทีละโดเมน
3. ใช้ summary → mindmap → flashcards → quiz ในชุดนี้วนรอบจุดอ่อน
4. จองสอบที่ Pearson VUE เมื่อพร้อม (เป้าหมาย 700/1000)

## คำเตือน

ชุดนี้เป็นสื่อทบทวน ไม่ใช่ Official ISC² course และไม่รับประกันผลสอบ — ตรวจ outline ล่าสุดก่อนสอบเสมอ
