


from datasets import load_dataset

# Load the IMDB dataset
imdb_dataset = load_dataset("imdb")


# Check the dataset structure
print(imdb_dataset)

# Access the training, testing, and validation sets
train_data = imdb_dataset['train']
test_data = imdb_dataset['test']

# View a sample from the training data
print(train_data[0])

# Save the dataset to CSV
train_data.to_csv("imdb_train.csv", index=False)
test_data.to_csv("imdb_test.csv", index=False)


