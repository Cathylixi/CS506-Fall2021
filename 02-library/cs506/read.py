def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    one_file = open('csv_file_path','r')
    new_list = list(csv.reader(one_file, delimiter=";"))
    return new_list
