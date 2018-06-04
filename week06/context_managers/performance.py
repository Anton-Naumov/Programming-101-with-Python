import datetime
import time
from contextlib import contextmanager


# class performance:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.start_time = None
#
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         file_header = open(self.file_name, 'a')
#         time_spend = time.time() - self.start_time
#         file_header.write(f'Date: {datetime.datetime.now().date()}, Excecution time: {time_spend}\n')
#         file_header.close()


@contextmanager
def performance(file_name):
    start_time = time.time()
    yield
    end_time = time.time()
    time_spend = end_time - start_time
    with open(file_name, 'a') as file_header:
        file_header.write(f'Date: {datetime.datetime.now()}, Excecution time: {time_spend}\n')


if __name__ == '__main__':
    with performance('log_file.txt'):
        time.sleep(2)
