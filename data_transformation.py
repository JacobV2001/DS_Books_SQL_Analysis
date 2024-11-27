import csv

def read_csv(file_path):
    """
    Function to read in the file and return the data
    """

    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        return list(reader)
    
def save_csv(file_path, csv_data):
    """
    Function to save the data into a csv
    """

    with open(file_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(csv_data)

def clean_column(csv_data, feature_index):
    """
    Cleans a feature so it will be converted to numerica numbers
    """
    for row in csv_data[1:]:
        if len(row) > feature_index:  # ensure feature exists
            # keep only numbers
            row[feature_index] = ''.join([char for char in row[4] if char.isdigit()])
    return csv_data

# create file values
input_file = 'final_book_dataset_kaggle2.csv'
output_file = 'dsbooks.csv'

# read in data
csv_data = read_csv(input_file)

# clean two columns (pages & n_reviews)
csv_data = clean_column(csv_data, 4)
csv_data = clean_column(csv_data, 6)

# save csv to cleaner and easier to use data
save_csv(output_file, csv_data)