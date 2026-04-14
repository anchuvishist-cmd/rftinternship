# Basic CSV Reader without Pandas
def read_csv_file(filename):
    data = []
    with open(filename, "r") as file:
        # Read all lines
        lines = file.readlines()

        # First line is header
        headers = lines[0].strip().split(",")

        # Process remaining lines
        for line in lines[1:]:
            values = line.strip().split(",")

            # Handle missing values (replace with None)
            row = {}
            for i in range(len(headers)):
                value = values[i] if i < len(values) and values[i] != "" else None

                # Convert AGE and MARKS to int if not None
                if headers[i] in ["AGE", "MARKS"] and value is not None:
                    value = int(value)

                row[headers[i]] = value
            data.append(row)
    return data


def calculate_average(data, key="MARKS"):
    total, count = 0, 0
    for row in data:
        if row[key] is not None:
            total += row[key]
            count += 1
    return total / count if count > 0 else None


# dry run 
if __name__ == "__main__":
    filename = "students.csv"   # Example CSV file
    result = read_csv_file(filename)

    print("Structured Data:")
    print(result)

    avg_marks = calculate_average(result)
    print("Average Marks:", avg_marks)