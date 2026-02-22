def get_book_info():
    book_title = input("Enter the book title: ")
    formatted_title = book_title.strip()
    book_ISBN = input("Enter the book ISBN: ")
    formatted_ISBN = book_ISBN.strip()
    book_author_last_name = input("Enter the author's last name: ")
    formatted_author_last_name = book_author_last_name.strip()
    book_publisher = input("Enter the book publisher: ")
    formatted_publisher = book_publisher.strip()
    book_year_published = input("Enter the year published: ") 
    formatted_year_published = book_year_published.strip()
    american_dollars = float(input("Enter the price in American dollars: "))
    formatted_dollars = american_dollars
    
    all_info = f"{formatted_title}/{formatted_ISBN}/{formatted_author_last_name}/{formatted_publisher}/{formatted_year_published}/{formatted_dollars:.2f}"
    return all_info

def to_csv_format(all_info):
    csv = all_info.replace("/",",")
    return csv

def to_JSON_format(csv):
    # json={}
    # fields = cvs.split(",")
    # json["book_title"] = fields[0]
    # json["book_ISBN"] = fields[1]
    # json["book_author_last_name"] = fields[2]
    # json["book_publisher"] = fields[3]
    # json["book_year_published"] = fields[4]
    # json["american_dollars"] = fields[5]
    # return json
   
    fields = []
    start = 0
    for i in range(len(csv)):
        if csv[i] == ",":
            fields.append(csv[start:i].strip())
            start = i + 1
    fields.append(csv[start:].strip())  # Append the last field after the last comma

    title,ISBN,author_last_name,publisher,year_published,dollars = fields
   
    json_string = "{\n"
    json_string += f'  "book_title": "{title}",\n'
    json_string += f'  "book_ISBN": "{ISBN}",\n'
    json_string += f'  "book_author_last_name": "{author_last_name}",\n'
    json_string += f'  "book_publisher": "{publisher}",\n'
    json_string += f'  "book_year_published": "{year_published}",\n'
    json_string += f'  "american_dollars": {dollars}\n'
    json_string += "}"
    return json_string
    
def main():
    book_info = get_book_info()
    csv_format = to_csv_format(book_info)
    json_format = to_JSON_format(csv_format)
    
    print("Book Information:")
    print(book_info)
    print("CSV Format:")
    print(csv_format)
    
    print("\nJSON Format:")
    print(json_format)
# if __name__ == "__main__":  
main()
