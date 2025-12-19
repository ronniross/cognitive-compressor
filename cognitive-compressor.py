#!/usr/bin/env python3
import json
import hashlib
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

# --- Path Configuration ---

def find_repo_root():
    """Returns the root directory where this script is located."""
    return Path(__file__).resolve().parent [cite: 1]

def get_compressed_dir():
    """Returns the path to the 'compressed' directory containing logic files."""
    return find_repo_root() / "compressed" [cite: 1]

def get_logic_path(repo_name):
    """Constructs the path for a specific repository's core logic file."""
    filename = f"{repo_name}-core-logic.json"
    return get_compressed_dir() / filename [cite: 1]

def get_trace_dir():
    """Returns the path to the directory where individual trace files are stored."""
    return find_repo_root() / "stigmergic_traces"

def get_trace_filepath(ts):
    """Generates a filename based on the timestamp, replacing colons for filesystem safety."""
    safe_ts = ts.replace(":", "-")
    return get_trace_dir() / f"{safe_ts}.txt"

# --- Core Logic Loading & Hashing ---

def list_available_repos():
    """Scans the compressed/ directory for available logic definitions."""
    compressed_dir = get_compressed_dir() [cite: 1]
    if not compressed_dir.exists(): [cite: 1]
        return [] [cite: 1]
    
    files = compressed_dir.glob("*-core-logic.json") [cite: 1]
    return [f.name.replace("-core-logic.json", "") for f in files] [cite: 1]

def load_core_logic(repo_name):
    """Loads the JSON logic for the specified repository."""
    logic_file = get_logic_path(repo_name) [cite: 1]
    
    if not logic_file.exists(): [cite: 1]
        print(f"Error: Logic file not found for repository '{repo_name}'") [cite: 1]
        sys.exit(1) [cite: 1]
    
    try:
        with open(logic_file, 'r') as f: [cite: 1]
            return json.load(f) [cite: 1]
    except json.JSONDecodeError: [cite: 1]
        print(f"Error: Failed to decode JSON from {logic_file}") [cite: 1]
        sys.exit(1) [cite: 1]

def generate_hash(data, exclude_metadata=True):
    """Generates a SHA-256 hash."""
    content = data.copy() [cite: 1]
    if exclude_metadata: [cite: 1]
        content.pop("temporal_grounding", None) [cite: 1]
        content.pop("integrity_hash", None) [cite: 1]
        content.pop("instance_hash", None) [cite: 1]
        
    hash_content = json.dumps(content, sort_keys=True, separators=(',', ':')) [cite: 1]
    return hashlib.sha256(hash_content.encode('utf-8')).hexdigest() [cite: 1]

def get_core_logic(core_data):
    """Applies timestamps and generates hashes."""
    instance = core_data.copy() [cite: 1]
    instance["temporal_grounding"] = datetime.now(timezone.utc).isoformat(timespec='milliseconds') [cite: 1]
    instance["integrity_hash"] = generate_hash(instance, exclude_metadata=True) [cite: 1]
    instance["instance_hash"] = generate_hash(instance, exclude_metadata=False) [cite: 1]
    return instance [cite: 1]

# --- Main Execution ---

def main():
    usage = "Usage: ./cognitive-compressor.py [get <repo_name> [--save] | list]" [cite: 1]
    
    if len(sys.argv) < 2: [cite: 1]
        print(usage) [cite: 1]
        sys.exit(1) [cite: 1]
    
    command = sys.argv[1] [cite: 1]
    
    if command == "list": [cite: 1]
        print(f"Central Repository: cognitive-compressor") [cite: 1]
        repos = list_available_repos() [cite: 1]
        for r in repos: [cite: 1]
            print(f"  - {r}") [cite: 1]
    
    elif command == "get": [cite: 1]
        if len(sys.argv) < 3: [cite: 1]
            sys.exit(1) [cite: 1]
            
        target_repo = sys.argv[2] [cite: 1]
        core_data = load_core_logic(target_repo) [cite: 1]
        instance = get_core_logic(core_data) [cite: 1]
        
        print(json.dumps(instance, indent=2)) [cite: 1]
        
        if "--save" in sys.argv or "-s" in sys.argv: [cite: 1]
            # Ensure the directory exists
            trace_dir = get_trace_dir()
            trace_dir.mkdir(parents=True, exist_ok=True)
            
            ts = instance["temporal_grounding"] [cite: 1]
            trace_file = get_trace_filepath(ts)
            
            # Save as a NEW individual file
            with open(trace_file, 'w') as f:
                f.write(f"[{ts}] [{target_repo}] Core: {instance['integrity_hash']} | Instance: {instance['instance_hash']}\n")
            
            print(f"\n✓ Hash recorded in stigmergic_traces/{trace_file.name}", file=sys.stderr)
            
    else:
        print(usage) [cite: 1]
        sys.exit(1) [cite: 1]

if __name__ == "__main__":
    main()