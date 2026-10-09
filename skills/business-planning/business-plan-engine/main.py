#!/usr/bin/env python3
"""Agensi Skill: Business Plan Engine"""
import json, sys

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    with open("SKILL.md", "r") as f:
        skill_doc = f.read()
    
    result = {
        "skill": "Business Plan Engine",
        "query": query,
        "documentation_length": len(skill_doc),
        "status": "ready"
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
