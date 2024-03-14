from app import app
import pickle


if __name__ == '__main__':
    recipe = pickle.load(open('models/recipes.pkl', 'rb'))
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))

    app.run(debug=True)