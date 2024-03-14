from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

def recommend(recipes):
    index = recipe[recipe['title'] == recipes].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_recipes = []  # Correct variable name to plural
    for i in distances[1:13]:
        recommended_recipe = {
            'title': recipe.iloc[i[0]]['title'],
            'image_url': recipe.iloc[i[0]]['img'],
            'link': recipe.iloc[i[0]]['link']
        }
        recommended_recipes.append(recommended_recipe)  # Append to list correctly

    return recommended_recipes

@app.route('/')
def home():
    return render_template('index.html' , recipe_list=recipe["title"].values)

@app.route('/recommend', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        selected_recipe = request.form['selected_recipe']
        recommended_recipe = recommend(selected_recipe)

        return render_template('index.html', recommended_recipe=recommended_recipe)
#
# if __name__ == '__main__':
#     recipe = pickle.load(open('models/recipes.pkl', 'rb'))
#     similarity = pickle.load(open('models/similarity.pkl', 'rb'))
#
#     app.run(debug=True)
