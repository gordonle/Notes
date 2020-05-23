Chapter 2: Application Layer (pg 112)

# 2.1 Principles of Network Applications

Application development is writing programs that run on different hosts, and then communicate over the network. A Web application has a browser program running locally, and the server program running in the server host. 

When developing a new application, written software will run on multiple hosts. Software does not need to be written for network-core devices (eg. routers) since these function at lower layers. Application software is confined to the end systems.

The **application architechture** is designed by the app developer and dictates how the application is structured over various end systems. There are two popular paradigms used in modern day: client-server or peer-to-peer (P2P).

**Client-server Architecture**: always-on host, called the *server*, which services requests from many other hosts, called *clients*. Clients do not directly communicate. The server has a fixed, well-known IP address. Often a single-server host can't manage all the traffic, so **data centers** were introduced to manage load. They can house hundreds of thousands of servers. 

**P2P Architecture**: minimal (or no) relliance on dedicated servers. Instead, these apps exploit direct communication between pairs of intermittently connected hosts, called **peers**. These peers are not owned by the service provider, but are instead hosts controlled by users. File sharing services and video conferencing use P2P. A very compelling feature is the **self-scalability** here. The most peers you have, the larger your system capacity. There are struggles with security, performance and reliability, though. 

There exist hybrid architectures as well, like for messaging there's a IP address of users but user-to-user messaging can be done directly between hosts.

### Processes Communicating

It's not the programs but the **processes** running within end systems that communicate. When running on the same host, they can have interprocess communication, but on different hosts, they exchange **messages** across the computer network. 

Clients are the one requesting information or downloading, servers wait to be contacted.

A process sends messages into, and receives messages from, the network througha. software interface called a **socket**. The socket is the interface between the application layer and the transport layer. It exists within a host, and is also referred to as the **Application Programming Interface (API)** between the app and the network. It's the programming interface with which network apps are built. 

To identify the receiving process, we need

1. the address of the host, and
2. an identifier that specifies the receiving process in the destination host

In the Internet, the host is identified by its IP address (32-bit). The sending process needs to know both the host IP address and the process that is receiving it (receiving socket) running in the host. This purpose is fulfilled by the **port number**. 

### Transport Services Available to Applications

Each application chooses the transport service that it'll use. There are four dimensions.

#### Reliable Data Transfer

Avoids packet loss. If a protocol provides guaranteed data delivery services, it's said to provide reliable data transfer. When a transport-layer protocol doesn't provide this, some data sent might never arrive at the receiving process. This may be okay for **loss-tolerant applications** like audio/video calls.

#### Throughput

Guaranteed available throughput at some specified rate. This service would appeal to applications that require specific bandwidths. These are known as **bandwidth-sensitive applications**, such as video players. **Elastic applications** are the opposite; they don't have any throughput requirements.

#### Timing

Timing guarantees. For example, every bit that the sender pumps inot the socket arrives at the receiver's socket no more than 100 msec later. This would appeal to real-time applications such as video games.

#### Security

Security services can include data encryption/decryption, data integrity, end-point authentication, etc. 

### Transport Services Provided by the Internet

#### TCP Services

This service model is **connection-oriented** and a **reliable data transfer** service. Connection is guaranteed through a *handshaking procedure* that occurs before application-level messages are sent, where the client and server are both alerted. This allows them to prepare for the incoming packets, during which a **TCP connection** is said to exist between sockets.

It also includes a congestion-control mechanism that throttles a sending process when the network has heavy traffic. It also attempts to limit each TCP connection to its fair share of network bandwidth.

#### UDP Services

Super lightweight, minimal services. Connectionless, so there's no handshaking. Many firewalls actually will be configured to block most types of UDP traffic.

### Application-Layer Protocols

An **application-layer protocol** defines how an application's processes, running on different end systems, pass messages to each other. In particular, and application-layer protocol defines:

- types of messages exchanged (eg. request and response messages)
- syntax of the message types (ie. the fields and formatting)
- semantics of fields (ie. the meaning of the information)
- rules that determine when and how a process sends/responds to messages 

Examples of this is HTTP, the Web's application-layer protocol.

The distinction between network applications and application-layer protocols is important. An application-layer protocol is only one piece of a network application). 

# 2.2 The Web and HTTP (pg 129)



# 2.3 E-Mail in the Internet (pg 149)