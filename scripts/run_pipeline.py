"""
Bluestock MF Analytics — Master Pipeline Script
Run this script to execute the complete ETL pipeline
Usage: python scripts/run_pipeline.py
"""

import subprocess
import sys
import os

def run_script(script_path, description):
    """Run a Python script and print status"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"{'='*60}")

    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ {description} — Complete!")
    else:
        print(f"❌ {description} — Failed!")
        return False
    return True

if __name__ == "__main__":
    print("🚀 Bluestock MF Analytics — Full Pipeline")
    print("=" * 60)

    # Change to project root
    os.chdir(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

    steps = [
        ("scripts/data_cleaning.py",
         "Step 1: Data Cleaning"),
        ("scripts/database_setup.py",
         "Step 2: Database Setup"),
        ("scripts/run_queries.py",
         "Step 3: SQL Queries"),
    ]

    success = True
    for script, description in steps:
        if not run_script(script, description):
            success = False
            break

    if success:
        print("\n" + "=" * 60)
        print("🎉 Pipeline Complete! All steps successful!")
        print("=" * 60)
        print("\nNext Steps:")
        print("1. Open Jupyter: python -m jupyter notebook")
        print("2. Run EDA_Analysis.ipynb")
        print("3. Run Performance_Analytics.ipynb")
        print("4. Run Advanced_Analytics.ipynb")
        print("5. Open dashboard/bluestock_mf_dashboard.pbix")
    else:
        print("\n❌ Pipeline failed — check errors above!")