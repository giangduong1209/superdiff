import superdiff

com = superdiff.Differ(ignore_case=True).compare('ABCDEF','BCDEF')

print(list(com))

# class Test:
#     def __init__(self, file_one, file_two):    
#         self.file_one = file_one
#         self.file_two = file_two
#     def compare_files(self):
#         return superdiff.Differ().compare(self.file_one, self.file_two)

# com = Test(('A', 'B', 'C', 'D', 'E', 'F'), ('B', 'C', 'D', 'E', 'F', 'G'))
# print(com.compare_files())