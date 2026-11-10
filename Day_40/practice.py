
import sys
import platform
import subprocess
import importlib.util


def show_python_information():
    print("\n--- PYTHON INFORMATION ---")

    print("Python Version:", sys.version)
    print("Python Executable:", sys.executable)
    print("Operating System:", platform.system())


def show_pip_information():
    print("\n--- PIP INFORMATION ---")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout.strip())

    except subprocess.CalledProcessError:
        print("Could not retrieve pip information.")


def show_installed_packages():
    print("\n--- INSTALLED PACKAGES ---")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)

    except subprocess.CalledProcessError:
        print("Could not retrieve installed packages.")


def check_package(package_name):
    print(f"\nChecking package: {package_name}")

    if importlib.util.find_spec(package_name):
        print(f"{package_name} is installed.")
    else:
        print(f"{package_name} is not installed.")


def main():
    print("===== PYTHON ENVIRONMENT MANAGER =====")

    show_python_information()
    show_pip_information()
    check_package("requests")
    show_installed_packages()

    print("\nEnvironment check completed!")


if __name__ == "__main__":
    main()
