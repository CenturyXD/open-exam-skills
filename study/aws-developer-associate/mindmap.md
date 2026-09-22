# AWS Certified Developer – Associate (DVA-C02)

## ภาพรวมข้อสอบ

### รูปแบบ
#### 65 ข้อ / 130 นาที
#### คะแนนผ่าน 720/1000
#### Multiple choice และ multiple response
#### ค่าธรรมเนียม USD 150

### Domain weights
#### Development with AWS Services 32%
#### Security 26%
#### Deployment 24%
#### Troubleshooting and Optimization 18%

### ไทม์ไลน์เวอร์ชัน
#### DVA-C02 สอบได้ถึง 30 พ.ย. 2026
#### DVA-C03 GA 1 ธ.ค. 2026

## Domain 1 Development with AWS Services 32%

### พัฒนาด้วย AWS SDK และ CLI
#### Credential providers และ profiles
#### Pagination และ retries ใน SDK
#### Service quotas และ throttling
#### Idempotency ใน API calls

### AWS Lambda
#### Runtime handler memory timeout concurrency
#### Environment variables และ layers
#### Event source mapping (SQS Kinesis DynamoDB Streams)
#### Sync vs async invocation
#### Destinations และ dead-letter queues
#### VPC access กับ NAT Gateway
#### Provisioned concurrency และ cold starts

### ร้านข้อมูลและ persistence
#### DynamoDB partition sort key
#### Query vs Scan
#### GSI และ LSI
#### Eventually vs strongly consistent reads
#### DynamoDB Streams และ TTL
#### S3 storage classes และ lifecycle
#### ElastiCache / DAX สำหรับ caching
#### RDS และ Aurora จากมุมมองแอป

### Integration และ event-driven
#### API Gateway REST HTTP WebSocket
#### Amazon SQS standard vs FIFO
#### Amazon SNS fan-out
#### EventBridge rules และ buses
#### Step Functions orchestration
#### S3 event notifications

## Domain 2 Security 26%

### IAM สำหรับแอป
#### Users groups roles policies
#### Least privilege
#### Trust policy vs permissions policy
#### Resource-based policies
#### STS AssumeRole และ temporary credentials

### Authentication และ authorization ของผู้ใช้แอป
#### Amazon Cognito user pools
#### Cognito identity pools / federated identities
#### JWT และ API Gateway authorizers
#### OIDC / SAML federation basics

### ข้อมูลลับและการเข้ารหัส
#### Secrets Manager (rotation)
#### Systems Manager Parameter Store (SecureString)
#### AWS KMS CMK และ data keys
#### Encryption at rest และ in transit
#### S3 bucket policies และ encryption

### Application security
#### AWS WAF กับ API Gateway / CloudFront
#### ACM certificates
#### ไม่ hardcode credentials ในโค้ด

## Domain 3 Deployment 24%

### CI/CD บน AWS
#### CodeCommit / Git source
#### CodeBuild buildspec
#### CodePipeline stages และ approvals
#### CodeDeploy AppSpec
#### CodeArtifact สำหรับ packages

### Infrastructure as Code
#### CloudFormation stacks และ change sets
#### AWS SAM สำหรับ serverless
#### AWS CDK constructs และ synth
#### Nested stacks และ parameters / outputs

### กลยุทธ์การ deploy
#### All-at-once rolling
#### Blue/green
#### Canary และ linear (Lambda aliases)
#### Elastic Beanstalk environments
#### ECS / container deploy basics
#### API Gateway stages และ canary releases
#### Rollback และ traffic shifting

### Packaging และ config
#### Lambda zip vs container image
#### AppConfig สำหรับ feature flags
#### Environment-specific configuration

## Domain 4 Troubleshooting and Optimization 18%

### Observability
#### CloudWatch Logs Metrics Alarms
#### Embedded metrics และ custom metrics
#### AWS X-Ray tracing และ service map
#### CloudTrail สำหรับ API activity
#### Structured logging ในแอป

### แก้ปัญหา runtime
#### Lambda timeout memory throttling
#### DynamoDB throttling และ hot partitions
#### SQS visibility timeout และ poison messages
#### API Gateway 4xx vs 5xx
#### Permission / CORS errors

### Optimization
#### Lambda memory-CPU tradeoff
#### DynamoDB capacity on-demand vs provisioned
#### Caching strategies (lazy loading write-through)
#### S3 Transfer Acceleration / multipart
#### Cost-aware design สำหรับนักพัฒนา

## บริการที่ควรเน้นเป็นพิเศษ

### ต้องชำนาญ
#### Lambda
#### DynamoDB
#### IAM
#### API Gateway
#### S3
#### SQS SNS EventBridge
#### CodePipeline CodeBuild CodeDeploy
#### CloudWatch X-Ray
#### Cognito KMS Secrets Manager

### รู้พอใช้
#### Elastic Beanstalk
#### CloudFormation SAM CDK
#### ElastiCache / DAX
#### Step Functions
#### ECS / ECR basics
#### Amazon Q Developer (หัวข้อใหม่ใน outline)

## แผนอ่านแนะนำ

### เฟส 1 พื้นฐาน
#### อ่าน Exam Guide ทั้งฉบับ
#### Hands-on Lambda + DynamoDB + IAM
#### ท่อง flashcards Domain 1–2

### เฟส 2 Deploy และ debug
#### สร้าง pipeline เล็ก ๆ ด้วย CodePipeline
#### ฝึก X-Ray และ CloudWatch
#### ทบทวน deployment strategies

### เฟส 3 จำลองสอบ
#### Official Practice Question Set
#### Tutorials Dojo / practice exams
#### ทบทวนข้อที่ผิดเป็นชุด flashcards ใหม่
