#   Files Objects

#   Open
#   with open('test.txt', "r") as file:

#    size_to_read = 10
#    f_content = file.read(size_to_read)

#   while len(f_content) > 0:
#      print(f_content, end='*')
#     f_content = file.read(size_to_read)


#   Write
#with open('test2.txt', "w") as file:
#    file.write("hello world")
#    file.seek(0)
 #   file.write('M')

#   Copy txt
#with open('test.txt', "r") as rfile:
#    with open('test_copy.txt', "w") as wfile:
#        for line in rfile:
#            wfile.write(line)

#   Copy image
with open('github1_qr.png', "rb") as rfile:
    with open('github1_qr_copy.png', "wb") as wfile:
        chunk_size = 1024
        rfile_chunk = rfile.read(chunk_size)

        while len(rfile_chunk) > 0:
            wfile.write(rfile_chunk)
            rfile_chunk = rfile.read(chunk_size)