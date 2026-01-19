"""
Person Re-ID Project Launcher
Interactive menu to run different ML demos
"""

import os
import sys
import subprocess

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Python executable
PYTHON = sys.executable

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("\n" + "="*60)
    print("  🎯 PERSON RE-IDENTIFICATION PROJECT")
    print("="*60)
    print("  AI-Powered Computer Vision Demos")
    print("="*60)

def print_menu():
    print("\n  Choose an option:\n")
    print("    [1] 🧠 Person Re-Identification")
    print("        Face recognition with SFace model")
    print()
    print("    [2] 🧙 Harry Potter Invisible Cloak")
    print("        Color-based invisibility effect")
    print()
    print("    [3] ❌ Quit")
    print()
    print("="*60)

def run_reid():
    print("\n🚀 Launching Person Re-Identification...")
    print("-"*40)
    script = os.path.join(PROJECT_ROOT, "reidentification", "realtime_reid_robust.py")
    if os.path.exists(script):
        subprocess.run([PYTHON, script], cwd=os.path.dirname(script))
    else:
        print(f"❌ Script not found: {script}")
        input("\nPress Enter to continue...")

def run_cloak():
    print("\n🚀 Launching Harry Potter Invisible Cloak...")
    print("-"*40)
    script = os.path.join(PROJECT_ROOT, "harry-potter-cloak", "harry.py")
    if os.path.exists(script):
        subprocess.run([PYTHON, script], cwd=os.path.dirname(script))
    else:
        print(f"❌ Script not found: {script}")
        input("\nPress Enter to continue...")

def goodbye():
    clear_screen()
    print("\n" + "="*60)
    print("  👋 GOODBYE!")
    print("="*60)
    print("\n  Thank you for using Person Re-ID Project!")
    print("  We hope you enjoyed the demos.\n")
    print("  🌟 Created with ❤️ using OpenCV & Deep Learning")
    print("\n" + "="*60 + "\n")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        try:
            choice = input("  Enter your choice (1-3): ").strip()
            
            if choice == "1":
                run_reid()
            elif choice == "2":
                run_cloak()
            elif choice == "3":
                goodbye()
                break
            else:
                print("\n  ⚠️ Invalid choice! Please enter 1, 2, or 3.")
                input("\n  Press Enter to continue...")
        
        except KeyboardInterrupt:
            goodbye()
            break

if __name__ == "__main__":
    main()
