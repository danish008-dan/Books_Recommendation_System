# Book Recommendation System
🧠 Overview

This project is a Book Recommendation System built using Collaborative Filtering techniques.
It analyzes user ratings to recommend books that are similar in reading patterns and preferences.

Using datasets containing users, books, and ratings, the system identifies correlations between different book ratings to suggest books a user is likely to enjoy — just like Netflix or Goodreads recommendations.

🚀 Features

Loads and cleans three datasets: Books.csv, Users.csv, and Ratings.csv

Merges them into a unified DataFrame for analysis

Calculates average ratings and rating counts for each book

Filters active users and popular books for more reliable results

Creates a User–Book Matrix for correlation-based recommendations

Recommends top 10 similar books to a given title

🧩 Tech Stack

Python 3.x

Pandas — Data manipulation

NumPy — Numerical operations

Matplotlib / Seaborn (optional) — Data visualization

Jupyter Notebook / VS Code — Development environment

📁 Dataset Description

The system uses three files:

File	Description
Books.csv	Contains information about books such as ISBN, Title, Author, and Publisher
Users.csv	Contains User IDs and demographic information
Ratings.csv	Contains User ID, Book ISBN, and Rating values

💡 These datasets are part of the Book-Crossing dataset
 commonly used for recommendation system research.

⚙️ How It Works

Load the Data
Import all three datasets using pandas.

Merge the Datasets
Combine Ratings.csv and Books.csv on the ISBN key.

Clean the Data
Remove missing values and duplicates for a clean dataset.

Filter Active Users and Popular Books
Keep only users who rated >100 books and books rated by >50 users.

Create a Pivot Table
Transform the data into a matrix of users (rows) and books (columns).

Find Correlations
Calculate the Pearson correlation coefficient to find similar books.

Generate Recommendations
Display the top correlated books that have at least 50 ratings.

💻 Example Output
📚 Books similar to 'The Lovely Bones: A Novel':

                                         Correlation  Book-Rating
Book-Title                                                                  
The Lovely Bones: A Novel                              1.000000          407
Cryptonomicon                                          0.716309           52
The Jury                                               0.683793           55
Stalker: A Peter Decker and Rina Lazarus Novel         0.683627           51
Outbreak                                               0.665086           56
Vector                                                 0.616469           73
Mortal Prey                                            0.593020           74
The Final Judgment                                     0.581261           59
Nights in Rodanthe                                     0.579580           77
Every Breath You Take : A True Story of Obsessi...     0.560793           51


🧮 Project Structure
Book-Recommendation-System/
│
├── Books.csv
├── Users.csv
├── Ratings.csv
├── book_recommendation.py     # Main Python script
├── README.md
└── requirements.txt           # (optional) library dependencies

🧠 Future Enhancements

Implement KNN (K-Nearest Neighbors) or Cosine Similarity for better accuracy

Build a Content-Based Filtering model using book metadata

Create a Streamlit Web App for interactive book recommendations

Integrate user-based collaborative filtering
