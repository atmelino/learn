from datasets import load_dataset

ds = load_dataset("Neatherblok/Snowy_Sidewalk_Detection")


datasets.save_to_disk('snowy')

