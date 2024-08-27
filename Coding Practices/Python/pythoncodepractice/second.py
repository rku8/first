import pickle 
import pandas as pd
import json
with open('movies_dict.pkl', 'rb') as f:
    data = pickle.load(f)

new_df=pd.DataFrame(data)
movie_title=new_df['title'].values
# mv=list(movies_list)
movie_title = movie_title.tolist()
json_data = json.dumps(movie_title)
print(json_data)
# Write JSON data to list.js file
with open('list.js', 'w') as f:
    f.write('const myList = ')
    f.write(json_data)
    f.write(';')

print(movie_title)