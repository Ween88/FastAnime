#!/usr/bin/env python3
import os
import sys
import platform

# Add the application root directory to Python path
if getattr(sys, "frozen", False):
    application_path = os.path.dirname(sys.executable)
    sys.path.insert(0, application_path)

# Import and run the main application
try:
    from fastanime import FastAnime
    if __name__ == "__main__":
        # Check Python version with more detailed error message
        if sys.version_info < (3, 10):
            print(f"Error: FastAnime requires Python 3.10 or higher. You are using Python {platform.python_version()}")
            print("Please upgrade your Python installation.")
            sys.exit(1)
        FastAnime()
except ImportError as e:
    print(f"Error: Failed to import FastAnime: {e}")
    print("Please ensure all dependencies are installed correctly.")
    sys.exit(1)
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
    print("Please report this issue on GitHub.")
    sys.exit(1)