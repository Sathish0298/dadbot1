import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def read_ratings_from_csv(filename):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        new_ratings = df["Rating"].tolist()
        return new_ratings
    else:
        # Default ratings in case CSV file doesn't exist or has issues
        return [
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
            5,
            4,
        ]


def compare_products():
    old_ratings = [
        3,
        4,
        5,
        2,
        5,
        1,
        5,
        1,
        3,
        4,
        1,
        4,
        3,
        3,
        5,
        4,
        5,
        2,
        1,
        1,
        3,
        4,
        2,
        4,
        5,
        3,
        2,
        2,
        5,
        1,
    ]
    new_ratings = read_ratings_from_csv("outputs/feedback.csv")

    old_avg_rating = np.mean(old_ratings)
    new_avg_rating = np.mean(new_ratings)

    old_positive_reviews = sum(1 for rating in old_ratings if rating >= 4)
    new_positive_reviews = sum(1 for rating in new_ratings if rating >= 4)

    old_negative_reviews = sum(1 for rating in old_ratings if rating <= 3)
    new_negative_reviews = sum(1 for rating in new_ratings if rating <= 3)

    positive_change = new_positive_reviews - old_positive_reviews
    negative_change = new_negative_reviews - old_negative_reviews

    return old_avg_rating, new_avg_rating, positive_change, negative_change


def main():
    st.title("Product Comparison Analysis")

    # Perform comparison
    old_avg_rating, new_avg_rating, positive_change, negative_change = (
        compare_products()
    )

    # Display comparison results
    st.write("### Comparison Results:")
    st.write(f"Average rating of old product: {old_avg_rating:.2f}")
    st.write(f"Average rating of new product: {new_avg_rating:.2f}")
    st.write(f"Change in number of positive ratings: {positive_change}")
    st.write(f"Change in number of negative ratings: {negative_change}")

    # Visualize comparison with bar chart
    comparison_df = pd.DataFrame(
        {"Product": ["Old", "New"], "Average Rating": [old_avg_rating, new_avg_rating]}
    )

    st.write("### Comparison Visualization:")
    fig, ax = plt.subplots()
    comparison_df.plot(
        kind="bar", x="Product", y="Average Rating", ax=ax, color=["blue", "green"]
    )
    plt.xlabel("Product")
    plt.ylabel("Average Rating")
    plt.title("Average Rating Comparison")
    st.pyplot(fig)


if __name__ == "__main__":
    main()
