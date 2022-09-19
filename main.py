import sysconfig


if __name__ == "__main__":
    print("File exists purely to make indexing bug more visible")
    print(f"  Platform:         {sysconfig.get_platform()}")
    print(f"  Python version:   {sysconfig.get_python_version()}")

