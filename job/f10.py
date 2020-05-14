def category_stat(data_file):
    return data_file


stat = category_stat('category_stat_1.csv')
print('\n'.join(str(i) for i in stat))