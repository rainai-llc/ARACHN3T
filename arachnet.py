#!/usr/bin/env python3
# Scientist: Jeremiah Jackson-Williams
#
# Copy Right @Rainai Inc.
#

import sys
import json
import random

try:
    from memCluster import memCluster
except ImportError:
    print(json.dumps({"error": "memCluster.py not found or has an error."}), flush=True)
    sys.exit(1)

def process_mem_cluster():
    """
    Reads the memCluster data, shuffles it, and formats the first 28 items for output
    with a URL field.
    """
    output_data=[]
    try:
        if not isinstance(memCluster, dict):
            raise TypeError("memCluster is not a dictionary.")

        items_to_process=list(memCluster.items())
        total_items=len(memCluster)

        random.shuffle(items_to_process)

        for i in range(29):
            if i>=len(items_to_process):
                break
            key, value=items_to_process[i]
            output_data.append({
                "Total": total_items,
                "id": i,
                "text": key,
                "url": value
            })
        print(json.dumps(output_data), flush=True)
    except Exception as e:
        print(json.dumps({"error": f"Error processing memCluster: {str(e)}"}), flush=True)
        sys.exit(1)

if __name__ == "__main__":
    process_mem_cluster()
