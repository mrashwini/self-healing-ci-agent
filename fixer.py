import os

def apply_fix(error_type):
    if error_type == "missing_dependency":
        print("🔧 Fix: Installing missing dependency")
        os.system("pip install requests")

    elif error_type == "missing_command":
        print("🔧 Fix: Installing missing command")
        os.system("sudo apt-get install -y make")

    elif error_type == "permission_issue":
        print("🔧 Fix: Fixing permissions")
        os.system("chmod +x script.sh")

    else:
        print("❌ No automatic fix available")
