# สรุปเนื้อหาฉบับละเอียด: ISC² Certified in Cybersecurity (CC)

อัปเดต: 2026-08-11 · อ้างอิง Official CC Exam Outline

## 1) ภาพรวมข้อสอบ

| เรื่อง | จำ |
|--------|-----|
| ชื่อเต็ม | ISC² Certified in Cybersecurity (CC) |
| ระดับ | Entry / junior cybersecurity |
| Prerequisite | ไม่บังคับ (แนะนำมีพื้นฐาน IT) |
| เวลาสอบ | **2 ชั่วโมง** |
| จำนวนข้อ | **100–125** (CAT) |
| คะแนนผ่าน | **700 / 1000** |
| สถานที่ | Pearson VUE |
| ภาษา | English, Chinese, Japanese, German, Spanish |

**จำสั้น:** 2 ชม. · 100–125 ข้อ · ผ่าน 700

## 2) โดเมนและน้ำหนัก (ปัจจุบัน จนถึงก่อน 1 ก.ย. 2026)

| Domain | น้ำหนัก |
|--------|---------|
| 1. Security Principles | **26%** |
| 2. BC, DR & Incident Response Concepts | **10%** |
| 3. Access Controls Concepts | **22%** |
| 4. Network Security | **24%** |
| 5. Security Operations | **18%** |

## 3) Domain 1 — Security Principles (26%)

### CIA Triad + แนวคิดพื้นฐาน
- **Confidentiality** — จำกัดการเข้าถึงเฉพาะผู้มีสิทธิ์
- **Integrity** — ข้อมูลถูกต้อง ไม่ถูกแก้โดยไม่ได้รับอนุญาต
- **Availability** — พร้อมใช้เมื่อต้องการ
- **Authentication** — พิสูจน์ตัวตน (รวม MFA)
- **Authorization** — กำหนดว่าทำอะไรได้
- **Accounting** — บันทึก/ติดตามการใช้งาน
- **Non-repudiation** — ปฏิเสธการกระทำไม่ได้ (เช่น digital signature)
- **Privacy** — คุ้มครองข้อมูลส่วนบุคคลตามนโยบาย/กฎหมาย

### Risk management
1. Identify
2. Assess
3. Treat (mitigate / transfer / avoid / accept)
4. คำนึงถึง **risk priority** และ **risk tolerance**

### Security controls
| ประเภท | ตัวอย่าง |
|--------|----------|
| Technical | Firewall, encryption, MFA |
| Administrative | Policy, training, กระบวนการ |
| Physical | Badge, CCTV, lock |

### Governance
- **Policy** = ทิศทางระดับสูง
- **Standard** = ข้อกำหนดที่ต้องทำตาม
- **Procedure** = ขั้นตอนปฏิบัติ
- **Regulations / laws** = ข้อบังคับภายนอก

### ISC² Code of Ethics (จำ 4 ข้อ)
1. Protect society, the common good, necessary public trust and confidence, and the infrastructure
2. Act honorably, honestly, justly, responsibly, and legally
3. Provide diligent and competent service to principals
4. Advance and protect the profession

## 4) Domain 2 — BC, DR & Incident Response (10%)

| หัวข้อ | จุดจำ |
|--------|--------|
| **Business Continuity (BC)** | คงการดำเนินธุรกิจ/กระบวนการสำคัญให้ต่อเนื่อง |
| **Disaster Recovery (DR)** | กู้คืนระบบ IT / infrastructure หลังเหตุ |
| **Incident Response (IR)** | ตรวจจับ จำกัด กำจัด กู้คืน และเรียนรู้ |

**ลำดับ IR ที่พบบ่อย**
1. Preparation
2. Detection & Analysis
3. Containment
4. Eradication
5. Recovery
6. Lessons learned

**จำสั้น:** BC = ธุรกิจต่อ · DR = ระบบกลับ · IR = จัดการเหตุการณ์

## 5) Domain 3 — Access Controls (22%)

### Physical
- Badge / gate entry / environmental design
- Guards, CCTV, alarms, logs
- แยก authorized vs unauthorized

### Logical
- **Least Privilege (PoLP)** — สิทธิ์ขั้นต่ำที่จำเป็น
- **Segregation of Duties (SoD)** — แยกหน้าที่สำคัญ
- **DAC** — เจ้าของกำหนดสิทธิ์
- **MAC** — ระบบบังคับตาม label/clearance
- **RBAC** — สิทธิ์ตามบทบาท (role)

## 6) Domain 4 — Network Security (24%)

### พื้นฐานเครือข่าย
- **OSI 7 ชั้น:** Physical → Data Link → Network → Transport → Session → Presentation → Application
- **TCP/IP:** Link / Internet / Transport / Application
- IPv4, IPv6, Wi‑Fi, ports, applications

### พอร์ตควรจำ
| บริการ | พอร์ต |
|--------|-------|
| SSH | 22 |
| DNS | 53 |
| HTTP | 80 |
| HTTPS | **443** |
| RDP | 3389 |

### Threats / Detection / Prevention
- Threats: DDoS, virus, worm, Trojan, MITM, side-channel
- Detect: IDS, HIDS, NIDS
- Prevent: antivirus, scans, firewalls, IPS

### Infrastructure & design
- On-prem: power, HVAC, fire suppression, redundancy, MOU/MOA
- Segmentation: **DMZ**, VLAN, VPN, micro-segmentation
- **Defense in Depth**, NAC, IoT/embedded
- Cloud: SaaS / PaaS / IaaS / hybrid · SLA · MSP

**Shared responsibility สั้นๆ**
- SaaS → ผู้ให้บริการดูแลเกือบทั้งหมด
- PaaS → ผู้ใช้ดูแลแอป
- IaaS → ผู้ใช้ดูแล OS + แอป

## 7) Domain 5 — Security Operations (18%)

### Data security
- Encryption: symmetric (กุญแจเดียว) / asymmetric (คู่กุญแจ)
- Hashing: one-way สำหรับ integrity / เก็บรหัสผ่าน
- Handling: classification, labeling, retention, destruction
- Logging & monitoring

### Hardening
- Baselines · updates · patches · configuration management

### Policies ที่พบบ่อย
- Data handling · Password · **AUP** · BYOD · Change management · Privacy
- Change management ควรมี documentation / approval / rollback

### Awareness
- ลดความเสี่ยงจากคน: phishing, social engineering, password protection

## 8) โดเมนใหม่ตั้งแต่ 1 ก.ย. 2026

| Domain | น้ำหนัก |
|--------|---------|
| Security Principles | 24% |
| Security Governance | 17.3% |
| IAM Concepts | 20% |
| Networking and Cloud Security Concepts | 21.3% |
| Security Operations and Incident Response | 17.3% |

เนื้อหาส่วนใหญ่ยังทับซ้อน — แค่จัดกลุ่มใหม่ (Governance / IAM / Cloud / รวม IR เข้า Operations)

## 9) แผนจำเร็วก่อนสอบ

1. ท่อง CIA + AAA + ethics 4 ข้อ
2. แยก BC / DR / IR ให้ชัด + ลำดับ IR
3. PoLP, SoD, DAC/MAC/RBAC
4. OSI + พอร์ตสำคัญ + IDS vs IPS + DMZ
5. Symmetric vs asymmetric vs hash + นโยบาย Domain 5
6. ทำ quiz แล้ววนจุดที่ผิดด้วย flashcards

## 10) วิธีใช้คู่กับไฟล์อื่น

1. อ่านหน้านี้ (`summary.html`) ก่อน
2. เปิด `mindmap.html` ดูโครงโดเมน
3. ท่อง `flashcards.html`
4. ทดสอบ `quiz.html`
5. กลับมาอ่านจุดอ่อนในหน้านี้ซ้ำ
