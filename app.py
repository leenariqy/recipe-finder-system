
import streamlit as st
from recipes import (
    get_recommendations, search_recipe, filter_recipes, add_recipe, load_recipes, save_recipes
)

# Load recipe data
recipe_data = load_recipes()

st.title("🍽️ Recipe Finder System")
st.sidebar.title("Menu")
option = st.sidebar.radio("Choose an option:", (
    "Get Recipe Recommendations",
    "Search for a Recipe",
    "Filter Recipes",
    "Add a New Recipe",
))

if option == "Get Recipe Recommendations":
    cuisine = st.text_input("Enter your preferred cuisine (e.g., Italian, Indian):")
    if st.button("Find Recipes"):
        results = get_recommendations(recipe_data, cuisine)
        if results:
            st.success(f"Based on your love for {cuisine}, try these recipes:")
            for r in results:
                st.write(f"- {r}")
        else:
            st.warning("No recipes found for that cuisine. Try another!")

elif option == "Search for a Recipe":
    query = st.text_input("Search by name:")
    if st.button("Search"):
        result = search_recipe(recipe_data, query)
        if result:
            for name, details in result.items():
                st.subheader(f"🍽️ {name}")
                st.write(f"Cuisine: {details['Cuisine']}")
                st.write(f"Ingredients: {', '.join(details['Ingredients'])}")
                st.write(f"Prep Time: {details['Prep Time']} minutes")
                st.write(f"Difficulty: {details['Difficulty']}")
                st.write(f"Rating: {details['Rating']}")
        else:
            st.warning("No matching recipes found.")

elif option == "Filter Recipes":
    st.subheader("Filter Options:")
    difficulty = st.selectbox("Select difficulty:", ("Any", "Easy", "Medium", "Hard"))
    max_time = st.slider("Maximum prep time (minutes):", 0, 120, 30)
    min_rating = st.slider("Minimum rating:", 0.0, 5.0, 4.0)

    if st.button("Filter"):
        filtered = filter_recipes(recipe_data, difficulty, max_time, min_rating)
        if filtered:
            st.success(f"{len(filtered)} recipe(s) found:")
            for name in filtered:
                st.write(f"- {name}")
        else:
            st.warning("No recipes matched your filters.")

elif option == "Add a New Recipe":
    st.subheader("Add Your Recipe")
    name = st.text_input("Recipe Name")
    cuisine = st.text_input("Cuisine")
    ingredients = st.text_area("Ingredients (comma-separated)")
    prep_time = st.number_input("Prep Time (minutes)", min_value=1, step=1)
    difficulty = st.selectbox("Difficulty", ("Easy", "Medium", "Hard"))
    rating = st.number_input("Rating (1 to 5)", min_value=0.0, max_value=5.0, step=0.1)

    if st.button("Add Recipe"):
        new = {
            "Cuisine": cuisine,
            "Ingredients": [i.strip() for i in ingredients.split(",")],
            "Prep Time": int(prep_time),
            "Difficulty": difficulty,
            "Rating": float(rating)
        }
        add_recipe(recipe_data, name, new)
        save_recipes(recipe_data)
        st.success(f"Recipe '{name}' added!")


