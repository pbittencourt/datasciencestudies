def open_dataset(file_name, header=True):
    """
    Open a dataset contained in a csv file.
    :param str file_name: The csv file that contains the dataset
    :param bool header: If the dataset has a header (default=True)
    :return: A list with dataset content
    """
    # open the file
    opened_file = open(file_name, encoding='utf8')

    # import module that handles csv files
    from csv import reader

    # read the file
    read_file = reader(opened_file)

    # make a list with file contents
    data = list(read_file)

    # if dataset has a header, returns the tuple (header, content)
    if header:
        return data[0], data[1:]
    # else, returns all data
    else:
        return data


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)

    if rows_and_columns:
        print('Número de linhas:', len(dataset))
        print('Número de colunas:', len(dataset[0]))


def extract(dataset, column_index=0):
    """
    Extracts one column from a dataset.
    :param list dataset: A list with all dataset content
    :param int column_index: The index of the column that will be extracted from dataset
    :return: A list with the column contents
    """
    column = []
    for row in dataset:
        column.append(row[column_index])
    return column


def freq_table(column, order_by_desc=False):
    """
    Generates a frequency table from the values on a column and stores it in an dictionary.
    :param list column: the list containing all the items that will generates the frequency table
    :param bool order_by_desc: if the table will be sorted descend by items values (default=False)
    :return: a dictionary with column items as keys and a list containing absolute and relative frequencies
    """
    # initialize an empty dictionary
    frequency_table = {}

    # calculate the total of items in table
    total = len(column)

    # loop through column rows
    for row in column:
        if row in frequency_table:
            # update the values inside 'row' list:
            # increment absolute frequency by 1
            frequency_table[row][0] += 1
            # divides absolute frequency by the totals
            frequency_table[row][1] = frequency_table[row][0] / total
        else:
            # creates an item in dictionary with 'row' as key and of list type
            frequency_table[row] = []
            # the first item of list is absolute frequency. set as 1 (first occurrence)
            frequency_table[row].append(1)
            # the second item is relative frequency, i.e., absolute / total
            frequency_table[row].append(1 / total)

    if order_by_desc:
        from operator import itemgetter
        return sorted(frequency_table.items(), key=itemgetter(1), reverse=True)
    else:
        return frequency_table


def new_freq_table(dataset, index):
    table = {}
    total = 0

    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1

    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage

    return table_percentages


def display_freq_table(dataset, index, title='frequency table', size=50, sep='-', sort_by_value=True, sort_descending=True):
    """
    Display a frequency table of values in a column from a dataset.
    :param list dataset: the dataset, a list of lists
    :param int index: index of the column containing values
    :param str title: title of the table, displayed after it (default='frequency table')
    :param int size: lenght of the table, default=50
    :param str sep: character used to separate sections of the table, default='-'
    :return: none
    """
    # import module to sort dictionary by item values
    from operator import itemgetter
    # extract the column from dataset
    column = extract(dataset, index)
    # make a frequency table from column
    ft = freq_table(column)
    if sort_by_value:
        # sort frequency table by item values, not by key
        sort_ft = sorted(ft.items(), key=itemgetter(1), reverse=sort_descending)
    else:
        sort_ft = sorted(ft.items(), key=itemgetter(0), reverse=sort_descending)

    # display the title of this table
    print(sep * size)
    print(title.upper().center(size))
    print('(column | number of apps | % of total)'.center(size))
    print(sep * size)

    # print table items with number of occurrences
    for value in sort_ft:
        name = value[0].replace("_", " ")
        abs_fq = value[1][0]
        rel_fq = value[1][1] * 100
        # print(f'{name:<34}  {abs_fq:>6}  {rel_fq:04.2f}%')
        print('{:<34}  {:>6}  {:04.2f}%'.format(name, abs_fq, rel_fq))

    # end of table
    print(sep * size)


def display_table(dataset, index):
    table = new_freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse=True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


def number_of_ratings(dataset, genre_index, ratings_index):
    # import module to sort dictionary by item values
    from operator import itemgetter

    # initialize an empty dictionary
    totals = {}

    # initialize the sum of ratings in the entire dataset
    sum_of_ratings = 0

    # loop through content in dataset
    for row in dataset:
        genre = row[genre_index]
        ratings = int(row[ratings_index].replace(',', '').replace('+', ''))
        sum_of_ratings += ratings

        if genre not in totals:
            totals[genre] = []
            totals[genre].append(ratings)
            totals[genre].append(ratings / sum_of_ratings)
        else:
            totals[genre][0] += ratings
            totals[genre][1] = totals[genre][0] / sum_of_ratings

    return sorted(totals.items(), key=itemgetter(1), reverse=True)
