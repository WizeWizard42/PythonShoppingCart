from pyparsing import empty
import shoppingcart as sc

def main():
    print("Hello world!")
    emptyItem = sc.Item()
    testItem = sc.Item.importItem(24, "Orange", 0.72, 50, "Tasty!")

    print(emptyItem)
    print(testItem)

if __name__ == "__main__":
    main()
