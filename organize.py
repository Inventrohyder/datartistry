language_folder = "./data/languages/English"
destination_folder = "./ResumeParser/data/input/example_resumes/"
for category in os.listdir(language_folder):
  print(f"Entering '{category}' category")
  category_path = os.path.join(language_folder, category)
  for file in os.listdir(category_path):
    old_loc = category_path + "/" + file
    new_loc = destination_folder + category + "-" + file
    print(f"IN: <<< {old_loc}")
    print(f"OUT: >>> {new_loc}")
    shutil.copy(old_loc, new_loc)
  print('------------')
