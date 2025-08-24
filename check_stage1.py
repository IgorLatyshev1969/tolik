
import os
import sys

def check_directory_structure():
    expected_dirs = [
        'src/core', 'src/ui', 'src/utils',
        'tests',
        'resources/icons', 'resources/styles', 'resources/fonts',
        'docs'
    ]
    missing_dirs = [d for d in expected_dirs if not os.path.exists(d)]
    return len(missing_dirs) == 0, missing_dirs

def check_gitignore():
    expected_content = [
        'venv/',
        '__pycache__/',
        '*.pyc',
        '.DS_Store',
        '*.log'
    ]
    if not os.path.exists('.gitignore'):
        return False, "File .gitignore is missing"
    with open('.gitignore', 'r') as f:
        content = f.read()
    missing_entries = [entry for entry in expected_content if entry not in content]
    return len(missing_entries) == 0, missing_entries

def check_logger_setup():
    if not os.path.exists('src/utils/logger.py'):
        return False, "File src/utils/logger.py is missing"
    with open('src/utils/logger.py', 'r') as f:
        content = f.read()
    required_elements = [
        'from loguru import logger',
        'os.path.expanduser("~/Library/Logs/EllTol/")',
        'logger.add(',
        'rotation="10 MB"',
        'retention="30 days"',
        'def get_logger():'
    ]
    missing_elements = [elem for elem in required_elements if elem not in content]
    return len(missing_elements) == 0, missing_elements

def main():
    checks = [
        ("Directory structure", check_directory_structure),
        (".gitignore setup", check_gitignore),
        ("Logger setup", check_logger_setup)
    ]
    
    report = []
    all_passed = True
    
    for check_name, check_func in checks:
        passed, details = check_func()
        status = "PASS" if passed else "FAIL"
        all_passed &= passed
        report.append(f"{check_name}: {status}")
        if not passed:
            report.append(f"  Missing: {', '.join(details)}")
        report.append("")
    
    overall_status = "PASS" if all_passed else "FAIL"
    report.insert(0, f"Overall status: {overall_status}\n")
    
    with open("stage_1_report.txt", "w") as f:
        f.write("\n".join(report))
    
    print(f"Report has been written to 'stage_1_report.txt'")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
