"""
StartMyDay - Workspace Automation Tool
Step 5 & 6: Open multiple websites and desktop applications (VS Code)
"""
import webbrowser
import subprocess
import time

# Dictionary storing our default target websites
WEBSITES = {
    "Gmail": "https://mail.google.com",
    "GitHub": "https://github.com",
    "Outlook": "https://outlook.live.com",
    "LeetCode": "https://leetcode.com",
    "WhatsApp Web": "https://web.whatsapp.com"
}

def open_websites():
    print("\n🌐 Opening websites in browser tabs...")
    for name, url in WEBSITES.items():
        try:
            webbrowser.open_new_tab(url)
            print(f"  ✓ {name} opened ({url})")
            time.sleep(0.3)  # Small pause to allow browser tab scheduling
        except Exception as e:
            print(f"  ✗ {name} could not be opened: {e}")

def open_vscode():
    print("\n💻 Opening VS Code workspace...")
    try:
        # Popen launches VS Code in the background without blocking Python execution
        subprocess.Popen(["code", "."], shell=True)
        print("  ✓ VS Code opened in current folder")
    except Exception as e:
        print(f"  ✗ VS Code could not be launched: {e}")

def main():
    print("==========================================")
    print("   🚀 START MY DAY - AUTOMATION TOOL      ")
    print("==========================================")
    
    open_websites()
    open_vscode()

    print("\n==========================================")
    print("   ✨ Workspace Ready! Have a productive day! ")
    print("==========================================")

if __name__ == "__main__":
    main()
