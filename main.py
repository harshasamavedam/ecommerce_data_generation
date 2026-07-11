from produce import  production
def main():
    try:
        print("Running production function...")
        production()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
