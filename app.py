import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Exploratory Data Analysis Interface",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------
st.title("📊 Streamlit-Based Exploratory Data Analysis")
st.write("Upload a CSV dataset and interactively explore its metadata and attributes.")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("Interactive Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

# --------------------------------------------------
# DATASET INGESTION
# --------------------------------------------------
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        # Check if dataset is empty
        if df.empty:
            st.error("The uploaded CSV file is empty.")
            st.stop()

        st.success("Dataset uploaded successfully!")

        # --------------------------------------------------
        # TOP SECTION - DATASET PREVIEW
        # --------------------------------------------------
        st.header("1. Dataset Preview")

        st.subheader("First 5 Rows")
        st.dataframe(df.head())

        # --------------------------------------------------
        # DATASET DIMENSIONS
        # --------------------------------------------------
        st.header("2. Dataset Overview")

        rows, columns = df.shape

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Number of Rows", rows)

        with col2:
            st.metric("Number of Columns", columns)

        # --------------------------------------------------
        # COLUMN DATA TYPES
        # --------------------------------------------------
        st.subheader("Column Data Types")

        data_types = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(data_types, use_container_width=True)

        # --------------------------------------------------
        # MISSING VALUES
        # --------------------------------------------------
        st.subheader("Missing Values Per Attribute")

        missing_values = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum()
        })

        st.dataframe(missing_values, use_container_width=True)

        # --------------------------------------------------
        # STATISTICAL SUMMARY
        # --------------------------------------------------
        st.subheader("Statistical Summary for Numerical Attributes")

        numerical_columns = df.select_dtypes(
            include=["number"]
        ).columns

        if len(numerical_columns) > 0:

            statistics = pd.DataFrame({
                "Mean": df[numerical_columns].mean(),
                "Median": df[numerical_columns].median(),
                "Minimum": df[numerical_columns].min(),
                "Maximum": df[numerical_columns].max()
            })

            st.dataframe(statistics, use_container_width=True)

        else:
            st.info("No numerical attributes found in the dataset.")

        # --------------------------------------------------
        # ATTRIBUTE SELECTION
        # --------------------------------------------------
        st.sidebar.header("Attribute Analysis")

        selected_column = st.sidebar.selectbox(
            "Select a Column",
            df.columns
        )

        # --------------------------------------------------
        # ATTRIBUTE TYPE DETECTION
        # --------------------------------------------------
        if pd.api.types.is_numeric_dtype(df[selected_column]):
            attribute_type = "Numerical"
        else:
            attribute_type = "Categorical"

        st.sidebar.write(
            f"Detected Attribute Type: **{attribute_type}**"
        )

        # --------------------------------------------------
        # VISUALIZATION MODULE
        # --------------------------------------------------
        st.header("3. Attribute Visualization")

        fig, ax = plt.subplots(figsize=(10, 5))

        # --------------------------------------------------
        # NUMERICAL VISUALIZATION
        # --------------------------------------------------
        if attribute_type == "Numerical":

            sns.histplot(
                df[selected_column].dropna(),
                bins=20,
                kde=True,
                ax=ax
            )

            ax.set_title(
                f"Distribution of {selected_column}"
            )

            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")

        # --------------------------------------------------
        # CATEGORICAL VISUALIZATION
        # --------------------------------------------------
        else:

            value_counts = (
                df[selected_column]
                .dropna()
                .value_counts()
            )

            sns.barplot(
                x=value_counts.index.astype(str),
                y=value_counts.values,
                ax=ax
            )

            ax.set_title(
                f"Frequency Distribution of {selected_column}"
            )

            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")

            plt.xticks(rotation=45)

        # --------------------------------------------------
        # DISPLAY VISUALIZATION
        # --------------------------------------------------
        st.pyplot(fig)

    # --------------------------------------------------
    # ERROR HANDLING
    # --------------------------------------------------
    except pd.errors.EmptyDataError:
        st.error("The uploaded CSV file contains no data.")

    except pd.errors.ParserError:
        st.error(
            "The uploaded file is not a properly formatted CSV file."
        )

    except Exception as e:
        st.error(
            f"An error occurred while reading the file: {e}"
        )

else:

    st.info(
        "Please upload a CSV file using the sidebar to begin analysis."
    )