# INCIDENT REPORT FORM
---

## Incident Title: Unauthorized File Access and Modification
##  Reported By: Jake
## Date & Time of Detection: 2025-04-22 at approximately 8:50am.
## Affected User(s): Jake

---

## Description of the Incident: 
- On 2025-04-22, Jake reported that his file project.docx was modified without his knowledge before he logged in the morning. He claimed he did not access the file during the night.

## Suspicious Findings from Logs: 
- Log analysis revealed:
  - A login from Jake’s IP; 192.168.1.12 at 1:03:12 on 2025-04-22 which was off working hours.
  - Login from unfamiliar IP 198.51.100.7 at 2025-04-22 02:14:03, unlike Jake’s likely IP 192.168.1.12. (Private IP) and without a logout.
  - Jake logged in at 08:42:21 on 2025-04-22
  - File /user_folders/jake/project.docx modified at 2025-04-22 08:43:03, which Jake denies performing just a minute after logging in which means there was a log-in session running from an unfamiliar IP.
  - Jake accessed his file at 08:45:30 and realized the file had been modified.

## Containment Actions Taken:
- Jake’s account was temporarily disabled to prevent further unauthorized access.

## Eradication Steps:
- Password reset for Jake’s account
- Enabling Multi-Factor Authentication for Jake’s account
- Conducted malware scan on Jake’s device and computers connected to it.
- Blocked IP 198.51.100.7 at the firewall.

## Recovery Process:
- Re-enabled Jake’s account with new credentials and enabled enhanced monitoring for suspicious activities
- Restored /user_folders/jake/project.docx from a clean backup.

## Lessons Learned / Prevention Plan:
- Implement Multi-Factor Authentication for all user accounts to enhance security.
- Deploy an Intrusion Detection/Prevention System for real-time detection of suspicious logins and file changes.
- Conduct regular user training on phishing attempts.
- Encourage security practices like using a password manager and employees must not use the “Keep me signed-in” policy on their browsers.

## Submitted by: Group 1 Incident Response Team   Date: 2025-04-22


