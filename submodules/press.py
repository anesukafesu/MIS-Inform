import main
import webbrowser

def press():
    websites = {
        "Igihe": "https://www.igihe.com/",
        "BBC": "https://www.bbc.com/news",
        "KigaliT": "https://www.kigalitoday.com/",
        
    }

    print("Select a news website:")
    for i, name in enumerate(websites.keys()):
        print(f"{i+1}. {name}")
    choice = input("Enter your choice: ")
    try:
        index = int(choice) - 1
        selected_website = list(websites.values())[index]
        webbrowser.open(selected_website)
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")

