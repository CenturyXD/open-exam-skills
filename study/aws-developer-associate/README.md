# ชุดเรียน: AWS Certified Developer – Associate (DVA-C02)

ชุดทบทวนสอบจาก Official Exam Guide และ AWS Docs สำหรับนักพัฒนาที่กำลังเตรียมสอบ Developer Associate

## ไฟล์ในชุดนี้

| ไฟล์ | คำอธิบาย |
|------|----------|
| `SOURCES.md` | รายการแหล่งข้อมูลทางการ + รูปแบบข้อสอบ |
| `mindmap.md` / `mindmap.html` | แผนที่ความคิดตาม 4 domains |
| `flashcards.json` / `flashcards.html` | บัตรคำท่องจำจุดที่ออกบ่อย |
| `quiz.json` / `quiz.html` | แบบทดสอบปรนัยแนวข้อสอบ 20 ข้อ |

## วิธีใช้

1. อ่าน `SOURCES.md` เพื่อรู้ขอบเขตและเวอร์ชันข้อสอบ
2. เปิด `mindmap.html` เพื่อเห็นภาพรวม 4 domains
3. ท่องด้วย `flashcards.html` (Space = พลิก, ←/→ = เปลี่ยนใบ)
4. ทดสอบด้วย `quiz.html` แล้วทบทวนข้อที่ผิด

## สร้าง HTML ใหม่ (ถ้าแก้ไข JSON/Markdown)

```bash
cd skills/mindmap && python main.py -i ../../study/aws-developer-associate/mindmap.md -o ../../study/aws-developer-associate/mindmap.html
cd ../flashcards && python main.py -i ../../study/aws-developer-associate/flashcards.json -o ../../study/aws-developer-associate/flashcards.html
cd ../quiz && python main.py -i ../../study/aws-developer-associate/quiz.json -o ../../study/aws-developer-associate/quiz.html
```

## ขอบเขตเนื้อหา

- Domain 1: Development with AWS Services (Lambda, DynamoDB, API Gateway, messaging)
- Domain 2: Security (IAM, Cognito, KMS, Secrets)
- Domain 3: Deployment (CI/CD, IaC, blue/green/canary)
- Domain 4: Troubleshooting and Optimization (CloudWatch, X-Ray)

## เป้าหมายคะแนน

ฝึกจนทำ practice exam ได้ประมาณ **80%+** อย่างสม่ำเสมอ ก่อนจองวันสอบจริง
