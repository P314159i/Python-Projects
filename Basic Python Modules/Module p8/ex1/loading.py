import importlib as imp


def check_dependencies() -> None:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    print("👀 Checking dependencies:\n")

    missing_package = []

    for package, description in packages.items():
        try:
            module = imp.import_module(package)
            print(
                f"[OK] {package} ({module.__version__}) "
                f"- {description}"
            )
        except ImportError:
            missing_package.append(package)
            print(f"❌ {package} doesn't exist")

    if missing_package:
        print("\nInstall dependencies with pip:")
        print("  ⚙️  pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("  ⚙️  pip install poetry")
        print("  ⚙️  poetry install\n")
    if not missing_package:
        analysis()


def analysis() -> None:

    print("\n🔬 Analyzing Matrix data...")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # for mypy install pandas-stubs too
    data = np.random.rand(1000)
    # pandas automatically creates an index and a value column (2D)
    df = pd.DataFrame({"value": data})

    print(f"  ~ Processing {len(data)} data points...")
    print(f"    Mean: {df['value'].mean():.3f}")
    print(f"    Min: {df['value'].min():.3f}")
    print(f"    Max: {df['value'].max():.3f}")

    print("\n📊 Generating visualization...")

    # plot takes value coumn and draw as line graph
    # x axis raw index of pandas
    # title, x, y labling graph axis and name
    # savefig saves a png
    # close releases graph from RAM
    plt.plot(df["value"])
    plt.title("Matrix Data")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print(" 🟢 Analysis complete! ")
    print("    Results saved to: 🖼️  matrix_analysis.png")

    print("\n  Dependency management:")
    print("     pip uses requirements.txt")
    print("     Poetry uses pyproject.toml\n")


def main() -> None:
    print("\n\n ҉  LOADING STATUS: Loading programs...")
    check_dependencies()


if __name__ == "__main__":
    main()
