import struct
import Writer
import Reader
import InitDB
base_struct = {'id': 'int', 'name': 'str', 'developer': 'str', 'year': "int", 'price': "float", 'purchased': "bool"}
format = InitDB.create_db("Example.bin", base_struct)
# bstruct, format = InitDB.open_db("Example.bin")
# print(bstruct)
# #
# Writer.append("test", format, bstruct, {'aaa': 1, 'bbb': '2', 'ccc': False, 'dddddddd': 4.9})
# Reader.print_base("test", format, bstruct)
#
# f = open("test", "ab")
# {'id': 1, 'name': 'Skyrim', 'developer': 'Bethesda', 'year': 2012, 'price': 39.99, 'purchased': True}
# {'id': 2, 'name': 'Northgard', 'developer': 'Shiro Games', 'year': 2018, 'price': 4.99, 'purchased': True}
# {'id': 3, 'name': 'Factorio', 'developer': 'Wube Software LTD', 'year': 2020, 'price': 4.99, 'purchased': True}
Writer.insert("Example.bin", format, base_struct, 1, {'id': 1, 'name': 'Skyrim', 'developer': 'Bethesda', 'year': 2012, 'price': 39.99, 'purchased': True})
Writer.insert("Example.bin", format, base_struct, 2, {'id': 2, 'name': 'Northgard', 'developer': 'Shiro Games', 'year': 2018, 'price': 4.99, 'purchased': True})
Writer.insert("Example.bin", format, base_struct, 3, {'id': 3, 'name': 'Factorio', 'developer': 'Wube Software LTD', 'year': 2020, 'price': 4.99, 'purchased': True})

# Writer.delete("test", format, bstruct, 7)

# Reader.print_base("test", format, bstruct)
# Reader.print_base_entries(bstruct, Reader.find_by_fields("test", format, bstruct, 'dddddddd', ">", '59'))
