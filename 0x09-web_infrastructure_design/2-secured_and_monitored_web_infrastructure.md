Designing the Secured and Monitored Web Infrastructure:
Explanation for Each Element Added:

Three Servers: To ensure redundancy, high availability, and load distribution.
Firewalls (3): To add multiple layers of security and control incoming/outgoing traffic.
SSL Certificate: To enable HTTPS, encrypting data transmitted between users and the web server.
Monitoring Clients (3): To collect data on server performance, availability, and potential issues.
Firewalls: Firewalls are added to restrict unauthorized access, prevent malicious attacks, and control the flow of traffic. They act as barriers between the internal network and the external world.

HTTPS Traffic: Serving traffic over HTTPS encrypts data transmitted between users and the server, enhancing security and protecting sensitive information from being intercepted.

Monitoring: Monitoring tools help track server performance, detect anomalies, and ensure system availability. They provide insights for proactive issue resolution and optimization.

Monitoring Data Collection: Monitoring clients (data collectors) gather performance metrics, log data, and other relevant information from servers and send it to monitoring services like Sumo Logic. This data is then analyzed for insights and alerts.

Monitoring Web Server QPS: To monitor the web server's Queries Per Second (QPS), set up metrics tracking and reporting for incoming HTTP requests. Monitoring tools can generate QPS statistics and alert you if thresholds are breached.

Issues with the Infrastructure:

Terminating SSL at Load Balancer: Terminating SSL at the load balancer exposes the decrypted traffic within the internal network. SSL termination should ideally occur at the application server to maintain end-to-end encryption.
Single MySQL Server for Writes: Relying on a single MySQL server for write operations creates a single point of failure and can lead to data inconsistency. Replicate the MySQL database for redundancy and failover support.
Uniform Server Components: Using identical server components (database, web server, and application server) can lead to resource contention and limited scalability. Different components should be distributed across servers to optimize performance.
By addressing these issues and making the suggested improvements, the web infrastructure can become more secure, resilient, and performant.
