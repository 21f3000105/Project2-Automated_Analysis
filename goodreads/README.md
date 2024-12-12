# Analysis Report for goodreads

## Overview

This report provides an analysis of the dataset `goodreads`. The analysis includes statistical summaries, visualizations, and generated insights.

## Processing Timestamp

- The data was processed on **12-12-2024 14:18:34**.


## Dataset Details
- **Rows:** 10000
- **Columns:** 23
- **Column Names:** book_id, goodreads_book_id, best_book_id, work_id, books_count, isbn, isbn13, authors, original_publication_year, original_title, title, language_code, average_rating, ratings_count, work_ratings_count, work_text_reviews_count, ratings_1, ratings_2, ratings_3, ratings_4, ratings_5, image_url, small_image_url
- **Numeric Columns:** book_id, goodreads_book_id, best_book_id, work_id, books_count, isbn13, original_publication_year, average_rating, ratings_count, work_ratings_count, work_text_reviews_count, ratings_1, ratings_2, ratings_3, ratings_4, ratings_5
- **Categorical Columns:** isbn, authors, original_title, title, language_code, image_url, small_image_url
    

## Data Insights

### Detailed Analysis of the Book Data Summary

#### Overview
The dataset contains a total of 10,000 entries relating to books from a literary repository, likely Goodreads given the presence of "goodreads_book_id." The dataset encompasses various metrics including book IDs, counts of books authored, average ratings, publication years, and reviews, which provide a comprehensive picture of the book catalog's structure and usage.

#### Data Summary Insights

1. **Book IDs:**
   - **Count:** 10,000
   - **Mean Book ID:** 5000.5
   - **Standard Deviation:** 2886.90 (this indicates a moderate spread across book IDs, suggesting a relatively uniform distribution of book IDs from 1 to 10,000).
   - **Range:** From 1 to 10,000.

2. **Goodreads Book ID:**
   - **Mean:** 5,264,696.51 with a significant standard deviation of 7,575,461.86.
   - **Range:** The minimum of 1 and a maximum of 33,288,638 suggests that some books may not be well-represented or cataloged accurately.

3. **Best Book ID:**
   - This ID similarly follows the trend of having a high mean (5,471,213.58) with a substantial standard deviation (7,827,329.89) across the entries, reinforcing the variability in the dataset.

4. **Work IDs:**
   - The work-related metrics confirm a range from 87 to 56,399,597, indicating that multiple iterations or editions of books are represented, with a mean of 8,646,183.42.

5. **Book Counts:**
   - Mean books count authored is 75.71 with a max of 3,455, indicating that while most authors have a substantial number of titles published, there are also a small number of prolific authors skewing the average.

6. **ISBN and ISBN13:**
   - **ISBN:** 700 missing entries, while all ISBNs are unique.
   - **ISBN13 Mean:** 9,755,044,298,883.46 with standard deviation indicating well-structured relations despite some missing entries.

7. **Authors:**
   - There are 4,664 unique authors, with 'Stephen King' being the most frequently mentioned (60 occurrences), reflecting the presence of popular authors in this dataset.

8. **Publication Year:**
   - The mean year of original publication is around 1981, with entries dating back as far as -1750 (possibly indicating errors or misentries) to a max of 2017. The published works suggest a predominantly recent focus with strong historical representation.
   - The standard deviation indicates variability in publishing years.

9. **Average Ratings:**
   - Average rating sits at 4.00 with a narrow standard deviation (0.25). This suggests a generally high quality of books in the dataset.
   - The distribution of ratings counts from 2.47 at the minimum to a perfect 4.82 shows variance in reader reception.

10. **Ratings Breakdown:**
   - The breakdown (ratings_1 through ratings_5) showcases distinct ratings that inform on user engagement:
     - **Ratings 1 - 5:** The mean number of ratings increases from ratings_1 (1,345) to ratings_5 (23,789). This indicates that the best-rated books tend to receive far more ratings, affirming the popularity of highly-rated titles.

11. **Images:**
   - The dataset shows a notable count of image URLs (10,000 with 6,669 being unique), which may aid in the identification and marketing of these books.

#### Missing Values
The dataset has several missing values, particularly in ISBN (700), ISBN13 (585), original titles (585), and language codes (1,084). This hints at a potential area for further cleaning and enhancing the dataset's usability.

#### Correlation Analysis
The correlation matrix reveals some interesting relationships:
- **Negative Correlations:** There is a noticeable negative correlation between `ratings_count` and all `ratings` categories (specific correlations range from around -0.373 to -0.419), suggesting as ratings increase, total unique ratings (i.e., 1 to 5 classifications) might decrease, possibly indicating a concentration of ratings in well-received works.
  
- **Positive Correlations:** Strong relationships exist between the `work_ratings_count` and all `ratings` categories, which suggests that books with a higher count of reviews tend to attract more ratings across the board.

#### Conclusion
This analysis implies a vibrant community of books, influenced heavily by a few key authors and works, while also highlighting areas for potential improvement in data integrity. The high average ratings suggest a quality standard for the books included in this dataset, with a healthy spread of ratings indicating diverse reader opinions.

Future work could prioritize rectifying missing values and identifying outliers, particularly in publication years, to enhance the analytical strength of the dataset. Additionally, pinpointing how ratings evolve over time per book could foster a deeper understanding of reading trends and reception dynamics.

## Visualizations

The following visualizations were generated:

- **book_id_distribution.png**: Shows the distribution of values in the `book_id` column.
- **book_id_boxplot.png**: Displays the spread and outliers in the `book_id` column.
- **goodreads_book_id_distribution.png**: Shows the distribution of values in the `goodreads_book_id` column.
- **goodreads_book_id_boxplot.png**: Displays the spread and outliers in the `goodreads_book_id` column.
- **best_book_id_distribution.png**: Shows the distribution of values in the `best_book_id` column.
- **best_book_id_boxplot.png**: Displays the spread and outliers in the `best_book_id` column.
- **work_id_distribution.png**: Shows the distribution of values in the `work_id` column.
- **work_id_boxplot.png**: Displays the spread and outliers in the `work_id` column.
- **books_count_distribution.png**: Shows the distribution of values in the `books_count` column.
- **books_count_boxplot.png**: Displays the spread and outliers in the `books_count` column.
- **isbn13_distribution.png**: Shows the distribution of values in the `isbn13` column.
- **isbn13_boxplot.png**: Displays the spread and outliers in the `isbn13` column.
- **original_publication_year_distribution.png**: Shows the distribution of values in the `original_publication_year` column.
- **original_publication_year_boxplot.png**: Displays the spread and outliers in the `original_publication_year` column.
- **average_rating_distribution.png**: Shows the distribution of values in the `average_rating` column.
- **average_rating_boxplot.png**: Displays the spread and outliers in the `average_rating` column.
- **ratings_count_distribution.png**: Shows the distribution of values in the `ratings_count` column.
- **ratings_count_boxplot.png**: Displays the spread and outliers in the `ratings_count` column.
- **work_ratings_count_distribution.png**: Shows the distribution of values in the `work_ratings_count` column.
- **work_ratings_count_boxplot.png**: Displays the spread and outliers in the `work_ratings_count` column.
- **work_text_reviews_count_distribution.png**: Shows the distribution of values in the `work_text_reviews_count` column.
- **work_text_reviews_count_boxplot.png**: Displays the spread and outliers in the `work_text_reviews_count` column.
- **ratings_1_distribution.png**: Shows the distribution of values in the `ratings_1` column.
- **ratings_1_boxplot.png**: Displays the spread and outliers in the `ratings_1` column.
- **ratings_2_distribution.png**: Shows the distribution of values in the `ratings_2` column.
- **ratings_2_boxplot.png**: Displays the spread and outliers in the `ratings_2` column.
- **ratings_3_distribution.png**: Shows the distribution of values in the `ratings_3` column.
- **ratings_3_boxplot.png**: Displays the spread and outliers in the `ratings_3` column.
- **ratings_4_distribution.png**: Shows the distribution of values in the `ratings_4` column.
- **ratings_4_boxplot.png**: Displays the spread and outliers in the `ratings_4` column.
- **ratings_5_distribution.png**: Shows the distribution of values in the `ratings_5` column.
- **ratings_5_boxplot.png**: Displays the spread and outliers in the `ratings_5` column.
- **correlation_heatmap.png**: Displays the correlation between numeric columns.
- **pairplot.png**: Shows pairwise relationships between numeric columns.
- **isbn_countplot.png**: Displays the top 10 most frequent values in the `isbn` column.
- **authors_countplot.png**: Displays the top 10 most frequent values in the `authors` column.
- **original_title_countplot.png**: Displays the top 10 most frequent values in the `original_title` column.
- **title_countplot.png**: Displays the top 10 most frequent values in the `title` column.
- **language_code_countplot.png**: Displays the top 10 most frequent values in the `language_code` column.
- **image_url_countplot.png**: Displays the top 10 most frequent values in the `image_url` column.
- **small_image_url_countplot.png**: Displays the top 10 most frequent values in the `small_image_url` column.

All visualizations are saved in the `goodreads` directory.

## Methodology

1. **Data Loading:** Data was loaded with encoding detection.
2. **Data Cleaning:** Missing values and anomalies were identified.
3. **Data Analysis:** Statistical summaries and correlations were computed.
4. **Visualizations:** Graphs were generated for deeper insights.

## Limitations

This analysis is limited by the quality and completeness of the input dataset.

## Recommendations

- Consider filling missing values in key columns.
- Review outliers in numeric data for potential data errors.
