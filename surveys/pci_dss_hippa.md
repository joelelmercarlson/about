# PCI DSS & HIPAA Readiness Assessment for Small Businesses

## 1. Organization Overview
-	Legal business name and DBA
-	Primary business activities
-	Number of employees (full time, part time, contractors)
-	Locations (physical offices, remote workforce, data centers)
-	Key contacts for compliance, IT, and operations

## 2. PCI DSS Scope Identification

### 2.1 Cardholder Data Environment (CDE)
-	Do you store, process, or transmit cardholder data?
-	What payment channels do you use (in person POS, e commerce, phone orders, mobile apps)?
-	Do you store any cardholder data (full PAN, expiration date, CVV)?
-	If stored, where and how (databases, logs, paper, third party systems)?
-	Do you use tokenization or point to point encryption (P2PE)?

### 2.2 Payment Service Providers
-	Which payment processors or gateways do you use (Stripe, Square, PayPal, etc.)?
-	Do you use any third party POS systems?
-	Do you have service provider agreements and Attestations of Compliance (AOC)?

### 2.3 Network & System Architecture
-	Describe your network layout (firewalls, VLANs, segmentation).
-	Are CDE systems segmented from the rest of the network?
-	Do you maintain network diagrams and data flow diagrams?

### 2.4 Policies & Procedures
-	Do you have documented security policies?
-	Do you have an incident response plan?
-	Do you perform annual PCI self assessment questionnaires (SAQ)?
-	Do you conduct quarterly ASV scans or penetration tests?

## 3. HIPAA Scope Identification

### 3.1 PHI Handling
-	Do you create, receive, maintain, or transmit Protected Health Information (PHI)?
-	What types of PHI do you handle (medical records, billing data, patient identifiers)?
-	Where is PHI stored (EHR, cloud storage, email, paper files)?
-	Who has access to PHI internally?

### 3.2 Business Associate Relationships
-	Are you a Covered Entity or a Business Associate?
-	Do you have Business Associate Agreements (BAAs) with all vendors handling PHI?
-	Do you share PHI with third parties (billing, IT, cloud services)?

### 3.3 Administrative Safeguards
-	Do you have a HIPAA Security Officer and Privacy Officer?
-	Do you conduct annual HIPAA risk assessments?
-	Do employees receive HIPAA training?
-	Do you have policies for access control, minimum necessary use, and workforce sanctions?

### 3.4 Technical Safeguards
-	Do you use encryption for PHI at rest and in transit?
-	Do you enforce MFA for systems containing PHI?
-	Do you maintain audit logs and access monitoring?
-	Do you have secure email or secure messaging for PHI transmission?

### 3.5 Physical Safeguards
-	How is physical access to PHI controlled (locked rooms, badge access, cameras)?
-	Do you have workstation security policies?
-	How do you dispose of PHI (shredding, secure wipe, vendor destruction)?

## 4. IT Infrastructure & Security Baseline
-	Inventory of servers, workstations, mobile devices
-	Operating systems and patching practices
-	Antivirus/EDR solutions
-	Backup and disaster recovery processes
-	Cloud services used (Microsoft 365, Google Workspace, AWS, etc.)
-	Remote access methods (VPN, RDP, zero trust tools)

## 5. Current Security Practices
-	Password policy and MFA usage
-	Firewall configuration and change management
-	Vulnerability scanning and patch management
-	Logging and monitoring tools
-	Incident response procedures
-	Employee security awareness training

## 6. Documentation & Evidence Readiness
-	Existing policies and procedures
-	Network diagrams, data flow diagrams
-	Asset inventory
-	Risk assessments (PCI, HIPAA, or general cybersecurity)
-	Prior audit reports or compliance findings

## 7. Business Goals & Constraints
-	Desired certification timeline
-	Budget constraints
-	Internal resource availability
-	Appetite for outsourcing vs. in house remediation
-	Planned technology changes (new POS, EHR migration, cloud adoption)
