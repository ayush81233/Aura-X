
from datetime import datetime
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
TEST_FILE = PROJECT_DIR / "aura_test.txt"


def show_status():
    print("=" * 40)
    print("AURA-X LOCAL AGENT")
    print("=" * 40)
    print("Status: Online")
    print(f"Computer: macOS")
    print("Safety: Only the project test file is enabled")
    print("=" * 40)


def create_test_file():
    content = (
        "Hello from Aura-X!\n"
        f"Created at: {datetime.now().astimezone().isoformat()}\n"
    )

    TEST_FILE.write_text(content, encoding="utf-8")

    if TEST_FILE.is_file() and TEST_FILE.read_text(encoding="utf-8") == content:
        print(f"SUCCESS: File created and verified.")
        print(f"Location: {TEST_FILE}")
    else:
        print("ERROR: File verification failed.")


def main():
    show_status()
    create_test_file()


if __name__ == "__main__":
    main()
