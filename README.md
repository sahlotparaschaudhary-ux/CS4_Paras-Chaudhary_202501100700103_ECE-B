# CS4_Paras-Chaudhary_202501100700103_ECE-B

This case study focuses on implementing file handling operations in Python using a log file named CS4.txt. The task involves reading file content using different methods and displaying key information such as total lines and specific portions of the file. It also requires classifying log entries based on keywords like INFO, WARNING, and ERROR. Filtered data must be written into separate files accordingly. Additionally, a search feature is implemented to find and store specific log entries. File pointer operations using seek() are performed to navigate and read different parts of the file.

Sample Output ---

python> python -u "c:\Users\sahlo\OneDrive\Documents\coding\python\file_reading"
Total number of lines: 10



First 2 lines:
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:17:45 ERROR Database connection failed




Last 2 lines:
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully



Log Counts:
{'INFO': 5, 'WARNING': 2, 'ERROR': 3}



Filtered files created successfully.



Enter keyword to search (INFO/WARNING/ERROR): INFO
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:25:12 INFO File uploaded successfully user_id=102
2026-04-01 10:32:11 INFO User logout user_id=101
2026-04-01 10:40:22 INFO User login success user_id=103
2026-04-01 10:50:05 INFO Backup completed successfully

Search results saved in search_result.txt



First 50 characters:
2026-04-01 10:15:32 INFO User login success user_i



After seek(0):
2026-04-01 10:15:32 INFO User login success user_i



From middle:
necting to server
2026-04-01 10:32:11 INFO User lo



Last 100 characters:
d=103
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully


PS C:\Users\sahlo\OneDrive\Documents\coding\python> 
