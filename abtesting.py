import streamlit as st
import os
import csv


def main():
    st.title("Omran HEM 7120 - Online Store")
    st.header("Product Details")
    st.image(
        "images/product-image.jpg", caption="Omran HEM 7120", use_column_width=True
    )

    # Product Description
    st.header("Product Description")
    product_description = """
    **Introducing our advanced blood pressure monitor designed with cutting-edge features to revolutionize your health monitoring experience. With a focus on accuracy, visibility, and user-friendliness, this device is your ultimate companion for precise health tracking.**

    **Key Features:**
    
    - **Enhanced Accuracy:** Utilizes advanced technology to provide consistent and reliable blood pressure readings, ensuring accurate health monitoring.

    - **Improved Display Visibility:** Enhanced display ensures clear and easy-to-read blood pressure results, even in varying lighting conditions, for effortless interpretation.

    - **Clear Instructions:** User-friendly interface with clear instructions ensures proper device usage, leading to accurate readings and effective health management.

    - **Expanded Memory Capacity:** Generous memory storage allows users to track and analyze blood pressure trends over time for comprehensive health monitoring.

    - **Rechargeable Battery Option:** Offers the convenience of a rechargeable battery option, reducing battery costs and environmental impact for sustainable power usage.

    - **Includes Power Adapter:** Provides flexibility with both battery and adapter power options for user convenience and uninterrupted usage.

    - **Improved Packaging:** Enhanced packaging ensures the device arrives in pristine condition, protecting it from damage during shipping and enhancing customer satisfaction.

    - **Expanded Cuff Size Options:** Multiple cuff size options ensure a comfortable and accurate fit for users of all body types, improving overall accuracy and user comfort.

    - **Optimized Battery Life:** Extended battery life reduces maintenance needs and ensures long-lasting performance for hassle-free health monitoring.

    - **Strict Quality Control Measures:** Rigorous quality control measures ensure product reliability, durability, and consistent performance, meeting the highest standards for customer satisfaction.

    **Why Choose Our Blood Pressure Monitor?**

    Our blood pressure monitor combines precision, convenience, and reliability to empower you in your health journey. With advanced features and meticulous attention to detail, it's the perfect choice for those who demand accuracy and usability in their health monitoring devices.

    Invest in your health with confidence. Choose our advanced blood pressure monitor today.
    """
    st.markdown(product_description)

    # Space before action buttons
    st.header(" ")

    # Action Buttons
    col1, col2, col3 = st.columns([1, 1, 3])

    with col1:
        if st.button("Buy Now"):
            buy_product()

    with col2:
        if st.button("Add to Cart"):
            add_to_cart()

    with col3:
        st.header("Rate Product")
        rating = st.slider("", 1, 5)

    # Comments & Suggestions Section
    st.header("Comments & Suggestions")
    comment = st.text_area("Leave your comment or suggestion here:")
    if st.button("Submit"):
        submit_comment(comment, rating)


def buy_product():
    # Add your buy functionality here
    st.success("Product bought!")


def add_to_cart():
    # Add your add to cart functionality here
    st.success("Added to cart!")


def submit_comment(comment, rating):
    # Add your comment and rating submission functionality here
    st.success(f"Thank you for your feedback! You rated this product {rating} stars.")
    # Append comment and rating to CSV
    append_to_csv("outputs/feedback.csv", rating, comment)


def append_to_csv(filename, rating, comment):
    # Check if file exists, if not create it and add headers
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Rating", "Review"])  # Include headers for two columns
        writer.writerow([rating, comment])  # Write data in two separate columns


if __name__ == "__main__":
    main()
