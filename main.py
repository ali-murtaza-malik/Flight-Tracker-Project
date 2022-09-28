from api import fetcher
def main_wrapper():
    print(f"This is the start of our project. This function's name is {main_wrapper.__name__}")

    #Code here
    fetcher.states_accessor()

    print("This is the end of our project.")

if __name__ == "__main__":
    main_wrapper()