# Flashcards — AWS Developer Associate (DVA-C02)

> วิธีใช้ใน Notion: Import ไฟล์นี้ หรือ copy ทั้งหน้าไปวางในหน้า Notion แล้วพับ toggle ได้

---

## 1. Domain weights ของ DVA-C02 มีอะไรบ้าง?

1. Development with AWS Services — 32%

2. Security — 26%

3. Deployment — 24%

4. Troubleshooting and Optimization — 18%

• ที่มา: Official Exam Guide

---

## 2. รูปแบบข้อสอบ DVA-C02 เป็นอย่างไร?

• 65 ข้อ

• 130 นาที

• Multiple choice / multiple response

• ผ่านที่ scaled score 720/1000

• ค่าธรรมเนียมประมาณ USD 150

---

## 3. Lambda synchronous vs asynchronous invocation ต่างกันอย่างไรเรื่อง retry?

• Synchronous (เช่น API Gateway): caller จัดการ error / ไม่มี auto-retry จาก Lambda service

• Asynchronous (เช่น S3, SNS, EventBridge): Lambda retry อัตโนมัติสูงสุด 2 ครั้ง (รวม 3 attempts)

• Event source mapping (SQS/Kinesis/DDB Streams): Lambda poll และจัดการ partial batch ตาม config

---

## 4. เมื่อ Lambda ต้องเข้าถึง resource ใน private subnet ต้องทำอะไร?

• เชื่อม Lambda กับ VPC (private subnets + security groups)

• ถ้าต้องออก internet: มี route ไป NAT Gateway

• ใช้ VPC endpoints สำหรับบริการ AWS บางชนิดเพื่อไม่พึ่ง internet

• Execution role ต้องมีสิทธิ์สร้าง ENI (AWSLambdaVPCAccessExecutionRole)

---

## 5. Lambda Destinations ต่างจาก DLQ อย่างไร?

• DLQ (SQS/SNS): เก็บเฉพาะ failed event payload ของ async invocation

• Destinations: ส่ง record ของ success หรือ failure ได้ และมี metadata เพิ่ม (เช่น response, stack trace)

• Destinations รองรับ SQS, SNS, EventBridge, Lambda อีกตัว

---

## 6. พารามิเตอร์สำคัญที่ต้องตั้งค่า Lambda มีอะไรบ้าง?

• Memory (มีผลต่อ CPU ด้วย)

• Timeout

• Concurrency / reserved concurrency

• Runtime และ handler

• Environment variables

• Layers / extensions

• Triggers และ destinations

---

## 7. DynamoDB Query ต่างจาก Scan อย่างไร?

• Query: อ่านด้วย partition key (และเงื่อนไข sort key) — มีประสิทธิภาพ

• Scan: อ่านทั้งตารางหรือ index — แพงและช้าเมื่อตารางใหญ่

• ข้อสอบมักเลือก Query + ออกแบบ key ให้ตรง access pattern

---

## 8. GSI กับ LSI ใน DynamoDB ต่างกันอย่างไร?

• LSI: ใช้ partition key เดียวกับตาราง เปลี่ยน sort key; สร้างตอนสร้างตาราง; ใช้ throughput ของตาราง

• GSI: partition/sort key ใหม่ได้; สร้าง/ลบทีหลังได้; มี throughput แยก

• LSI รองรับ strongly consistent; GSI เป็น eventually consistent

---

## 9. Eventually consistent vs strongly consistent reads ใน DynamoDB?

• Eventually consistent (default): อาจอ่านค่าเก่าชั่วคราว — ถูกกว่า/throughput สูงกว่า

• Strongly consistent: ได้ค่าล่าสุดที่เขียนสำเร็จแล้ว — ใช้ RCU มากขึ้น

• Global tables / GSI ไม่รองรับ strongly consistent ในลักษณะเดียวกับ base table

---

## 10. ทำอย่างไรไม่ให้ DynamoDB มี hot partition?

• เลือก partition key ที่มี high cardinality

• หลีกเลี่ยง key ที่ skew มาก (เช่น status=ACTIVE อย่างเดียว)

• ใช้ write sharding / composite keys ตาม access pattern

• ดู CloudWatch ThrottledRequests / การกระจาย RCU/WCU

---

## 11. SQS Standard กับ FIFO ต่างกันอย่างไร?

• Standard: at-least-once, best-effort ordering, throughput สูงมาก

• FIFO: exactly-once processing (ในเงื่อนไข), order ต่อ Message Group, throughput จำกัดกว่า

• FIFO ต้องมี MessageGroupId และมักใช้ Content-based deduplication หรือ DeduplicationId

---

## 12. SQS visibility timeout ใช้ทำอะไร และตั้งอย่างไรเมื่อมี Lambda?

• ซ่อนข้อความระหว่าง consumer ประมวลผล เพื่อไม่ให้ consumer อื่นรับซ้ำทันที

• ควรยาวกว่าเวลาประมวลผลสูงสุด

• ถ้า fail ก่อนหมดเวลา ข้อความจะกลับมา visible

• กับ Lambda event source: จัดการ partial batch failure / ระวัง poison message

---

## 13. รูปแบบ SNS + SQS fan-out คืออะไร?

• Publisher ส่งไป SNS topic ครั้งเดียว

• มีหลาย SQS queues subscribe topic

• แต่ละ consumer อ่านจาก queue ของตนแบบ decoupled

• ใช้เมื่อต้องการ fan-out ไปหลายระบบอย่างทนทาน

---

## 14. IAM trust policy ต่างจาก permissions policy อย่างไร?

• Trust policy (resource-based บน role): ใคร AssumeRole ได้บ้าง

• Permissions policy: role นั้นทำอะไรได้บน AWS resources

• Lambda execution role = permissions ให้ฟังก์ชันเรียกบริการอื่น

• Resource-based policy บน Lambda = ใคร/บริการไหน invoke ได้

---

## 15. เมื่อไหร่ใช้ Secrets Manager แทน SSM Parameter Store?

• Secrets Manager: โฟกัส secrets + automatic rotation + integrate กับ RDS ฯลฯ (มีค่าใช้จ่ายต่อ secret)

• Parameter Store: config ทั่วไป hierarchical; SecureString เข้ารหัสด้วย KMS; Standard ฟรีในโควตา; Advanced มี throughput/ขนาดสูงกว่า

• ข้อสอบ: password/API key ที่ต้อง rotate → Secrets Manager

---

## 16. Cognito User Pools กับ Identity Pools ต่างกันอย่างไร?

• User Pools: directory สำหรับ sign-up/sign-in ออก JWT (authentication)

• Identity Pools (Federated Identities): แลก identity เป็น AWS temporary credentials ผ่าน STS (authorization เข้า AWS resources)

• มักใช้คู่กัน: login ด้วย User Pool แล้วได้ IAM creds จาก Identity Pool

---

## 17. หลัก least privilege สำหรับแอปบน AWS คืออะไร?

• ให้สิทธิ์เท่าที่จำเป็นต่อ task

• ใช้ role แยกต่อฟังก์ชัน/บริการ แทน long-term access key ในโค้ด

• จำกัด resource ARN และเงื่อนไข (Condition) ใน policy

• หมุนเวียน credentials และใช้ STS temporary creds

---

## 18. CodePipeline / CodeBuild / CodeDeploy แบ่งหน้าที่อย่างไร?

• CodePipeline: orchestrate stages ของ CI/CD

• CodeBuild: compile/test/package ตาม buildspec.yml

• CodeDeploy: deploy ไป EC2/On-Prem/ECS/Lambda ตาม AppSpec

• Source มักมาจาก CodeCommit, GitHub, หรือ S3

---

## 19. กลยุทธ์ deploy ที่พบบ่อยในข้อสอบมีอะไร?

• All-at-once: เร็ว แต่เสี่ยง downtime

• Rolling: ทยอยเปลี่ยนชุด instances

• Blue/green: สภาพแวดล้อมคู่แล้วสลับ traffic

• Canary / linear: เลื่อน traffic ทีละส่วน (Lambda alias + CodeDeploy)

• เลือกตามความเสี่ยงและ rollback requirement

---

## 20. AWS SAM กับ CloudFormation และ CDK สัมพันธ์กันอย่างไร?

• SAM: ขยาย CloudFormation สำหรับ serverless (ง่ายกว่าสำหรับ Lambda/API/DynamoDB)

• CloudFormation: IaC หลักแบบ declarative templates

• CDK: เขียน IaC ด้วยภาษาโปรแกรม แล้ว synth เป็น CloudFormation

• ทั้งสามใช้ deploy เป็น stacks บน AWS

---

## 21. API Gateway stages และ canary release ใช้ทำอะไร?

• Stage = สภาพแวดล้อมของ API (dev/test/prod) พร้อม stage variables

• Canary release: ส่งเปอร์เซ็นต์ traffic ไป deployment ใหม่ใน stage เดิม

• ใช้ทดสอบเวอร์ชันใหม่แบบควบคุมความเสี่ยงก่อน promote เต็ม

---

## 22. CloudWatch กับ X-Ray ใช้ต่างกันอย่างไรเวลา debug?

• CloudWatch Logs/Metrics/Alarms: ดู log, metric, แจ้งเตือนระดับบริการ/ฟังก์ชัน

• X-Ray: distributed tracing ดู latency เป็น segment/subsegment และ service map

• ใช้ร่วมกัน: metric บอกว่าพัง → X-Ray บอกจุดช้า/error ใน call chain

---

## 23. วิธีลด cold start ของ Lambda มีแนวทางใดบ้าง?

• Provisioned concurrency สำหรับ latency-sensitive

• ลดขนาด package / ใช้ lean dependency

• Init โค้ดหนักนอก handler อย่างระมัดระวัง

• เลือก runtime ที่เหมาะสม

• หลีกเลี่ยง VPC ถ้าไม่จำเป็น (หรือใช้ snapshot/ENI optimization ตามแนวทางปัจจุบัน)

---

## 24. S3 event ไป Lambda แล้วประมวลผลล้มเหลว ควรคิดเรื่องอะไร?

• S3 → Lambda เป็น asynchronous → มี retry ของ Lambda

• ตั้ง Destinations/DLQ เพื่อจับ failure

• ทำให้ processing เป็น idempotent (event อาจซ้ำ)

• ตรวจสิทธิ์ resource-based policy ของ Lambda และ IAM ของ S3

---

## 25. ElastiCache / DAX ช่วยแอปอย่างไรในมุม Developer Associate?

• ElastiCache (Redis/Memcached): cache ชั้นแอป ลดโหลด DB

• DAX: in-memory cache เฉพาะ DynamoDB ลด read latency

• รู้ caching patterns: lazy loading, write-through, TTL

• ระวัง stale data และ invalidation

---

## 26. สิ่งที่อยู่นอกขอบเขตข้อสอบ (ไม่ต้องออกแบบลึก) มีแนวทางใด?

จาก Exam Guide — ไม่เน้นให้

• ออกแบบ distributed architecture ระดับ Solutions Architect ลึก ๆ

• บริหาร IAM users/groups ระยะยาวแบบ admin

• ออกแบบเครือข่าย VPC/Direct Connect ซับซ้อน

• โฟกัส: พัฒนา ทดสอบ deploy debug แอปบน AWS

---

## 27. Amazon EventBridge เหมาะกับสถานการณ์ใด?

• Event bus สำหรับ event-driven architecture

• Rule กรอง event แล้วส่งไป target หลายตัว

• Integrate กับ AWS services, SaaS partners, custom apps

• เหมาะกว่า SNS เมื่อต้องการ content-based routing / schema

---

## 28. ก่อนสอบจริงควรทำอะไรบ้าง?

1. อ่าน Official Exam Guide ให้ครบ domains

2. Hands-on lab: Lambda + API GW + DynamoDB + IAM + pipeline

3. ท่องจุดเปรียบเทียบบริการ (SQS/SNS, SAM/CFN, Secrets/SSM)

4. ทำ practice exams จน ~80%+

5. ทบทวนข้อผิดด้วย flashcards

---

## 29. DVA-C02 กับ DVA-C03 ต่างกันอย่างไรในภาพรวม (2026)?

• C02: สอบได้ถึง 30 พ.ย. 2026 — โฟกัสพัฒนาแอป AWS แบบเดิม

• C03: GA 1 ธ.ค. 2026 — เพิ่ม AI-assisted development และ AI security

• รูปแบบยังประมาณ 65 ข้อ / 130 นาที / ผ่าน 720

• ถ้าพร้อมแล้วและต้องการใบรับรองเร็ว → สอบ C02 ได้

---

## 30. ทำไมข้อสอบชอบถามเรื่อง idempotency?

• ระบบกระจาย/queue/retry ทำให้ processing ซ้ำได้

• ต้องออกแบบให้ทำซ้ำแล้วได้ผลเทียบเท่า (เช่น conditional write, dedupe keys)

• เกี่ยวกับ SQS at-least-once, Lambda async retries, Step Functions retries

---
