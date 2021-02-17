import time

test_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Okt', 'Nov', 'Dec']

for index, month in enumerate(test_list):
    time.sleep(0.5)
    print(index, month)
