import os
from database.database_objects import EBook, serialize_ebook

PDF_DIR_PATH = os.path.join('database', 'blobs', 'ebooks', 'pdf')
USER_DIR_PATH = os.path.join('database', 'blobs', 'accounts')
EBOOKS_DIR_PATH = os.path.join('database', 'blobs', 'ebooks')

GENRE_LIST = ["Kids",
              "Adventure",
              "Education",
              "DIY",
              "Romance",
              "Comedy",
              "Fantasy",
              "Biography",
              "History",
              "Magazine",
              "Religion",
              "Sports"]

init_ISBN = 1000000000
count = 0

for pdf in os.listdir(PDF_DIR_PATH):
    if count == len(GENRE_LIST):
        break

    if pdf.endswith('.pdf'):
        serialize_ebook(EBook(title=(pdf[:-4]),
                              author="Author#" + str(count),
                              genre=GENRE_LIST[count],
                              price=count,
                              uploader=USER_DIR_PATH[count],
                              book_text="",
                              isbn=init_ISBN),
                        str(init_ISBN),
                        os.path.join(PDF_DIR_PATH, pdf))
        init_ISBN += 1
        count += 1
