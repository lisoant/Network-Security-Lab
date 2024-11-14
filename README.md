# Network-Security-Lab
## **Introduction**

This project is a hands-on exploration of network security attacks, illustrating the potential weaknesses in communication protocols and the methods attackers use to exploit these vulnerabilities. By providing scripts and instructions for each task, this repository serves as a learning resource for anyone interested in network security, ethical hacking, and cybersecurity.

## **Project Overview**

Each task in this repository simulates a different type of network attack. These exercises are conducted in a controlled environment using Mininet, a network emulator, and Python scripts. The primary objective is to analyze each attack and understand the techniques used, which can be beneficial in designing effective defense strategies in real-world scenarios.

### **Tasks Overview**

* **ICMP Spoofing Attack**: Simulates packet interception by spoofing ICMP echo requests and replies.  
* **MITM Attack Using ARP Cache Poisoning**: Demonstrates interception of communication by manipulating the ARP cache.  
* **TCP Session Hijacking Attack**: Explores session hijacking by injecting spoofed packets into an active TCP session.

---

## **Prerequisites**

Before you begin, ensure you have the following tools and libraries installed:

* **Python 3.x**: Python programming language.

**Scapy library**: For packet manipulation and crafting.  
```pip install scapy```

* **Mininet**: Network emulator for creating virtual networks.  
* **Virtual Machine (VM) environment** (recommended): To safely test network attacks without affecting live networks.

---

## **Installation**

**Clone this repository** to your local machine:  
```git clone https://github.com/yourusername/network-security-lab.git```  
```cd network-security-lab```

1. **Install dependencies**:

Install Scapy (if not already installed): ```pip install scapy```

2. **Set up Mininet**:  
   * Follow the official Mininet installation guide if you haven't installed it already.

---

## **Tasks**

### **Task 1: ICMP Spoofing Attack**

In this task, you'll learn how to capture and spoof ICMP packets (e.g., ping requests and replies) between two hosts within a Mininet network. This demonstrates how attackers can intercept and alter network communications.

**Files**:

* ```sniff_icmp.py```: Script to capture ICMP packets.  
* ```spoof_icmp.py```: Script to spoof ICMP echo replies.

### **Task 2: MITM Attack Using ARP Cache Poisoning**

This task demonstrates a **Man-in-the-Middle** attack by using ARP cache poisoning. By sending malicious ARP responses, an attacker can intercept and alter communications between two hosts.

**Files**:

* ```udp_server.py```: UDP server script to simulate normal traffic.  
* ```udp_client.py```: UDP client script to simulate normal traffic.  
* ```arp_poison.py```: Script to perform ARP cache poisoning.

### **Task 3: TCP Session Hijacking Attack**

This task explores TCP session hijacking, where an attacker takes over an active session between two hosts by injecting spoofed packets.

**Files**:

* ```tcp_server.py```: TCP server script to simulate a session.  
* ```tcp_client.py```: TCP client script to simulate a session.  
* ```sniff_tcp_session.py```: Script to capture TCP session details.  
* ```tcp_hijack.py```: Script to perform TCP session hijacking by injecting spoofed packets.

---

## **Usage**

Each task is designed to be run in a Mininet environment. Below are the steps to execute each task:

**Set up the Mininet environment**:  
```sudo python hub_topo.py```

1. **Run the relevant scripts** on different Mininet hosts to perform each task.

**Task 1: ICMP Spoofing**  
`# On Host 1`  
```python sniff_icmp.py```

`# On Host 2`  
```ping 10.0.0.1```

**Task 2: ARP Cache Poisoning (MITM)**  
`# On Host 1`  
```python udp_server.py```

`# On Host 2`  
```python udp_client.py```

`# On Host 3`  
```python arp_poison.py```

**Task 3: TCP Session Hijacking**  
`# On Host 1`  
```python tcp_server.py```

`# On Host 2`  
```python tcp_client.py```

`# On Host 3`  
```python sniff_tcp_session.py```  
```python tcp_hijack.py```

2. **Observe the output**: Each script will display output on the console, showing captured packets, spoofed replies, and other details based on the task.

**Note**: Execute these commands within the Mininet environment to simulate real network conditions.

---

## **Contributing**

Contributions to this repository are welcome. All contributions should follow best practices and include detailed comments and documentation.

---

## **License**

This project is licensed under the MIT License. For more information, please refer to the LICENSE file.
