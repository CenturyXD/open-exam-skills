# แหล่งข้อมูลที่น่าเชื่อถือ — AWS Certified Developer – Associate (DVA-C02)

อัปเดต: 2026-09-22  
หลักการคัดแหล่ง: ใช้ Exam Guide / เอกสาร AWS อย่างเป็นทางการเป็นหลัก แล้วเสริมด้วย AWS Docs ของบริการที่อยู่ในขอบเขตข้อสอบ

## แหล่งหลัก (Primary / Official)

| ลำดับ | แหล่ง | บทบาท | URL |
|------|--------|--------|-----|
| S1 | AWS Certification – Developer Associate | หน้าข้อสอบ รายละเอียดรูปแบบและค่าธรรมเนียม | https://aws.amazon.com/certification/certified-developer-associate/ |
| S2 | DVA-C02 Exam Guide (PDF) | Domain weights, task statements, in/out-of-scope services | https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS-Certified-Developer-Associate_Exam-Guide.pdf |
| S3 | AWS Docs – Certification outline | Content outline แบบ HTML | https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html |
| S4 | AWS Skill Builder | Free digital training / Official Practice Question Set | https://skillbuilder.aws/ |
| S5 | AWS Training Blog | ประกาศอัปเดตข้อสอบ (เช่น DVA-C03) | https://aws.amazon.com/blogs/training-and-certification/ |

## เอกสารที่ใช้จัดทำชุดเรียนนี้

| ID | เอกสาร | แหล่ง | หมายเหตุ |
|----|--------|--------|----------|
| D1 | AWS Certified Developer – Associate Exam Guide (DVA-C02) | S2 | Domain 1–4 และน้ำหนักคะแนน |
| D2 | Content Domain outline (Developer Associate 02) | S3 | Task statements และ skills |
| D3 | AWS service documentation (Lambda, DynamoDB, IAM, CI/CD, X-Ray, Cognito, KMS) | AWS Docs | ใช้ยืนยันพฤติกรรมบริการที่ออกข้อสอบบ่อย |
| D4 | Certification updates – September 2026 | S5 | DVA-C02 สอบได้ถึง 30 พ.ย. 2026; DVA-C03 GA 1 ธ.ค. 2026 |

## รูปแบบข้อสอบ (DVA-C02)

| รายการ | ค่า |
|--------|-----|
| รหัสข้อสอบ | DVA-C02 |
| จำนวนข้อ | 65 ข้อ (multiple choice / multiple response) |
| เวลา | 130 นาที |
| คะแนนผ่าน | 720 / 1000 (scaled) |
| ค่าธรรมเนียม | USD 150 (อาจต่างตามประเทศ) |
| กลุ่มผู้เข้าสอบเป้าหมาย | ผู้พัฒนาแอปบน AWS ประมาณ 1 ปีขึ้นไป |

## Domain weights (DVA-C02)

1. Development with AWS Services — **32%**
2. Security — **26%**
3. Deployment — **24%**
4. Troubleshooting and Optimization — **18%**

## หมายเหตุเรื่องเวอร์ชันข้อสอบ

- ชุดนี้โฟกัส **DVA-C02** (เวอร์ชันปัจจุบัน ณ ก.ย. 2026)
- **วันสุดท้ายที่สอบ DVA-C02 ได้:** 30 พฤศจิกายน 2026
- **DVA-C03** เปิดลงทะเบียน 27 ต.ค. 2026 และเริ่มสอบจริง 1 ธ.ค. 2026 (เพิ่ม AI-assisted development / AI security)
- ใบรับรองที่ได้จาก C02 ยังใช้ได้ตามอายุใบรับรองปกติ ไม่ถูก reset เมื่อมี C03

## ขอบเขตชุดเรียนนี้

ครอบคลุมหัวข้อที่ออกบ่อยในการสอบ Developer Associate:
1. Lambda, API Gateway, DynamoDB, S3, messaging (SQS/SNS/EventBridge)
2. IAM, Cognito, KMS, Secrets Manager / Parameter Store
3. CI/CD (CodePipeline / CodeBuild / CodeDeploy), CloudFormation / SAM / CDK, deployment strategies
4. CloudWatch, X-Ray, performance และ error handling

## คำเตือนการใช้งาน

- ชุดนี้เป็นสรุปเพื่อทบทวนสอบ ไม่ทดแทน Official Exam Guide หรือ hands-on บน AWS Console
- พฤติกรรมบริการ AWS อาจเปลี่ยนได้ — เมื่อสงสัยให้เปิด AWS Docs ฉบับล่าสุด
- ข้อสอบเน้น **สถานการณ์ใช้งานจริง** มากกว่าท่องชื่อบริการเปล่า ๆ
