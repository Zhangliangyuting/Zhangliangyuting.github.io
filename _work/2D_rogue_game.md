---
title: "2D rogue game"
date: 2024-01-05
image: "images/projects/204/cover.png"
category: "OOP / Graph Algorithms"
weight: 4
layout: "work"
abstract: "This project was developed as part of the CPT204 Object-Oriented Programming course, focusing on implementing advanced graph algorithms to create intelligent behaviors in a simplified version of the classic 2D game Rogue. The game involves navigating a dungeon, collecting items, and avoiding enemies, with both the player (Rogue) and the enemy (Monster) employing strategic movement. The project highlights the use of pathfinding and cycle detection algorithms to simulate effective pursuit and evasion dynamics."
---

This project was developed as part of the CPT204 Object-Oriented Programming course, focusing on implementing advanced graph algorithms to create intelligent behaviors in a simplified version of the classic 2D game Rogue. The game involves navigating a dungeon, collecting items, and avoiding enemies, with both the player (Rogue) and the enemy (Monster) employing strategic movement. The project highlights the use of pathfinding and cycle detection algorithms to simulate effective pursuit and evasion dynamics.

## AI Behavior Demonstration

The following GIFs showcase the dynamic interaction between the Monster and the Rogue, highlighting the effectiveness of the algorithms implemented in this project. Each scenario demonstrates the decision-making process of both agents and the resulting outcomes based on the dungeon layout and available strategies:

<figure class="gif-container">
    <img src="../../images/projects/204/E-caught.gif" alt="Demo Animation" class="gif-preview"/>
    <figcaption>
        The Rogue is caught by the Monster due to the lack of a reachable cycle or escape route. The Monster efficiently uses the shortest path to intercept the Rogue.
    </figcaption>
</figure>

<figure class="gif-container">
    <img src="../../images/projects/204/H-notcaught.gif" alt="Demo Animation" class="gif-preview"/>
    <figcaption>
       The Rogue successfully evades the Monster by entering a reachable cycle. Once inside, the Rogue remains one step ahead of the Monster indefinitely, ensuring safety.
    </figcaption>
</figure>

<figure class="gif-container">
    <img src="../../images/projects/204/I-caught.gif" alt="Demo Animation" class="gif-preview"/>
    <figcaption>
        In this scenario, the Rogue is unable to find a safe cycle and is eventually caught by the Monster. This highlights the Rogue’s survival strategy limitations in a cycle-free dungeon.
    </figcaption>
</figure>

<figure class="gif-container">
    <img src="../../images/projects/204/K-notcaught.gif" alt="Demo Animation" class="gif-preview"/>
    <figcaption>
        The Rogue leverages the nearest reachable cycle to avoid capture. The Monster attempts to intercept but cannot prevent the Rogue from entering the cycle, resulting in a successful escape.
    </figcaption>
</figure>

## Path Finding Algorithm

Since the most important part of the game is the path finding algorithm, I will introduce the algorithm in detail.

---

#### **Monster Algorithm: Pursuit Strategies**

The Monster's behavior centers around intelligently tracking and intercepting the Rogue using graph-based strategies:

1. **Pathfinding with BFS:**  
   The Monster uses a Breadth-First Search (BFS) algorithm to calculate the shortest path to the Rogue. This ensures dynamic, layer-by-layer exploration of the dungeon for optimal pursuit.

2. **Cycle Detection with DFS:**  
 The algorithm identifies closed-loop structures (cycles) in the dungeon using Depth-First Search (DFS). These cycles are critical for understanding potential Rogue escape routes. Room areas are abstracted into single nodes to simplify detection and improve computational efficiency.
 <figure>
<img src="../../images/projects/204/Fig1.png" alt="Example Image">
<figcaption>
Figure 1. (a) process of BFS for shortest path and (b) legal/illegal adjacent sites
</figcaption>
 </figure>

  <figure>
<img src="../../images/projects/204/Fig2.png" alt="Example Image">
<figcaption>
Figure 2. Cycle Detection (a) without RoomNode (b) with RoomNode
</figcaption>
 </figure>

3. **Hunting Strategies:**
   - **Shortest Path Pursuit:** The Monster directly follows the shortest path to the Rogue.
   - **Early Interception:** If the Rogue attempts to enter a cycle, the Monster prioritizes blocking the cycle's entry point, using a heuristic to choose the move that minimizes its distance to both the Rogue and the cycle entry. This strategy disrupts the Rogue's chances of using cycles to evade capture.

  <figure>
<img src="../../images/projects/204/Fig3.png" alt="Example Image">
<figcaption>
Figure 3. the Process Diagram of Monster Chasing Logic
</figcaption>
 </figure>

---

#### **Rogue Algorithm: Evasion Strategies**

The Rogue employs adaptive strategies based on the dungeon layout and the Monster's actions to ensure survival or prolong evasion:

1. **Cycle-Based Strategy (Winning Scenarios):**

   - **Cycle Identification & Usage:** The Rogue identifies reachable cycles in the dungeon where it can evade the Monster indefinitely.
   - **Cycle Movement:** Once inside a cycle, the Rogue ensures it stays one step ahead of the Monster by maintaining a safe distance within the loop.

2. **Pathfinding for Cycle Entry:**  
   The Rogue calculates the shortest path to the nearest cycle entry and moves strategically to enter it when threatened.

3. **Survival Strategy (Losing Scenarios):**  
   If no reachable cycle exists, the Rogue chooses a destination as far from the Monster as possible, maximizing survival time.

4. **Dynamic Adaptation:**  
   The Rogue's algorithm continuously evaluates the game state, switching between cycle-based and survival strategies to optimize its moves.

  <figure>
<img src="../../images/projects/204/Fig4.png" alt="Example Image">
<figcaption>
Figure 4. the Process Diagram of Rogue Move Logic. 
</figcaption>
 </figure>

---
