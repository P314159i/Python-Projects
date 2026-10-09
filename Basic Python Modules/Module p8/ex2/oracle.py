import os
import sys


try:
    from dotenv import load_dotenv
except ImportError:
    print("Install dotenv with pip:")
    print("pip install python-dotenv\n")
    sys.exit(1)


def get_env_or_exit(key: str) -> str:
    env = os.getenv(key)

    if not env:
        print(f"CRITICAL ERROR: {key} is required but missing.")
        print("\nCreate your .env file with:")
        print("cp .env.example .env")
        sys.exit(1)

    return env


def main() -> None:
    load_dotenv()

    # required: DATABASE_URL and API_KEY
    # so program stops if they are missing
    # the rest have default values even if fail
    mode = os.getenv("MATRIX_MODE", "development")
    database_url = get_env_or_exit("DATABASE_URL")
    api_key = get_env_or_exit("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv(
        "ZION_ENDPOINT",
        "http://localhost:8080"
    )
    db_status = (
                "Connected to local instance"
                if "localhost" in database_url or "127.0.0.1" in database_url
                else "Connected to remote instance"
            )
    api_status = "Authenticated" if api_key else "Not Authenticated"
    zion_status = "ᯤ Online" if zion_endpoint else "𝕠𝕗𝕗𝕝𝕚𝕟𝕖"

    if mode not in ("development", "production"):
        print("CRITICAL ERROR: MATRIX_MODE must be development or production.")
        sys.exit(1)

    print(" 🔮 ORACLE STATUS: Reading the Matrix...\n")
    print(" |၊၊• Configuration loaded:\n")
    print(f"  🛠  Mode: {mode}\n")

    print(f"⛃  Database: {db_status}")

    print(f"⚕️  API Access: {api_status}")
    print(f"📖  Log Level: {log_level}")

    print(f"🌐  Zion Network: {zion_status}")

    print("\nEnvironment security check:")
    print("   🟢 Secrets loaded from environment")

    if os.path.exists(".env"):
        print("   🟢 .env file properly configured")

    # export MATRIX_MODE=production
    # export API_KEY=secret123
    print("   🟢 Environment variable overrides supported")
    print("\n  👁️⃤  The Oracle sees all configurations... 🧙\n")


if __name__ == "__main__":
    main()
