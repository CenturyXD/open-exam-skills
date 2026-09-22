# AWS Certified Developer – Associate (DVA-C02) — คู่มือทบทวน

อัปเดต: 2026-09-22  
ใช้ไฟล์นี้ import เข้า Notion ได้ทั้งก้อน หรือแยกหน้าตามหัวข้อด้านล่าง

---

## รูปแบบข้อสอบ

| รายการ | ค่า |
|--------|-----|
| รหัส | DVA-C02 |
| จำนวนข้อ | 65 ข้อ |
| เวลา | 130 นาที |
| คะแนนผ่าน | 720 / 1000 |
| ค่าธรรมเนียม | ประมาณ USD 150 |

### Domain weights

1. **Development with AWS Services — 32%**
2. **Security — 26%**
3. **Deployment — 24%**
4. **Troubleshooting and Optimization — 18%**

### ไทม์ไลน์เวอร์ชัน

- สอบ **DVA-C02** ได้ถึง **30 พ.ย. 2026**
- **DVA-C03** เปิดลงทะเบียน 27 ต.ค. 2026 / เริ่มสอบ 1 ธ.ค. 2026
- ถ้าพร้อมแล้วและต้องการใบรับรองเร็ว → สอบ C02 ได้

### ลิงก์ทางการ

- [หน้าข้อสอบ](https://aws.amazon.com/certification/certified-developer-associate/)
- [Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS-Certified-Developer-Associate_Exam-Guide.pdf)
- [Skill Builder](https://skillbuilder.aws/)

---

## Domain 1 — Development with AWS Services (32%)

### Lambda

- ตั้งค่า: memory (มีผล CPU), timeout, concurrency, runtime, handler, layers, env vars
- **Sync** (API Gateway): caller จัดการ error — ไม่มี async auto-retry
- **Async** (S3, SNS, EventBridge): retry สูงสุด 2 ครั้ง (รวม 3 attempts)
- **Event source mapping** (SQS / Kinesis / DynamoDB Streams): Lambda เป็นคน poll
- **Destinations** vs **DLQ**: Destinations ส่ง success/failure + metadata ได้; DLQ เก็บ failed payload ของ async
- เข้า VPC: private subnet + SG; ออก internet ต้องมี NAT Gateway (หรือ VPC endpoint สำหรับบริการ AWS)

### DynamoDB

- ออกแบบ key ตาม **access pattern**
- **Query** > **Scan** เมื่อรู้ partition key
- **GSI**: key ใหม่ได้ สร้างทีหลังได้ — อ่าน eventually consistent
- **LSI**: partition key เดิม เปลี่ยน sort key — สร้างตอนสร้างตาราง
- หลีกเลี่ยง **hot partition** ด้วย high-cardinality partition key
- Streams, TTL, DAX สำหรับ read cache

### Integration

- API Gateway: REST / HTTP / WebSocket, stages, authorizers
- SQS Standard = at-least-once + best-effort order
- SQS FIFO = order ต่อ Message Group + exactly-once (ในเงื่อนไข)
- SNS + SQS = fan-out
- EventBridge = content-based routing / event bus
- S3 events → Lambda: ทำให้ idempotent + มี Destinations/DLQ

---

## Domain 2 — Security (26%)

### IAM

- **Trust policy** = ใคร AssumeRole ได้
- **Permissions policy** = role ทำอะไรได้
- Lambda execution role ≠ resource-based policy ที่อนุญาตให้บริการอื่น invoke
- Least privilege + แยก role ต่อฟังก์ชัน + ไม่ฝัง long-term keys ในโค้ด

### Cognito

- **User Pools** = sign-up / sign-in / JWT (authentication)
- **Identity Pools** = temporary AWS credentials ผ่าน STS (authorization เข้า AWS resources)

### Secrets & encryption

- **Secrets Manager** → secrets + automatic rotation
- **SSM Parameter Store** → config hierarchical / SecureString
- KMS สำหรับ encryption at rest
- ACM สำหรับ TLS certificates
- WAF กับ API Gateway / CloudFront

---

## Domain 3 — Deployment (24%)

### CI/CD

| บริการ | หน้าที่ |
|--------|---------|
| CodePipeline | orchestrate stages |
| CodeBuild | build / test ตาม buildspec |
| CodeDeploy | deploy ตาม AppSpec (EC2 / ECS / Lambda) |
| CodeArtifact | package repository |

### IaC

- CloudFormation = template / stacks / change sets
- **SAM** = shorthand สำหรับ serverless บน CloudFormation
- **CDK** = เขียนด้วยโค้ด แล้ว synth เป็น CloudFormation

### Deployment strategies

- All-at-once — เร็ว แต่เสี่ยง
- Rolling — ทยอยเปลี่ยน
- Blue/green — สลับ environment / rollback เร็ว
- Canary / linear — เลื่อน traffic ทีละส่วน (Lambda alias + CodeDeploy)

---

## Domain 4 — Troubleshooting & Optimization (18%)

### Observability

- CloudWatch Logs / Metrics / Alarms
- **X-Ray** = distributed tracing + service map (หาจุดช้าใน call chain)
- CloudTrail = API activity ในบัญชี

### ปัญหาที่พบบ่อยในข้อสอบ

- Lambda: timeout, memory, throttling, cold start
- DynamoDB: throttling จาก hot partition
- SQS: visibility timeout, poison messages
- API Gateway: 4xx vs 5xx, CORS, permission errors

### Optimization

- เพิ่ม Lambda memory เพื่อได้ CPU เพิ่ม
- DynamoDB on-demand vs provisioned
- Caching: lazy loading / write-through / TTL
- Provisioned concurrency ลด cold start เมื่อจำเป็น

---

## บริการที่ต้องชำนาญ

Lambda · DynamoDB · IAM · API Gateway · S3 · SQS / SNS / EventBridge · CodePipeline / CodeBuild / CodeDeploy · CloudWatch / X-Ray · Cognito · KMS / Secrets Manager

### รู้พอใช้

Elastic Beanstalk · CloudFormation / SAM / CDK · ElastiCache / DAX · Step Functions · ECS / ECR basics

---

## แผนอ่าน 3 เฟส

1. **พื้นฐาน** — Exam Guide + Lambda / DynamoDB / IAM + flashcards Domain 1–2
2. **Deploy & debug** — pipeline เล็ก ๆ + X-Ray / CloudWatch + deployment strategies
3. **จำลองสอบ** — Official Practice Question Set / practice exams จน ~80%+ แล้วทบทวนข้อผิด

---

## ไฟล์ Markdown ในชุดนี้ (สำหรับ Notion)

| ไฟล์ | เนื้อหา |
|------|---------|
| `STUDY-GUIDE.md` | คู่มือสรุปนี้ (แนะนำ import เป็นหน้าหลัก) |
| `flashcards.md` | บัตรท่อง 30 ข้อ |
| `quiz.md` | แบบทดสอบ 20 ข้อพร้อมเฉลย |
| `mindmap.md` | แผนที่ความคิดแบบ outline |
| `SOURCES.md` | แหล่งอ้างอิงทางการ |

### วิธีใส่ Notion

1. ใน Notion: **Import → Markdown**
2. เลือกไฟล์ `.md` ที่ต้องการ (แนะนำเริ่มที่ `STUDY-GUIDE.md`)
3. หรือเปิดไฟล์แล้ว Copy ทั้งหมด → Paste ในหน้า Notion
