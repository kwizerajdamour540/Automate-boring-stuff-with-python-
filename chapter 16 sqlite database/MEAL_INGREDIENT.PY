import sqlite3

def main():
    # Use :memory: or delete meals.db if you want to use a file
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Enable foreign keys in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Explicitly define meals with PRIMARY KEY to satisfy SQLite FK strict constraints
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY,
            name TEXT
        ) STRICT
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            name TEXT,
            meal_id INTEGER,
            FOREIGN KEY(meal_id) REFERENCES meals(id)
        ) STRICT
    """)
    conn.commit()

    while True:
        user_input = input("Enter meal/ingredient or 'meal:ing1,ing2' (or 'quit'): ").strip()

        if user_input.lower() == "quit":
            break

        if ":" in user_input:
            meal_name, ingredients_str = user_input.split(":", 1)
            meal_name = meal_name.strip()
            ingredients = [i.strip() for i in ingredients_str.split(",") if i.strip()]

            cursor.execute("INSERT INTO meals (name) VALUES (?)", (meal_name,))
            meal_id = cursor.lastrowid

            for ingredient in ingredients:
                cursor.execute(
                    "INSERT INTO ingredients (name, meal_id) VALUES (?, ?)",
                    (ingredient, meal_id)
                )

            conn.commit()
            print(f"Meal added: {meal_name}")

        else:
            query_term = user_input.strip()

            cursor.execute("SELECT id FROM meals WHERE name = ?", (query_term,))
            meal_row = cursor.fetchone()

            if meal_row:
                meal_id = meal_row[0]
                cursor.execute("SELECT name FROM ingredients WHERE meal_id = ?", (meal_id,))
                ingredients = cursor.fetchall()

                print(f"Ingredients of {query_term}:")
                for ing in ingredients:
                    print(f"  {ing[0]}")

            else:
                cursor.execute("""
                    SELECT DISTINCT meals.name 
                    FROM meals 
                    JOIN ingredients ON meals.id = ingredients.meal_id 
                    WHERE ingredients.name = ?
                """, (query_term,))
                meals = cursor.fetchall()

                if meals:
                    print(f"Meals that use {query_term}:")
                    for m in meals:
                        print(f"  {m[0]}")

    conn.close()

if __name__ == "__main__":
    main()