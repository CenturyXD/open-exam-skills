# แบบทดสอบ — AWS Developer Associate (DVA-C02)

> ทำทีละข้อ แล้วเลื่อนดูเฉลยด้านล่างแต่ละข้อ

---

## ข้อ 1

Domain ใดมีน้ำหนักมากที่สุดในข้อสอบ DVA-C02?

- **A.** Security (26%)
- **B.** Development with AWS Services (32%)
- **C.** Deployment (24%)
- **D.** Troubleshooting and Optimization (18%)

**เฉลย:** B

**Hint:** ดู Official Exam Guide — domain แรก

**อธิบาย:** Development with AWS Services มีน้ำหนัก 32% ซึ่งสูงสุด ตามด้วย Security 26%, Deployment 24%, Troubleshooting 18%

---

## ข้อ 2

แอปเรียก Lambda ผ่าน API Gateway แล้วฟังก์ชัน error — พฤติกรรม retry ใดถูกต้องที่สุด?

- **A.** Lambda จะ retry อัตโนมัติ 2 ครั้งเสมอ
- **B.** เป็นการเรียกแบบ synchronous — client/API Gateway เป็นผู้จัดการ error โดย Lambda service ไม่ทำ async retry
- **C.** ข้อความจะถูกส่งเข้า DLQ โดยอัตโนมัติทุกกรณี
- **D.** API Gateway จะสลับไป alias อื่นให้อัตโนมัติ

**เฉลย:** B

**Hint:** แยก sync กับ async invocation

**อธิบาย:** API Gateway → Lambda เป็น synchronous invocation — ไม่มี automatic async retry จาก Lambda service แบบ S3/SNS

---

## ข้อ 3

ทีมต้องการให้ Lambda อ่านข้อมูลจากฐานข้อมูลใน private subnet และยังเรียก API ภายนอก internet ได้ ต้องมีอะไร?

- **A.** วาง Lambda ใน public subnet พร้อม public IP เท่านั้น
- **B.** เชื่อม Lambda กับ private subnet และมี NAT Gateway (หรือทางออก internet ที่เทียบเท่า) ใน VPC
- **C.** เปิด 0.0.0.0/0 ใน security group ของ Lambda โดยไม่ต้องมี NAT
- **D.** ใช้เฉพาะ IAM policy โดยไม่ต้องแตะ VPC

**เฉลย:** B

**Hint:** ENI ใน private subnet ออก internet ได้อย่างไร?

**อธิบาย:** Lambda ใน VPC ใช้ ENI ใน subnet ที่กำหนด — การออก internet จาก private subnet ต้องอาศัย NAT Gateway (หรือเทียบเท่า) และ route ที่ถูกต้อง

---

## ข้อ 4

ต้องการอ่านรายการออเดอร์ของลูกค้าคนหนึ่งจาก DynamoDB อย่างมีประสิทธิภาพ ควรใช้การทำงานแบบใด?

- **A.** Scan ทั้งตารางแล้ว filter ที่แอป
- **B.** Query ด้วย partition key ของลูกค้า (+ sort key ถ้ามี)
- **C.** Scan บน GSI ทุกครั้งเพราะเร็วกว่า Query
- **D.** ใช้ only strongly consistent Scan

**เฉลย:** B

**Hint:** access pattern ชัด = key design + Query

**อธิบาย:** Query ด้วย partition key ที่ออกแบบตาม access pattern มีประสิทธิภาพและถูกกว่า Scan ทั้งตาราง

---

## ข้อ 5

ข้อใดถูกต้องเกี่ยวกับ Global Secondary Index (GSI)?

- **A.** ต้องสร้างตอนสร้างตารางเท่านั้น และใช้ strongly consistent read ได้เสมอ
- **B.** สามารถมี partition/sort key ต่างจากตาราง และสร้างทีหลังได้ แต่การอ่านเป็น eventually consistent
- **C.** ใช้ throughput ร่วมกับตารางเสมอเหมือน LSI
- **D.** ห้ามมี attribute ต่างจาก base table

**เฉลย:** B

**Hint:** เทียบกับ LSI

**อธิบาย:** GSI อนุญาต key ใหม่ สร้าง/ลบทีหลังได้ มีความจุแยก และการอ่านจาก GSI เป็น eventually consistent

---

## ข้อ 6

ระบบต้องประมวลผลข้อความตามลำดับต่อผู้ใช้ และไม่ต้องการ duplicate ในหน้าต่าง deduplication ควรเลือกอะไร?

- **A.** Amazon SNS Standard topic
- **B.** Amazon SQS Standard queue
- **C.** Amazon SQS FIFO queue
- **D.** Amazon S3 Event Notifications อย่างเดียว

**เฉลย:** C

**Hint:** ordering + exactly-once ในคิว

**อธิบาย:** SQS FIFO ให้ ordering ต่อ Message Group และรองรับ exactly-once processing ในเงื่อนไข deduplication

---

## ข้อ 7

Publisher ต้องการกระจาย event เดียวไปยังระบบย่อยหลายตัวที่แต่ละตัวประมวลผลอิสระและทนทาน แบบใดเหมาะสม?

- **A.** เรียก Lambda ของทุกระบบแบบ synchronous จาก publisher
- **B.** SNS topic fan-out ไปยังหลาย SQS queues
- **C.** เก็บไฟล์ใน EBS แล้วให้ทุกระบบ mount ร่วมกัน
- **D.** ใช้เฉพาะ Cognito User Pool

**เฉลย:** B

**Hint:** classic pub/sub + queue

**อธิบาย:** SNS → หลาย SQS เป็น fan-out pattern คลาสสิก ทำให้แต่ละ consumer อ่านคิวของตนอย่าง decoupled

---

## ข้อ 8

Lambda ต้องดึงรหัสผ่านฐานข้อมูลที่หมุนเวียนอัตโนมัติ ควรใช้บริการใดเป็นหลัก?

- **A.** SSM Parameter Store String ธรรมดาไม่เข้ารหัส
- **B.** AWS Secrets Manager
- **C.** เก็บใน environment variable แบบ hardcode
- **D.** ใส่ใน Docker image layer

**เฉลย:** B

**Hint:** rotation เป็นจุดเด่นของบริการใด?

**อธิบาย:** Secrets Manager ออกแบบมาสำหรับ secrets และรองรับ automatic rotation ซึ่งเหมาะกับรหัสผ่าน DB

---

## ข้อ 9

แอปมีหน้า login สมัครสมาชิก แล้วต้องการให้ผู้ใช้เข้าถึง AWS resources ด้วย temporary credentials — ใช้บริการใดคู่กัน?

- **A.** เฉพาะ IAM users ถาวรแจกให้ลูกค้าปลายทาง
- **B.** Cognito User Pool สำหรับ auth และ Identity Pool สำหรับ AWS credentials
- **C.** เฉพาะ AWS WAF
- **D.** เฉพาะ ACM

**เฉลย:** B

**Hint:** User Pool = auth, Identity Pool = AWS creds

**อธิบาย:** User Pools จัดการ sign-in/JWT ส่วน Identity Pools ออก temporary AWS credentials ผ่าน STS

---

## ข้อ 10

เอกสาร trust policy ของ IAM role กำหนดสิ่งใด?

- **A.** รายการ API ที่ role เรียกได้บน S3/DynamoDB
- **B.** Principal ที่อนุญาตให้ AssumeRole ได้
- **C.** Billing alert ของบัญชี
- **D.** Retention ของ CloudWatch Logs

**เฉลย:** B

**Hint:** trust ≠ permissions

**อธิบาย:** Trust policy บอกว่าใครassume role ได้; สิทธิ์ไปเรียกบริการอื่นอยู่ใน permissions policy

---

## ข้อ 11

ทีมต้องการ pipeline ที่ดึงโค้ดจาก Git แล้ว build ทดสอบ และ deploy ไป Lambda แบบ canary — ชุดบริการใดตรงที่สุด?

- **A.** Athena + QuickSight + Macie
- **B.** CodePipeline + CodeBuild + CodeDeploy (กับ Lambda alias traffic shifting)
- **C.** Amazon MQ + AWS Glue เท่านั้น
- **D.** AWS DataSync + Storage Gateway

**เฉลย:** B

**Hint:** CI/CD trio + deployment strategy

**อธิบาย:** CodePipeline คุม flow, CodeBuild แพ็กเกจ/ทดสอบ, CodeDeploy ทำ canary/linear บน Lambda aliases

---

## ข้อ 12

ต้องการ template สั้น ๆ สำหรับ serverless (Lambda + API Gateway + DynamoDB) ที่แปลงเป็น CloudFormation ได้ ควรเริ่มจากอะไร?

- **A.** AWS SAM
- **B.** Amazon EMR
- **C.** AWS Snowball
- **D.** Amazon Detective

**เฉลย:** A

**Hint:** serverless shorthand บน CloudFormation

**อธิบาย:** AWS SAM เป็นส่วนขยายของ CloudFormation ที่เขียน serverless resources ได้กระชับและ deploy เป็น stacks

---

## ข้อ 13

การ deploy แบบ blue/green มีข้อดีหลักข้อใด?

- **A.** ไม่ต้องมี environment สองชุดเลย
- **B.** สลับ traffic ไปสภาพแวดล้อมใหม่ได้ และ rollback เร็วเมื่อมีปัญหา
- **C.** บังคับ downtime ยาวทุกรอบ
- **D.** ใช้ได้เฉพาะกับ Amazon Glacier

**เฉลย:** B

**Hint:** สองสภาพแวดล้อม + สลับ traffic

**อธิบาย:** Blue/green เตรียม environment ใหม่คู่กันแล้ว切換 traffic ทำให้ลด downtime และ rollback ได้เร็ว

---

## ข้อ 14

ต้องการหาว่า microservice ใดใน request path ทำให้ latency สูง ควรใช้เครื่องมือใด?

- **A.** AWS X-Ray
- **B.** Amazon S3 Inventory อย่างเดียว
- **C.** AWS Snowcone
- **D.** Amazon Comprehend

**เฉลย:** A

**Hint:** distributed tracing / service map

**อธิบาย:** X-Ray ให้ tracing และ service map เพื่อชี้ segment ที่ช้าหรือ error ในสายเรียก

---

## ข้อ 15

DynamoDB ขึ้น ThrottledRequests ทั้งที่ provisioned capacity ดูสูง — สาเหตุที่พบบ่อยคืออะไร?

- **A.** ใช้ Query มากเกินไปแทน Scan
- **B.** Hot partition จาก partition key ที่กระจายไม่ดี
- **C.** เปิด TTL ไว้
- **D.** ใช้ IAM role แทน access key

**เฉลย:** B

**Hint:** capacity รวมสูง แต่ key เดียวรับโหลด

**อธิบาย:** แม้ capacity รวมจะพอ แต่ถ้า partition key skew โหลดจะกระจุกที่ partition เดียวจน throttle

---

## ข้อ 16

ข้อใดเป็นแนวทาง least privilege ที่ถูกต้องสำหรับ Lambda?

- **A.** ติด policy AdministratorAccess กับทุกฟังก์ชันเพื่อลดงาน ops
- **B.** ใช้ execution role แยกต่อฟังก์ชันและให้สิทธิ์เฉพาะ action/resource ที่จำเป็น
- **C.** ฝัง access key ของ root ในโค้ดแล้ว commit
- **D.** เปิด public บน security group ทุกพอร์ต

**เฉลย:** B

**Hint:** แยก role + สิทธิ์ขั้นต่ำ

**อธิบาย:** Least privilege = execution role เฉพาะงาน ไม่ใช้สิทธิ์กว้างเกิน และไม่ฝัง long-term keys ในโค้ด

---

## ข้อ 17

S3 ส่ง event เรียก Lambda แบบ async แล้วประมวลผลล้มเหลวซ้ำ — ควรตั้งค่าเพิ่มเติมใดเพื่อจับ failure ได้ดี?

- **A.** ปิด CloudWatch Logs
- **B.** ตั้ง Lambda Destinations หรือ DLQ สำหรับ failed asynchronous invocations
- **C.** ลบ IAM role ทั้งหมด
- **D.** เปลี่ยนบัคเก็ตเป็น public เสมอ

**เฉลย:** B

**Hint:** async failure handling

**อธิบาย:** สำหรับ async invocations ใช้ Destinations/DLQ เพื่อเก็บ failure records หลัง retry หมด

---

## ข้อ 18

ต้องการลด read latency ของ DynamoDB สำหรับ read-heavy workload โดยไม่เปลี่ยน data model มาก ตัวเลือกใดเกี่ยวข้องโดยตรง?

- **A.** Amazon DAX
- **B.** AWS Data Pipeline เท่านั้น
- **C.** Amazon Polly
- **D.** AWS Device Farm

**เฉลย:** A

**Hint:** DynamoDB-specific cache

**อธิบาย:** DAX เป็น in-memory cache สำหรับ DynamoDB ช่วยลด read latency ของ read-heavy workloads

---

## ข้อ 19

คะแนนผ่านขั้นต่ำของ DVA-C02 คือเท่าใด?

- **A.** 600 / 1000
- **B.** 700 / 1000
- **C.** 720 / 1000
- **D.** 800 / 1000

**เฉลย:** C

**Hint:** scaled score ของ AWS Associate หลายใบ

**อธิบาย:** ข้อสอบใช้ scaled score 100–1000 และเกณฑ์ผ่านคือ 720

---

## ข้อ 20

ตามประกาศปี 2026 วันสุดท้ายที่สอบ DVA-C02 ได้คือเมื่อใด?

- **A.** 30 กันยายน 2026
- **B.** 27 ตุลาคม 2026
- **C.** 30 พฤศจิกายน 2026
- **D.** 1 ธันวาคม 2026

**เฉลย:** C

**Hint:** วันก่อน DVA-C03 GA

**อธิบาย:** AWS ระบุว่าวันสุดท้ายของ DVA-C02 คือ 30 พฤศจิกายน 2026 และ DVA-C03 เริ่ม 1 ธันวาคม 2026

---
