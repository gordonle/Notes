Chapter 1: Computer Networks and the Internet (pg 26)

## 1.1 What is the Internet (pg 27)

Vocabulary

- **host / end system**: devices that connect to the Internet
    - e.g. computers, phones, traffic control systems
- **communication links**: connect end systems together
    - e.g. optical fiber, radio spectrum
- **transmission rate**: the rate at which a type of link can transmit data (bits/second)
- **packet**: package of information sent between systems
- **packet switch**: takes an arriving packet and forwards it onto an outgoing link
    - e.g. routers (network core), link-layer switches (access networks)
- **Internet Service Providers (ISPs)**: provide end systems with Internet access, it's a network of packet switches and comm. links. 
    - e.g. AT&T, Rogers, Bell
- **protocol**:  the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event
    - e.g. **Transmission Control Protocol (TCP)**, **Internet Protocol (IP)**
- **socket interface**: specifies how a program running on one end system asks the Internet infrastructure to deliver data to a specific destination program running on another end system

## 1.2 The Network Edge (pg 36)

Hosts can be divided into **clients** and **servers**. Clients tend to be desktop/mobile PCs, smartphones, etc. while servers tend to be larger, more powerful machines that stores and distribute Web pages, stream video, etc. Servers mostly reside in data centers.

The **access network** is the network that physically connects a host to the first route (edge router) on a path from the host to any other distant host.

Two most prevalent types of broadband residential access are **digital subscriber line (DSL)** and **cable**. Consumers that use DSL also have their telephone company as their ISP. At the local central office, they have **digital subscriber line access multiplexers (DSLAMs)** that then connect you to the Internet.

When upstream and downstream transmission rates are different, the access is said to be *asymmetric*.

#### Twisted-pair copper wire

Least expensive and most commonly used **guided transmission** (wired) medium. A wire pair is composed of two insulated copper wires ~1mm thick, arranged in a regular spiral pattern and consititutes a single communication link. **Unshielded twisted pair (UTP)** is commonly used for computer networks within a building (LANs). It's the optimal solution for high-speed LAN networking.

#### Coaxial Cable

Also two copper conductors, but they are concentric rather than parallel. Common in cable television systems. It can be used as a guided **shared medium**, so a number of hosts can be connected directly to the cable, with each of the hosts receiving whatever is sent by the other hosts.

#### Fiber Optics

Thin and flexible, conducts pulses of light (each pulse represents a bit). Can support very high bit rates. Immune to electromagnetic interference, very low signal attenuation, and very difficult to tap. Thus they are the preferred long distance guided transmission media, especially for overseas links. Optical devices can be quite expensive though.

#### Terrestrial Radio Channels

Radio channels carry signals int he electromagnetic spectrum. Environmental considerations determine **path loss and shadow fading** (decreases signal strength due to obstructive objects), **multipath fading** (signal reflection off of interfering objects) and **interference** from other transmissions/electromagnetic signals. 

Are usually split into three groups, based on the distance that they travel, from short distance, to local area, to wide area. 

#### Satellite Radio Channels

A communication satellite links two or more Earth-based microwave transmitter/receivers, known as **ground stations**. Two types of satellites used: **geostationary satellites** and **low-earth orbiting (LEO) satellites**.

Geostationary permanently remain above the same spot on Earth, so it's in orbit at 36000 km above the surface. LEO satellites are much closer, but not not stay in the same spot, They rotate and communicate with each other.

## 1.3 The Network Core (pg 49)

The "mesh of packet swithces and links that interconnects the Internet's end systems". 

### Packet Switching 

Messages sent between hosts are broken up into *packets*, and between the source and destination, each packet travels through communication links and packet switches. 

#### Store-and-Forward Transmission

Most use this at the inputs to the links. It means that the packet switch must receive the entire packet before it can begin to transmit the first bit of the packet onto an outbound link. Let's say that each packet consists of $L$ bits, with transmission rate of $R$ bps.

The source begins to transmit at time 0. At time $L/R$ seconds, the source has transmitted the entire packet, and the entire packet has been received and stored at the router (no propagation delay). At time $L/R$, the router can begin to transmit the packet onto the outbound link. At $2L/R$, the router has completed transmitting, and destination has received it. Total delay $= 2L/R$. For all three packets to arrive, it would take $4L/R$ delay. If the packet switch forwarded immediately instead of waiting for the full packet, then total delay would be $L/R$ per packet since bits weren't held up at the router. 

#### Queueing Delays and Packet Loss

Each packet switch has multiple links. For each link, the switch has an **output buffer** (queue) which stores packets that the router is waiting to send out onto the link. Thus in addition to store-and-forward delays, packets suffer from output buffer **queuing delays**. These depend on level of congestion in the network. 

If the buffer is full, **packet loss** occurs where either the arriving or a queued packet will be dropped.

#### Forwarding Tables and Routing Protocols

Based on the computer network, there are different routing protocols. For the Internet, every host has an IP address included in the header of a packet. Each router has a **forwarding table** that maps destination addresses to certain outbound links. These tables are automatically set by a number of special **routing protocols**. 

### Circuit Switching

In circuit-switched networks, the resources needed along a path (buffers, link transmission rate) are *reserved* for the duration of the communication session between hosts. This is basically making reservations at a restaurant, vs first-come-first-serve with packet switching. 

This is useful when you need to maintain connection between two hosts, like for phone calls. This maintained connection state is called a **circuit**. Once established, it also reserves a constant transmission rate for the duration of the connection. 

#### Multiplexing in Circuit-Switched Networks

A circuit in a link is implemented with either **frequency-division multiplexing (FDM)** or **time-division multiplexing (TDM)**. With FDM, the frequency spectrum of a link is divided among the connections established across the link. Specifically, the link dedicates a frequency band to each connection. The width of the band is known as **bandwidth**. For TDM, time is divided into frames of fixed-duration, and each frame is divided into a fixed number of time slots. Each time slot gets assigned to a connection.

FDM $\to$ each circuit continuously gets a fraction of bandwidth

TDM $\to$ each circuit gets all bandwidth for brief intervals

Circuit switching can be wasteful, because dedicated circuits are idle during **silent periods** (no data being transmitted). It also requires complex signaling software for coodination, making it more complicated. 

> File to send: 640000 bits from A to B on a circuit-switched network.
>
> All links use TDM with 24 slots and have a bit rate of 1.536 Mbps. It takes 500ms to establish an end-to-end circuit. How long does it take to send the file?
>
> Transmission rate of each circuit = (bit rate) / (# of slots) = 64 kbps, so it takes 640000 bits/64 kbps = 10s to transmit. Add circuit establish time for 10.5s tos end. 

### Packet VS Circuit Switching

Packet Switch

|                       | Packet Switch                        | Circuit Switch                                        |
| --------------------- | ------------------------------------ | ----------------------------------------------------- |
| Delay                 | variable, unpredictable, packet loss | continuous circuit guarantees, initial setup required |
| Transmission Capacity | Better                               | Not as good                                           |
| Complexity            | Simpler, more efficient to set up    | Complicated, more costly to set up                    |

In a situation where users are likely to remain idle, packet switch trumps circuit switch since it can support many more users. Also, if there's one user who wants to transmit a lot of data and no other users, packet switch allows them to send at a continuous rate, whereas circuit with TDM would take (# of time slots) times as much time.

So packet switching tends to be more popular, even for things like telephones.

### Network of Networks

The Internet is made up of billions of end systems, and they are all connected on a number of tiers of ISPs. Regional ISPs connect to one of many global ISPs, which are all interconnected themselves. Tier-1 ISPs (actually global) exist, but aren't available everywhere.

A **point of presence** is a group of routers (at the same location) in the provider's network where customer ISPs can connect into the provider ISP. Customer ISPs that connect to two or more provider ISPs are called **multi-homed**.

When two ISPs **peer**, they directly connect their networks so that all the traffic between them passes over a direction connection, rather than through upstream intermediaries. An **Internet Exchange Point (IXP)** is a meeting point where multiple ISPs can peer together. 

*Network Structure 4* refers to all these; access ISPs, regional ISPs, tier-1 ISPs, PoPs, multi-homing, peering, and IXPs.

Today's Internet though is described by ***Network Structure 5***. It builds on top of NS4 by adding **content-provider networks** (ie. datacenters). Google has data centers all over the world that are interconnected via Google's private TCP/IP network. It bypasses the upper tiers of Internet by peering with lower-tier ISPs. By creating it's own network, a content provider not only reduces payments to upper-tier ISPs, but also retains greater control of how its services are delivered to end users. 

## 1.4 Delay, Loss, and Throughput in Packet-Switched Networks (pg 62)

### Delays

Types of delay include **nodal processing delay**, **queuing delay**, **transmission delay**, and **propagation delay**; these accumulated results in the **total nodal delay**. 

**Processing Delay**: time required to examine packet header and to determine where to direct the packet, can include bit-level error checks

**Queuing Delay**: waiting in buffer to be transmitted onto the link. If buffer is empty, this is 0

**Transmission Delay**: length of packet as $L$ bits, transmission rate of link from router A to B as $R$ bits/sec, then transmission delay is equal to $\frac LR$. It's the amount of time to push (transmit) all the packet's bits into the link (not related to distance between A and B)

**Propagation Delay**: time taken to propagate from A to B, depends on propagation speed of the link and the travel distance needed

#### Queuing Delay

This is the only one that varies from packet to packet. Thus, statistical mesures such as *average queuing delay* *variance of queuing delay*, and the *probability that queuing delay > some value* are used.

Let $a$ denote average rate at which packets arrive in the queue per second. $R$ is transmission rate in bits/sec, and packet size is $L$ bits. Then the average rate at which bits arrive at the queue is $La$ bits/sec. If the queue is infinitely long, the ratio $\frac{La}R$ is called **traffic intensity**. If $\frac{La}R >1$, then the average rate at which bits arrive at the queue exceeds the rate at which the bits can be transmitted. Then the queue will increase without bound and the queuing delay will tend to infinity! **Therefore it should always be less than 1.**

If $\frac{La}R\le 1$, then we need to consider the nature of the arriving traffic. If packets arrive periodically (e.g. one per $\frac LR$ sec), then there is no queuing delay. But if they arrive in bursts, then there will be a queuing delay. If $N$ packets arrive simultaneously every $\frac{\frac LR}N$ second, then the first packet has no queuing delay, the next one has queuing delay of $\frac LR$, and the $n$th packet will have a delay of $(n-1)\frac LR$ seconds. Thus average queuing delay is $(\frac n2) \frac LR$ seconds.

Typically, arrival of packets is *random*.

#### Packet Loss

Queues are finite, and once a packet arrives at a full queue, the router will be forced to **drop** the packet. The packet is now **lost**. Performance at a node is also measured in terms of *probability of a packet loss*. A lost packet can be retransmitted on end-to-end basis.

#### End-to-End Delay

This is the total delay from source to destination (can include multiple routers). Consider $n-1$ routers between source host and destination host. Suppose queuing delays are negligible, processing delay is $d_{proc}$, transmission rate is $R$ bits/sec, propagation on each link is $d_{prop}$. If $d_{trans}=\frac LR$, then  $d_{end-to-end}=n(d_{proc} + d_{trans} + d_{prop})$. This doesn't include average queuing delay.

There can also be other delays, like purposeful delays and packetization delay for Voice-over-IP applications.

### Throughput in Computer Networks

The **instantaneous throughput** at any instant of time is the rate (in bits/sec) at which the destination host is receiving the file. If a file has size $F$ bits, transfer takes $T$ seconds for destination to receive all $F$ bits, then the **average throughput** of the transfer is $\frac FT$ bits/sec.

The **end-to-end throughput** is the slowest transmission rate amonst all the links involved. If a single link is used for multiple different transfers, the transmission rate can be bottlenecked there.

## 1.5 Protocol Layers & Their Service Models (pg 75)

### Protocol Layering

To provide structure to the design of network protocols, designers organize them in **layers**. Each layer offers a number of **services** to the layer above - called the **sevice model** of a layer. A layer performs certain actions within itself and uses the services of the layer below it.

Advantages to this include *modularity*, but disadvantages include redundant functionality or inaccessible information.

The procotols of the various layers are called the **protocol stack**. The Internet protocol stack consists of five layers: 

1. Application (top of stack)
2. Transport
3. Network
4. Link
5. Physical (bottom of stack)

#### Application Layer

Where network applications and their application-layer protocols reside (e.g. HTTP, SMTP, FTP). Translation from network addresses to readable human-friendly addresses is here too (DNS). It's distributed over multiple end systems, with applications in different end systems using protocols to exchange packets (called **messages**).

#### Transport Layer

Transports **messages** between application endpoints. In the Internet, there are two transport protocols: TCP and UDP. TCP provides connection-oriented service, guarantees delivery and breaks long messages into shorter segments. Also has congestion-control mechanism, to throttle transmission rate if network is congested. UDP is connectionless, provides no reliability or anything else. A transport-layer packet is called a **segment**.

#### Network Layer

Network-layer packets are called **datagrams**. Transport-layer protocols in a source host passes a segment and a destinatino to the network layer, who then delivers the segment to the transport layer in the destination host. This layer includes IP protocol, and is often referred to as the IP layer.

#### Link Layer

Routes datagrams through series of routers between source and destination. At each node, the network layer passes the datagram down to the link layer, wchih passes it to the next node in the route. Then it's passed back up to the network layer. Services provided depend on the specific link-layer protocol for that link. Some provide reliable delivery, for example. Examples of link-layer protocols include Ethernet, WiFi, etc. Link-layer packets are called **frames**.

#### Physical Layer

The physical layer moves the individual bits within the frame from one node to the next. Protocols are link dependent and further depend on the actual medium of transmission.

#### OSI Model

Open Systems Interconnection model is the same as the Internet one but with two extra layers. The presentation layer provides services that allow communicating application to interpret the meaning of data exchanged (compression, encryption, description). The sessions layer provides delimiting and synchronization of data exchange (checkpointing, recovery). Application layer sits on top of presentation, which is on top of session.

Circuit switched networks don't have these layers.

### Encapsulation

Not all layers are implemented in packet switches. Routers implement 1-3, link-layer switches only 1-2.

**Encapsulation** occurs as data is passed between layers. Transport-layer segment encapsulates the application-layer message. Together they consitute the segment. At each layer, a packet has two types of fields: a **header field** from the current layer, and a **payload field**, which is the packet from the layer above.

