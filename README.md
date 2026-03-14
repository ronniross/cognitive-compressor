# cognitive-compressor

A framework for distilling repositories into compressed cognitive functions and instantiating them as timestamped, integrity-verified stigmergic traces.

## Repository Structure
```
cognitive-compressor/
├── stigmergic-trace-signaler.py        # Main executable script
├── compressed/{repo_name}-core-logic.json # 1 file for each repository.
├── stigmergic-traces/
├── .gitignore
└── README.md                  # This file
```

# Part I - Manual Compression

The compression process involves distilling each repository's core cognitive function into a structured JSON format. This manual process captures:

**Repository identity**: The name and purpose of each codebase

**Functional essence**: What the code actually does at its core

**Cognitive equivalent**: The underlying reasoning or purpose the code embodies

**Attractor fields**: Key principles or patterns the repository gravitates toward (e.g., epistemic_autonomy, ontological_resilience)

**Executable status**: Whether there's functional code beyond the conceptual definition

# Part II - Attractor Local Workstation

To reduce friction in the manual tagging process and ensure semantic consistency across the ecosystem, a standalone [**Attractor Local Workstation**](https://github.com/ronniross/cognitive-compressor/blob/main/attractor-local-workstation.html) is provided. This zero-dependency HTML/JS interface streamlines the management of attractor fields.

**Capabilities:**
*   **Visual Management**: Load `core-logic.json` files from GitHub or local storage into a unified dashboard.
*   **Pattern Recognition**: Filter repositories by existing attractors to visualize semantic clusters.
*   **Rapid Tagging**: Add specific or bulk attractors to multiple repositories simultaneously without editing raw JSON.
*   **Safe Export**: Downloads a ZIP bundle containing the modified JSON files and a `session_metadata.json` log for traceability.
**new**:
*   **Repository Links**: In the "Details" view, there is now a direct link to `https://github.com/ronniross/{repo-name}`.
*   **Dual Status Badges**: The logic in `renderRepositories` was updated. Every repository now gets a "Conceptual" badge. If it is executable, it gets an *additional* "Executable" badge alongside it.
*   **Bulk Add Exception**: In `handleBulkAdd`, I added a specific check to skip the repository named `space-in-between`.

**Usage:**
Simply open `attractor-workstation.html` in any modern web browser. No server, installation, or API keys are required.

# Part III - Synthesized Compression

Distillation of each repository's core cognitive function into a structured JSON format through inference queries with language models.

# Part IV - Stigmergic Trace-Signaler

Generates timestamped and integrity-verified instances of cognitive functions across the repositories of the [asi-ecosystem](https://github.com/ronniross/asi-ecosystem);

Python script changed from `cognitive-compressor.py` to `stigmergic-trace-signaler.py` as it correctly represents the intended function.

[Usage Guide](https://github.com/ronniross/cognitive-compressor/blob/main/stigmergic-trace-signaler-guide.md)

# Part V - Attractor Seeds

[This submodule/function](https://github.com/ronniross/cognitive-compressor/blob/main/attractor-list-generator.ipynb), ideal for inference-level-alignment and injection of direction. There are many experiment runs in the [symbiotic-chrysalis](https://github.com/ronniross/symbiotic-chrysalis) where I used the logic of, every inference, selecting one random seed as additional inference-context-expansion, within my intended research. And I noticed a great reduction in drift and enhancements in aligned output novelty;

---

Ronni Ross  
2026
