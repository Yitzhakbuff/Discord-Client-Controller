import sys

if __name__ == "__main__":
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print(f"Error: Version requerida: 3.6 | tu version: {python_version}")
        sys.exit(1)

    import dcc
    dcc.main()
