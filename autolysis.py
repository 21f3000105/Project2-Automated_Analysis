# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "pandas", "scikit-learn", "chardet", "requests", "seaborn", "matplotlib", "python-dotenv","httpx"]
# ///

# Import necessary libraries
import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib
import httpx
import chardet
import time

from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.decomposition import PCA
from httpx import HTTPStatusError

matplotlib.use("Agg")  # Use a non-interactive backend

# Constants
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIxZjMwMDAxMDVAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.0Y7eFEtfKEAmO8Y1s937GPXl0akNtLEsMvQBq6xcRfA"

def send_request_with_retries(url, headers, payload, retries=5, backoff_factor=1.0):
    for attempt in range(retries):
        try:
            response = httpx.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            if e.response.status_code == 429:  # Too Many Requests
                wait_time = backoff_factor * (2 ** attempt)  # Exponential backoff
                print(f"Rate limit hit. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries reached. API is unavailable.")

def load_data(file_path):
    """Load CSV data with encoding detection."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)

def analyze_data(df):
    """Perform advanced data analysis."""
    numeric_df = df.select_dtypes(include=['number'])
    # Advanced analysis: Z-scores and PCA
    z_scores = numeric_df.apply(zscore).to_dict()
    pca = PCA(n_components=min(len(numeric_df.columns), 5))
    pca_result = pca.fit_transform(numeric_df.dropna())
    pca_df = pd.DataFrame(pca_result, columns=[f'PC{i+1}' for i in range(pca_result.shape[1])])

    analysis = {
        'summary': df.describe(include='all').to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'correlation': numeric_df.corr().to_dict(),
        'z_scores': z_scores,
        'pca_components': pca_df.describe().to_dict()
    }
    return analysis

def visualize_data(df, output_dir):
    """Generate and save visualizations with proper adjustments for axis labels."""
    sns.set(style="whitegrid")
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns

    # Numeric distributions
    for column in numeric_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column].dropna(), kde=True, color="skyblue")
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()  # Adjust layout
        plt.savefig(os.path.join(output_dir, f'{column}_distribution.png'))
        plt.close()

        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[column], color="lightgreen")
        plt.title(f'Boxplot of {column}')
        plt.xlabel(column)
        plt.tight_layout()  # Adjust layout
        plt.savefig(os.path.join(output_dir, f'{column}_boxplot.png'))
        plt.close()

    # Correlation heatmap
    if len(numeric_columns) > 1:
        plt.figure(figsize=(12, 10))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.tight_layout()  # Adjust layout
        plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
        plt.close()

    # Pairplot
    if len(numeric_columns) > 1:
        pairplot = sns.pairplot(df[numeric_columns], corner=True, diag_kind="kde")
        pairplot.fig.tight_layout()  # Adjust layout for pairplot
        pairplot.savefig(os.path.join(output_dir, 'pairplot.png'))
        plt.close()

    # PCA Visualization
    if len(numeric_columns) > 1:
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(df[numeric_columns].dropna())
        pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
        plt.figure(figsize=(10, 8))
        sns.scatterplot(x="PC1", y="PC2", data=pca_df, alpha=0.7, color="purple")
        plt.title('PCA Scatterplot')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'pca_scatterplot.png'))
        plt.close()

    # Categorical count plots
    for column in categorical_columns:
        top_values = df[column].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_values.index, y=top_values.values, hue=top_values.index, palette="pastel", dodge=False)
        plt.title(f'Top 10 Most Frequent Values in {column}')
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")  # Rotate labels and align them
        plt.tight_layout()  # Adjust layout
        plt.savefig(os.path.join(output_dir, f'{column}_countplot.png'))
        plt.close()

def generate_graph_descriptions(df, output_dir):
    """Generate descriptions of graphs based on the dataset."""
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    descriptions = []
    
    # Numeric Columns
    for column in numeric_columns:
        descriptions.append(f"- **{column}_distribution.png**: Shows the distribution of values in the `{column}` column.")
        descriptions.append(f"- **{column}_boxplot.png**: Displays the spread and outliers in the `{column}` column.")
    
    # Correlation Heatmap
    if len(numeric_columns) > 1:
        descriptions.append("- **correlation_heatmap.png**: Displays the correlation between numeric columns.")
    
    # Pair Plot
    if len(numeric_columns) > 1:
        descriptions.append("- **pairplot.png**: Shows pairwise relationships between numeric columns.")
    
    # PCA Scatterplot
    if len(numeric_columns) > 1:
        descriptions.append("- **pca_scatterplot.png**: Visualizes the main dimensions of variability in numeric columns using PCA.")

    # Categorical Columns
    for column in categorical_columns:
        descriptions.append(f"- **{column}_countplot.png**: Displays the top 10 most frequent values in the `{column}` column.")
    
    return "\n".join(descriptions)

def generate_narrative(analysis):
    """Generate narrative using LLM."""
    headers = {
        'Authorization': f'Bearer {AIPROXY_TOKEN}',
        'Content-Type': 'application/json'
    }
    prompt = f"Provide a detailed analysis based on the following data summary: {analysis}"
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = httpx.post(API_URL, headers=headers, json=data, timeout=30.0)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating narrative: {e}")
        return "Narrative generation failed due to an error."

def process_file(file_path):
    """Process a single CSV file."""
    df = load_data(file_path)
    analysis = analyze_data(df)

    # Create output directory
    file_base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join("", file_base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Generate visualizations and graph descriptions
    visualize_data(df, output_dir)
    graph_descriptions = generate_graph_descriptions(df, output_dir)
    
    # Generate narrative and combine with graph descriptions
    narrative = generate_narrative(analysis)

    # Generate dataset details
    dataset_summary = f"""
## Dataset Details
- **Rows:** {df.shape[0]}
- **Columns:** {df.shape[1]}
- **Column Names:** {', '.join(df.columns)}
- **Numeric Columns:** {', '.join(df.select_dtypes(include='number').columns)}
- **Categorical Columns:** {', '.join(df.select_dtypes(include=['object', 'category']).columns)}
    """

    # Add processing timestamp
    processing_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Combine all information into README
    readme_content = (
        f"# Analysis Report for {file_base_name}\n\n"
        f"## Overview\n\n"
        f"This report provides an analysis of the dataset `{file_base_name}`. "
        f"The analysis includes statistical summaries, visualizations, and generated insights.\n\n"
        f"## Processing Timestamp\n\n"
        f"- The data was processed on **{processing_timestamp}**.\n\n"
        f"{dataset_summary}\n\n"
        f"## Data Insights\n\n"
        f"{narrative}\n\n"
        f"## Visualizations\n\nThe following visualizations were generated:\n\n"
        f"{graph_descriptions}\n\n"
        f"All visualizations are saved in the `{output_dir}` directory.\n\n"
        f"## Methodology\n\n"
        f"1. **Data Loading:** Data was loaded with encoding detection.\n"
        f"2. **Data Cleaning:** Missing values and anomalies were identified.\n"
        f"3. **Data Analysis:** Statistical summaries and correlations were computed.\n"
        f"4. **Visualizations:** Graphs were generated for deeper insights.\n\n"
        f"## Limitations\n\n"
        f"This analysis is limited by the quality and completeness of the input dataset.\n\n"
        f"## Recommendations\n\n"
        f"- Consider filling missing values in key columns.\n"
        f"- Review outliers in numeric data for potential data errors.\n"
    )
    
    # Save README
    report_filename = os.path.join(output_dir, f'README.md')
    with open(report_filename, 'w') as f:
        f.write(readme_content)

    print(f"Processed {file_path}. Results saved to {output_dir}.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis1.py <path_to_csv>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)
    
    process_file(file_path)

if __name__ == "__main__":
    main()
