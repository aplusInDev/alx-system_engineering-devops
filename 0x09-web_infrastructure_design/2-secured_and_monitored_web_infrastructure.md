## Designing a Secure and Monitored Web Infrastructure

**Explanation for Each Added Element:**

- **Three Servers:** These are implemented to ensure redundancy, high availability, and effective load distribution.
- **Firewalls (3):** Multiple firewalls are added to enhance security by controlling both incoming and outgoing traffic.
- **SSL Certificate:** This is used to enable HTTPS, providing encryption for data transmitted between users and the web server.
- **Monitoring Clients (3):** These clients gather data on server performance, availability, and potential issues.

**Firewalls:** Firewalls are integrated to prevent unauthorized access, thwart malicious attacks, and manage traffic flow. They serve as barriers between the internal network and the external environment.

**HTTPS Traffic:** Implementing HTTPS encrypts the data exchanged between users and the server, thus elevating security and safeguarding sensitive information from interception.

**Monitoring:** Monitoring tools play a crucial role in tracking server performance, detecting anomalies, and ensuring the availability of the system. They offer insights for proactive issue resolution and optimization.

**Monitoring Data Collection:** Monitoring clients, acting as data collectors, retrieve performance metrics, log data, and other pertinent information from servers. This data is then transmitted to monitoring services such as Sumo Logic for analysis, yielding insights and alerts.

**Monitoring Web Server QPS:** To keep track of the web server's Queries Per Second (QPS), it's recommended to establish metrics tracking and reporting for incoming HTTP requests. Monitoring tools can generate QPS statistics and trigger alerts when predefined thresholds are exceeded.

**Infrastructure Challenges:**

- **Terminating SSL at Load Balancer:** Terminating SSL at the load balancer exposes decrypted traffic within the internal network. Ideally, SSL termination should occur at the application server to maintain end-to-end encryption.
- **Single MySQL Server for Writes:** Relying on a single MySQL server for write operations creates a single point of failure and can lead to data inconsistency. To mitigate this, consider replicating the MySQL database for redundancy and failover support.
- **Uniform Server Components:** Using identical server components (database, web server, and application server) can result in resource contention and limited scalability. Distributing different components across servers is recommended to optimize performance.

By addressing these challenges and implementing the suggested enhancements, the web infrastructure can achieve higher levels of security, resilience, and performance.

