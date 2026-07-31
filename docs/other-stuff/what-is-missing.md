# What is missing

> Gemini is garbage so I switched to Claude lol

Here's the consolidated list, pulled from everything we've covered, organized by subject and rough priority.

**Data Structures — the concrete remaining items:**

- Hashing (collision resolution: chaining vs. open addressing, load factor, amortized O(1))
- AVL trees / self-balancing BST theory (balance factor invariant, why rotations restore it — not necessarily every rotation case memorized cold)
- B-tree / B+tree (conceptual: why databases use them, branching factor tied to disk block size — lower priority than the above two)
- Floyd-Warshall path reconstruction (predecessor/`next` matrix — this one's a single afternoon, not a real gap)
- NP-completeness / reductions (formal treatment beyond YouTube-level — Cook-Levin, standard reduction proofs)
- Amortized analysis (formal proof techniques: aggregate, accounting, potential method)

**Operating Systems — beyond what your course + kernel project already cover:**

- Process/thread scheduling algorithms (Round Robin, priority, multilevel feedback queue) and their tradeoffs
- Memory management theory: paging, segmentation, page replacement (LRU/FIFO/Optimal/Clock), TLBs
- Deadlock: necessary conditions, detection/avoidance (Banker's algorithm)
- File systems: inode structures, allocation strategies, journaling
- Formal synchronization: producer-consumer, readers-writers, dining philosophers (the proofs, not just "I used a mutex correctly")

**Computer Architecture — the quantitative side your kernel work doesn't touch:**

- Pipelining and hazards
- Cache hierarchy/coherence, hit/miss ratio calculations
- CPI calculations, pipeline speedup problems
- Branch prediction, ISA-level tradeoffs

**Math:**

- Automata theory (regular languages, DFA/NFA, context-free grammars, pushdown automata, Turing machines/decidability) — the one fully-unstarted topic
- Linear algebra calculation speed drilling (concepts/proofs already solid per you — this is reps, not learning)

**Sequencing suggestion, since you asked for breathing room:**

Given your semester is genuinely light (per our scheduling discussion), I'd stagger this rather than front-load it all before internship season:

- **Now–September:** automata theory (fully new, best to knock out early), hashing + AVL (fast, bounded, directly useful for interviews too)
- **September–October (internship crunch):** pause new theory intake, focus on applications/interviews/kernel project — you don't need this material _done_, just not neglected long-term
- **November–December:** resume the list — scheduling, memory management, deadlock, file systems, NP-completeness/amortized proofs, CA quantitative topics, B+tree
- **Whenever each subject area feels reasonably solid, start layering in NYCU-specific past papers for that subject** — don't wait for 100% coverage across all subjects before starting exam practice, per our last exchange

This is a real but bounded list — nothing on it is "learn a new field," it's all "formalize/extend something adjacent to what you already know." Given your current 70% baseline and 20 weeks of runway, this is very doable without needing to touch it daily starting today. Go build the kernel module and prep for internships — this list will keep.
