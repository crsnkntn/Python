from pdfsearch import PDF_Search_All

# Example: Searching a directory of practice tests for keywords using PDF_Search
def main():
    in_path = "question_base"
    print("Enter the first output folder")
    search_output_dir = input()
    while not search_output_dir == "quit":
        keywords = []
        print("Begin entering keywords ('q' to stop)")
        key = input()
        while not key == "q":
            print("waiting")
            keywords.append(key)
            key = input()
        PDF_Search_All(in_path, search_output_dir, keywords)
        print("Enter the desired output folder")
        search_output_dir = input()
    

if __name__ == "__main__":
    main()
