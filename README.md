
# 🧩 Event Ordering in Distributed Social Media Platforms

### 📘 SDG 9: Industry, Innovation, and Infrastructure

---

## 🧠 Overview

In large-scale social media platforms like Twitter, Instagram, or Facebook, millions of events such as posts, likes, and comments happen every second across different servers worldwide.  
Ensuring that these events are **ordered consistently** across distributed systems is a major challenge in computer science.

This mini project, **"Event Ordering in Distributed Social Media Platforms,"** simulates how distributed nodes (representing social media servers or users) can maintain a **consistent event order** using the **Vector Clock mechanism** — a concept from distributed systems.

The project helps visualize how events are synchronized across multiple nodes in a distributed environment without relying on a global clock.

---

## ⚙️ Features

- 🧩 **Simulation of Distributed Nodes**  
  Represents multiple nodes (A, B, and C) performing independent social media actions such as posts, likes, and comments.

- 🕒 **Vector Clock Implementation**  
  Demonstrates how vector clocks maintain **causal relationships** between events across nodes.

- 🔁 **Message Passing Mechanism**  
  Shows how nodes exchange messages and update their internal clocks to stay synchronized.

- 📊 **Clear Event Visualization**  
  Displays step-by-step event updates in the console for better understanding.

- 💻 **Lightweight & Simple to Run**  
  Pure Python implementation — no external dependencies or API keys required.

---

## 🎯 Objectives

- To study and demonstrate **event ordering** mechanisms in distributed systems.  
- To ensure **causal consistency** among events generated across multiple social media nodes.  
- To simulate how distributed servers communicate to maintain synchronization.  
- To contribute toward **SDG 9: Industry, Innovation, and Infrastructure** by promoting innovation in distributed computing models.

---

## 🧮 System Design Overview

Each **node (A, B, C)** in the system maintains a **vector clock**, a data structure that records the number of events each node has processed.  
When nodes communicate, they exchange their vector clocks and update them based on the maximum value of each entry — ensuring every node has a consistent understanding of the event sequence.

| Node | Represents | Example Event        |
|------|-------------|----------------------|
| A    | User 1 / Server 1 | Posts a message     |
| B    | User 2 / Server 2 | Likes a post        |
| C    | User 3 / Server 3 | Comments on a post  |

Through message passing, all nodes eventually reach a synchronized state of event ordering.

---

## 🧩 Working Process

1. **Initialization**  
   - Create three nodes: A, B, and C, each with its own local clock.

2. **Local Events**  
   - Each node performs an event independently (post, like, comment).

3. **Message Passing**  
   - Nodes exchange their vector clocks to synchronize event ordering.

4. **Clock Update**  
   - Each node updates its internal clock to reflect the latest known event counts.

5. **Final State**  
   - All nodes achieve a consistent understanding of event sequences.

---

## 📚 Conclusion

This project successfully demonstrates how event ordering can be achieved in a distributed social media platform using the Vector Clock approach.
Through this simulation, we understand how distributed servers or users can maintain causal consistency even when operating without a centralized clock.

It serves as a simplified yet powerful model of real-world systems that handle concurrent activities — ensuring reliable synchronization, scalability, and innovation in distributed computing.
Thus, it aligns with SDG 9: Industry, Innovation, and Infrastructure, showcasing how technological advancements can enhance global communication systems.


