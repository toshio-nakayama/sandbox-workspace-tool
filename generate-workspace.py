#!/usr/bin/env python3
"""
generate-workspace.py

Resets and regenerates a fixed workspace directory based on template files.
All generated files are placed directly under a single output directory.
Usage:
  python generate-workspace.py
"""
import os
import shutil

# Fixed configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "workspace-templates")
OUTPUT_ROOT = os.path.join(SCRIPT_DIR, "generated-workspace")

# Definitions: (TYPE code, template filename, output filename pattern, default count)
TYPES = [
    ("PHP", "sandbox.tpl.php", "{type}-{num:03d}-gen.php", 3),
    ("SQL", "query.tpl.sql", "{type}-{num:03d}-tmp.sql", 3),
    ("MD", "document.tpl.md", "{type}-{num:03d}-sample.md", 2),
    ("HTML", "example.tpl.html", "{type}-{num:03d}.html", 1),
    ("TXT", "trouble-shooting.tpl.txt", "{type}-{num:03d}-log.txt", 1),
]


def main():
    # Remove existing workspace directory if it exists
    if os.path.isdir(OUTPUT_ROOT):
        print(f"Removing existing workspace: {OUTPUT_ROOT}")
        shutil.rmtree(OUTPUT_ROOT)

    # Create single output directory
    os.makedirs(OUTPUT_ROOT, exist_ok=True)

    # Copy templates to output directory with incremental naming
    for type_code, tpl_file, filename_pattern, count in TYPES:
        src_path = os.path.join(TEMPLATE_DIR, tpl_file)
        if not os.path.isfile(src_path):
            print(f"Template not found: {src_path}")
            continue

        for i in range(1, count + 1):
            dst_name = filename_pattern.format(type=type_code, num=i)
            dst_path = os.path.join(OUTPUT_ROOT, dst_name)
            shutil.copy(src_path, dst_path)
            print(f"Created: {dst_path}")

    print(f"Workspace has been reset and regenerated at: {OUTPUT_ROOT}")


if __name__ == "__main__":
    main()
