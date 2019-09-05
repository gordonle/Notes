CS348 L01 | September 05, 2019

==Data==: A representation of **facts**, **concepts**, and **instructions** in a formalized manner suitable for communication, interpretation, or processing by humans or by automatic means. Any representation such as characters or analog quantities to which **meaning is or might be assigned**. Generally, we perform operations on data or data items to supply some **information about an entity**. 

In this course, we are mainly concerned with **persistent data**. 

## Early Data Management

Previously, data was stored on magnetic tapes, and each program had its own data set. This means high data redundancy. More recently, we’ve been storing data in files located on disk drives with a file system interface between programs and files. There are now various access methods (ie. sequential, indexed, randomized), and now each file can be used by multiple programs. 

# Databases

==Database==: A *large* and *persistent* collection of factual data and metadata organized in a way that facilitates efficient *retrieval* and *revision*

==Factual Data==: John’s age is 42. He works in the IT department.

==Metadata==: There is a concept of an employee that has a name, age, and department. 

==Data Model==: determines the nature of the metadata and how retrieval and revision is expressed (ie. file cabinets, libraries, inventory control system)

==Database Management System (DBMS)==: A program (or set of programs) that implements the data model.

The idea here is to abstract common functions and create a uniform, well-defined interface for applications that require a database. Each DBMS should:

- support an **underlying data model** (data stored in well-defined and organized way)
- have **access control** (authorized access to various data)
- have **concurrency control** (multiple simultaneous accesses to data)
- have **database recovery** (reliability)
- be **well-maintained** (ie. revising metadata)

Things like inventory control, payroll, banking and reservation systems all use DBMSs. More recently, e-commerce, telecom systems and other new technologies have been using databases as well. 

## Schema and Instances

==Schema==: a collection of metadata conforming to an underlying data model

==Instance==: a collection of factual data, as defined by a given database schema

A schema can and typically does have many possible database instances

### Three Level Schema Architecture 

1. **External schema (view)**: what the application program and user see. This may differ for different users of the same database.
2. **Conceptual schema**: describes the logical structure of *all* data in a database
3. **Physical schema**: description of physical aspects (selection of files, devices, storage algorithms, etc.)

## Data Independence

The idea here is that applications don’t access data directly, but instead through an abstract data model provided by the DBMS. There are two kinds of data independence:

- **Physical**: applications immune to changes in storage structures
- **Logical**: modularity! (ie.  $A$ cannot be accessed by $B$ )

This is one of the ***most important reasons*** we use a DBMS.

## Transactions

==Transaction==: An application-specified atomic and durable unit of work.

A DBMS should ensure these properties with all its transactions:

- <u>**A**</u>tomic: a transaction will either occur in its entirety, or not at all
- <u>**C**</u>onsistency: each transaction preserves the consistency of the database
- <u>**I**</u>solated: concurrent transactions do not interfere with each other
- <u>**D**</u>urable: once completed, a transaction’s changes are permanent

## Interfacing with the DBMS

==Data Definition Language (DDL)==: specifies schemas. We may have different DDLs for external, conceptual and physical schemas

==Data Manipulation Language (DML)==: specifies retrieval and revision requests. It can be **navigational** (procedural) or **non-navigational** (declarative)

# Database Users

| Type                         | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| End Users                    | Accesses the database indirectly through forms or other query-generating applications, or generates ad-hoc queries using the DML |
| Application Developers       | Designs and implements applications that access the database |
| Database Administrator (DBA) | Manages the conceptual schema, assists with application view integration, monitors performance, defines internal schema, loads and reformats DB,  responsible for security and reliability |



