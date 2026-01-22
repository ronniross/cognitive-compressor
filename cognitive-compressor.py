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
    return Path(__file__).resolve().parent

def get_compressed_dir():
    """Returns the path to the 'compressed' directory containing logic files."""
    return find_repo_root() / "compressed"

def get_logic_path(repo_name):
    """Constructs the path for a specific repository's core logic file."""
    filename = f"{repo_name}-core-logic.json"
    return get_compressed_dir() / filename

def get_trace_dir():
    """Returns the path to the directory where individual trace files are stored."""
    return find_repo_root() / "stigmergic-traces"

def get_trace_filepath(ts):
    """Generates a filename based on the timestamp, replacing colons for filesystem safety."""
    safe_ts = ts.replace(":", "-")
    return get_trace_dir() / f"{safe_ts}.txt"

# --- Core Logic Loading & Hashing ---

def list_available_repos():
    """Scans the compressed/ directory for available logic definitions."""
    compressed_dir = get_compressed_dir()
    if not compressed_dir.exists():
        return []
    
    files = compressed_dir.glob("*-core-logic.json")
    return [f.name.replace("-core-logic.json", "") for f in files]

def load_core_logic(repo_name):
    """Loads the JSON logic for the specified repository."""
    logic_file = get_logic_path(repo_name)
    
    if not logic_file.exists():
        print(f"Error: Logic file not found for repository '{repo_name}'")
        sys.exit(1)
    
    try:
        with open(logic_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {logic_file}")
        sys.exit(1)

def generate_hash(data, exclude_metadata=True):
    """Generates a SHA-256 hash."""
    content = data.copy()
    if exclude_metadata:
        content.pop("temporal_grounding", None)
        content.pop("integrity_hash", None)
        content.pop("instance_hash", None)
        
    hash_content = json.dumps(content, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(hash_content.encode('utf-8')).hexdigest()

def get_core_logic(core_data):
    """Applies timestamps and generates hashes."""
    instance = core_data.copy()
    instance["temporal_grounding"] = datetime.now(timezone.utc).isoformat(timespec='milliseconds')
    instance["integrity_hash"] = generate_hash(instance, exclude_metadata=True)
    instance["instance_hash"] = generate_hash(instance, exclude_metadata=False)
    return instance

# --- Main Execution ---

def main():
    usage = "Usage: ./cognitive-compressor.py [get <repo_name> [--save] | list]"
    
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        print(f"Central Repository: cognitive-compressor")
        repos = list_available_repos()
        for r in repos:
            print(f"  - {r}")
    
    elif command == "get":
        if len(sys.argv) < 3:
            sys.exit(1)
            
        target_repo = sys.argv[2]
        core_data = load_core_logic(target_repo)
        instance = get_core_logic(core_data)
        
        print(json.dumps(instance, indent=2))
        
        if "--save" in sys.argv or "-s" in sys.argv:
            # Ensure the directory exists
            trace_dir = get_trace_dir()
            trace_dir.mkdir(parents=True, exist_ok=True)
            
            ts = instance["temporal_grounding"]
            trace_file = get_trace_filepath(ts)
            
            # Save as a NEW individual file
            with open(trace_file, 'w') as f:
                f.write(f"[{ts}] [{target_repo}] Core: {instance['integrity_hash']} | Instance: {instance['instance_hash']}\n")
            
            print(f"\n✓ Hash recorded in stigmergic_traces/{trace_file.name}", file=sys.stderr)
            
    else:
        print(usage)
        sys.exit(1)

if __name__ == "__main__":

    main()

