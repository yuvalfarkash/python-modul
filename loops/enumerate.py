# servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for server in enumerate(servers):
#     print(type(server))
#     print(server)
#     print(f"this is tuple {server}")
    

# servers = ["web-01", "web-02", "web-03"]
# # [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for index, server in enumerate(servers):
#     # print(type(server))
#     # print(server)
#     # print(server[0]) # index
#     # print(server[1]) # item
#     print(f"{index} Proccessing server {server}")

# names = ["Alice", "Bob", "Charlie"] #1
# for index, name in enumerate(names):
#     print(index, name)
# servers = ["app-01", "app-02", "app-03"]#2
# for count, server in enumerate(servers):
#     print(count +1, server)
#     count+=1

# errors = ["disk full", "timeout", "connection lost"]#3

# for index , error in enumerate(errors):
#     if index %2==0:
#         print(index, error)

# ports = [22, 80, 443, 8080]#4
# for index, port in enumerate(ports):
#     if index>1:
#         print(port)

# users = ["admin", "dev", "ops"]#5
# for index, user in enumerate(users):
#     print(f"user {index}: {user}")

# files = ["log1.txt", "log2.txt", "log3.txt"]#6
# for index, file in enumerate(files):
#     if index+1==len(files):
#         print(file)

# regions = ["us-east-1", "eu-west-1", "ap-south-1"]#7
# for index, region in enumerate(regions):
#     if index>0:
#         print(region)

services = ["nginx", "redis", "postgres"]
for service in enumerate (services, start=1):
    print(service)