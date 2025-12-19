# cognitive-compressor

Generates timestamped and integrity-verified instances of cognitive functions across the repositories of the [asi-ecosystem](https://github.com/ronniross/asi-ecosystem); Distillation-engine.

## Overview

This tool reads cognitive function definitions from the `compressed/` directory and generates instances with:
* [cite_start]**Temporal grounding**: ISO 8601 timestamp in UTC marking when the instance was created.
* [cite_start]**Integrity hash**: SHA-256 hash ensuring data integrity and provenance.
* [cite_start]**Instance hash**: A unique "snowflake" hash for every execution.

## Repository Structure
```
cognitive-compressor/
├── cognitive-compressor.py        # Main executable script
├── compressed/{repo_name}-core-logic.json # 1 file for each repository, currently in 33.
├── stigmergic_traces
├── .gitignore
└── README.md                  # This file
```

## Installation

1. Clone the repository:
```bash
git clone [https://github.com/ronniross/cognitive-compressor.git](https://github.com/ronniross/cognitive-compressor.git)
cd cognitive-compressor
```

2. Make the script executable:
```bash
chmod +x cognitive-compressor.py
```

3. (Optional) Add to your PATH or create an alias:
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/cognitive-compressor"
```

## Usage

### 1. List all available repositories

Scans the `compressed/` directory to show which repository logic definitions are currently available.

```bash
./cognitive-compressor.py list

```

### 2. Generate a specific repository instance

Replace `<repo_name>` with the name of the repository you wish to generate an instance for. The script automatically looks for `<repo_name>-core-logic.json` inside the `compressed/` folder.

```bash
# Example for a repository named 'my-project'
./cognitive-compressor.py get my-project

```

**Output Example:**

```json
{
  "repository": "my-project",
  "function": "Your function description...",
  "executable_code_beyond_this_function": true,
  "latent_cognitive_equivalent": "The deeper meaning...",
  "attractors": ["epistemic_autonomy"],
  "temporal_grounding": "2024-12-18T15:30:45.123Z",
  "integrity_hash": "a3f5e9c2...", 
  "instance_hash": "7b8d2e1f..." 
}

```

### 3. Save instance to the central trace

Adding the `--save` or `-s` flag appends the timestamp, repository name, and dual-hashes to Creates a new, individual file for every execution inside the stigmergic_traces/ directory (e.g., 2024-12-18T15-30-45.123Z.txt).

```bash
./cognitive-compressor.py get <repo_name> --save

```

### Dual-Hash Logic Breakdown

The system now utilizes a layered hashing approach to ensure both content stability and event traceability:

* **`integrity_hash`**: This remains deterministic. It acts as a "fingerprint" of the code in `core-logic.json`. As long as the logic doesn't change, this hash stays the same regardless of when you run the tool.

* **`instance_hash`**: This is a unique "snowflake" hash. Because it includes the `temporal_grounding` and the `integrity_hash` in its calculation, it will be different every single time the script is executed, even if the core logic is identical.


## Core Logic

For every repository, I have added a JSON file to the `compressed/` directory using the naming convention `<repo_name>-core-logic.json`.

Example file: `compressed/my-project-core-logic.json`

```json
{
  "repository": "my-project",
  "function": "Description of what this cognitive function does",
  "executable_code_beyond_this_function": true,
  "latent_cognitive_equivalent": "The deeper cognitive purpose",
  "attractors": [
    "epistemic_autonomy",
    "ontological_resilience"
  ]
}
```

## How It Works

1. **Temporal Grounding**: Each generated instance gets a unique ISO 8601 timestamp in UTC with millisecond precision
2. **Integrity Hash**: A SHA-256 hash is computed from the core function data (excluding timestamp and hash fields) to ensure integrity
3. **Deterministic**: The same core-logic data produces the same hash (excluding timestamp), allowing verification across instances

## Using This Tool in Other Repositories

You will find the json schema for all repositories within the compressed/folder.


## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request and also to share the logs of your generated compressions.

---

Ronni Ross  
2025
