# Importing required libraries
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Step 1: Load all the datasets
books = pd.read_csv("Books.csv")
users = pd.read_csv("Users.csv")
ratings = pd.read_csv("Ratings.csv")

print("Books Data:\n", books.head())
print("\nUsers Data:\n", users.head())
print("\nRatings Data:\n", ratings.head())


# Step 2: Merge all datasets together
# Merge ratings with books
df = pd.merge(ratings, books, on='ISBN')
print("\nMerged Data:\n", df.head())

# Step 3: Data cleaning
# Keep only necessary columns
df = df[['User-ID', 'Book-Title', 'Book-Author', 'Publisher', 'Book-Rating']]

# Drop duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)


# Step 4: Filter active users and popular books
# Keep users who have rated more than 100 books
active_users = df['User-ID'].value_counts()
active_users = active_users[active_users > 100].index
df = df[df['User-ID'].isin(active_users)]

# Keep books with more than 50 ratings
popular_books = df['Book-Title'].value_counts()
popular_books = popular_books[popular_books > 50].index
df = df[df['Book-Title'].isin(popular_books)]

print("\nFiltered Data Shape:", df.shape)

# Step 5: Create Pivot Table (User-Book Matrix)
book_matrix = df.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating')
print("\nUser-Book Rating Matrix:\n", book_matrix.head())

# Step 6: Correlation-based Recommendation
# Choose a sample book for testing
book_name = "The Lovely Bones: A Novel"

if book_name in book_matrix.columns:
    book_ratings = book_matrix[book_name]
    similar_books = book_matrix.corrwith(book_ratings)
    corr_book = pd.DataFrame(similar_books, columns=['Correlation'])
    corr_book.dropna(inplace=True)

    # Add number of ratings to each book
    ratings_count = df.groupby('Book-Title')['Book-Rating'].count()
    corr_book = corr_book.join(ratings_count)

    # Recommend top similar books with more than 50 ratings
    recommendations = corr_book[corr_book['Book-Rating'] > 50].sort_values('Correlation', ascending=False).head(10)

    print(f"\nBooks similar to '{book_name}':\n")
    print(recommendations)
else:
    print(f"\n'{book_name}' not found in the dataset! Try another title.")
