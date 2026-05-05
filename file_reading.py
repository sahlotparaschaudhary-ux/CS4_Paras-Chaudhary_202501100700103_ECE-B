#Paras Chaudhary
#202501100700103
#ECE - B

#        Task 1: Basic File Reading 

file_name = "CS4.txt"

with open(file_name, "r") as file:
    content = file.read()

with open(file_name, "r") as file:
    first_two = [file.readline() for _ in range(2)]

with open(file_name, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
print("\n")
print("\nFirst 2 lines:")
print("".join(first_two))
print("\n")

print("\nLast 2 lines:")
print("".join(lines[-2:]))
print("\n")

#        Task 2: Log Classification 

log_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for line in lines:
    if "INFO" in line:
        log_count["INFO"] += 1
    if "WARNING" in line:
        log_count["WARNING"] += 1
    if "ERROR" in line:
        log_count["ERROR"] += 1

print("\nLog Counts:")
print(log_count)

#         Task 3: Write Filtered Files 

info_lines = []
warning_lines = []
error_lines = []

for line in lines:
    if "INFO" in line:
        info_lines.append(line)
    if "WARNING" in line:
        warning_lines.append(line)
    if "ERROR" in line:
        error_lines.append(line)

with open("info_logs.txt", "w") as f:
    f.writelines(info_lines)

with open("warning_logs.txt", "w") as f:
    f.writelines(warning_lines)

with open("error_logs.txt", "w") as f:
    f.writelines(error_lines)
    print("\n")

print("\nFiltered files created successfully.")

#         Task 4: Search Feature 
print("\n")
keyword = input("\nEnter keyword to search (INFO/WARNING/ERROR): ")

search_results = []

for line in lines:
    if keyword in line:
        print(line.strip())
        search_results.append(line)

with open("search_result.txt", "w") as f:
    f.writelines(search_results)

print("\nSearch results saved in search_result.txt")
print("\n")

#         File Pointer (seek) Operations 

with open(file_name, "r") as file:
    print("\nFirst 50 characters:")
    print(file.read(50))
    print("\n")

    # Move to beginning
    file.seek(0)
    print("\nAfter seek(0):")
    print(file.read(50))
    print("\n")

    # Move to middle
    file.seek(0)
    file_content = file.read()
    middle = len(file_content) // 2
    file.seek(middle)
    print("\nFrom middle:")
    print(file.read(50))
    print("\n")

    # Move to last 100 characters
    file.seek(0)
    file.seek(len(file_content) - 100)
    print("\nLast 100 characters:")
    print(file.read())
    print("\n")
