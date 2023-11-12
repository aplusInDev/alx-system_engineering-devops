## Postmoterm project

Issue Summary
On March 15, 2023, our app experienced a complete outage that lasted for about five hours, from 9:00 am UTC to 2:00 pm UTC. The outage was caused by a human error that resulted in dropping the production database. The impact was that all customers were unable to access the app during the outage. The issue was resolved by restoring the database from a backup and applying data recovery procedures.

Timeline
- 9:30 am UTC: Operations staff reported that customers and internal users could not access the app. They also noticed that the production database was empty.
- 9:45 am UTC: Engineering team started to investigate the issue and tried to reproduce it by making database queries and testing the app functionality. They confirmed that the production database had no data and suspected a malicious attack.
- 10:15 am UTC: An emergency alert was sent on Slack and the engineering team joined a conference call to discuss the situation and coordinate the response.
- 10:45 am UTC: A senior engineer who had root access to the database realized that he had accidentally dropped the database while setting up his local environment using the production credentials. He informed the engineering team leader about his mistake and apologized for the incident.
- 11:00 am UTC: The engineering team leader escalated the issue to the senior management and informed them about the root cause and the estimated time to restore the service.
- 11:30 am UTC: The engineering team restored the database from the latest backup that was stored on a replica server. They verified that the backup data was consistent and complete.
- 12:00 pm UTC: The engineering team migrated the backup data to the main production database and restarted the app. They performed several tests to ensure that the app was working as expected and that no data was lost or corrupted.
- 12:30 pm UTC: The engineering team notified the operations staff and the senior management that the service was restored and that the app was fully functional.
- 1:00 pm UTC: The operations staff confirmed that the customers and internal users could access the app without any issues. They also sent an email to the customers to apologize for the inconvenience and explain the cause and resolution of the outage.
- 2:00 pm UTC: The engineering team conducted a postmortem meeting to review the incident and identify the corrective and preventive measures to avoid similar incidents in the future.

Root Cause and Resolution
The root cause of the outage was a human error that resulted in dropping the production database. The resolution was to restore the database from a backup and recover any data that was affected by the outage.

Corrective and Preventive Measures
To prevent this incident from happening again, the engineering team implemented the following measures:

- Changed the root user password and restricted the access to the production database to only authorized personnel.
- Created individual database users for each team member and assigned them appropriate privileges based on their roles and responsibilities. Disabled the delete and write privileges for the junior team members.
- Implemented a database audit system to monitor and log all the database activities and alert the engineering team leader in case of any suspicious or unauthorized actions.
- Implemented a database backup system to create regular and frequent backups of the production database and store them on a separate server.