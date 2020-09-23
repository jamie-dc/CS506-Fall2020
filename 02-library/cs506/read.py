def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path, 'r') as file:
        entire_file = file.readlines()
        for row in entire_file:
            row_stripped = row.rstrip("\n")
            split_row_stripped = row_stripped.split(",")
            row_list = []
            for feature in split_row_stripped:
                if feature.isdigit():
                    row_list.append(int(feature))
                else:
                    feature_stripped = feature.strip('"')
                    row_list.append(feature_stripped)
            matrix.append(row_list)
    return matrix
