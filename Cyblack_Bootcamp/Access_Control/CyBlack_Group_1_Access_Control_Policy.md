**ACCESS CONTROL POLICY**

**Purpose**

This Access Control Policy establishes a framework for managing
unauthorized access to organizational information systems, data, and
facilities, ensuring compliance with ISO 27001:2022. It enforces the
principle of Least Privilege to protect confidentiality, integrity, and
availability, addressing incidents such as unauthorized access to user
accounts or restricted areas in the organization.

**Scope**

This policy applies to all employees and third parties processing,
storing, or transmitting organizational data. It covers logical access
and physical access.

**Definitions**

- Access Control: Processes to grant, restrict, or revoke access to
  resources.

- Principle of Least Privilege: Granting only the minimum access
  required for job functions.

- Privileged Account: Accounts with elevated permissions.

**Roles and Responsibilities**

HR Manager: Registers new users, informs IT of staff onboarding and
exits to enable or disable access, and ensures only authorized personnel
have access to sensitive areas like the HR department.

IT Team: Implements RBAC, MFA, endpoint protection, and maintains access
logs.

**Policy**

**Access Control Rules (A.5.15, A.8.3)**

- Access to systems and physical areas is granted based on job roles
  using role-based access control.

- Segregation of duties is enforced to prevent single individuals from
  controlling critical processes.

- Access to sensitive data is restricted to authorized roles to prevent
  unauthorized disclosure.

**User Access Management (A.5.16, A.5.18)**

- Access rights are aligned with job roles (Marketing staff access
  Marketing_Campaigns only).

- Access rights are reviewed every 6 months to identify and revoke
  unnecessary permissions.

- Upon termination, access is disabled within 4 hours; role changes
  trigger access adjustments within 1 business day. Return of assets is
  essential.

**Authentication and Password Policy (A.5.17, A.8.5)**

- Passwords must be at least 12 characters, including uppercase,
  lowercase, numbers, and special characters.

- Passwords must be changed every 90 days.

- Multi-factor authentication (MFA) is mandatory for access to systems
  handling sensitive data.

**Privileged Access Management (A.8.2)**

- Privileged accounts require approval from the Information Security
  Team.

- Privileged actions are logged and reviewed weekly for anomalies.

- Privileged access is limited to essential personnel and revoked when
  no longer needed.

**Physical Access Controls (A.5.15)**

- Access to restricted areas is controlled via keycards or biometric
  systems, limited to authorized roles.

**User Endpoint Protection (A.8.1)**

- All endpoint devices must lock automatically after 5 minutes of
  inactivity.

**Data Leakage Prevention (A.8.3)**

- Data loss prevention tools are deployed to monitor and block
  unauthorized data transfers (emailing sensitive HR data).

- Sensitive data is encrypted at rest and in transit to prevent
  unauthorized access.

**Access Logging and Monitoring (A.5.18)**

- All logical and physical access events are logged and retained for 12
  months.

- Logs are reviewed weekly for suspicious activity (unauthorized access
  to HR_Payroll).

- Intrusion detection systems alert on unauthorized access attempts in
  real time.

**Training and Awareness (A.6.3)**

- All employees and third parties must complete annual training on
  access control policies, including recognizing risks like unauthorized
  access to sensitive areas or data.

- Quarterly simulations are conducted to test access control
  effectiveness.

**Compliance**

Non-compliance with this policy, such as granting unauthorized access,
may result in disciplinary action. Annual audits are conducted to ensure
compliance with ISO 27001:2022.

**Review**

This policy is reviewed annually, after significant or, following
updates to ISO 27001:2022, to ensure ongoing effectiveness and alignment
with organizational needs.
