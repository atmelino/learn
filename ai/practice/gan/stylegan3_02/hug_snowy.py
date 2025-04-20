from datasets import load_dataset

ds = load_dataset("Neatherblok/Snowy_Sidewalk_Detection")


ds.save_to_disk('snowy')

