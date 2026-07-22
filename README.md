# Youtube-Analysis
# INTRODUCTION
YouTube has become one of the largest platforms for content creators, attracting billions of viewers daily. However, creating a successful video is not just about uploading content factors like video length, posting time, title wording, thumbnail quality, and topic relevance significantly influence performance.Many creators struggle to identify what makes a video perform well and how they can improve before uploading. By leveraging data analytics and machine learning, we can predict a video’s success and provide personalized recommendations to increase its chances of performing well.

# PROBLEM STVATEMENT
YouTube creators often lack data-driven insights before publishing a video, relying on trial and error to optimize content. This results in missed opportunities for engagement and audience growth.
The problem is:
- There is no easily accessible tool that can both predict a video’s potential performance and recommend specific changes based on patterns from successful videos.
- Current YouTube analytics are mostly post-performance, meaning they tell creators how a video performed after it’s already live — too late for changes.
- Creators need a pre upload tool that can assess their content plan and suggest improvements before publishing.

# AIMS
This project aims to build an AI-powered YouTube Success Advisor that:
- Predicts the likelihood of a video’s success based on metadata and historical patterns.
- Highlights the video’s strengths and weaknesses.
- Provides actionable suggestions to improve performance.
Develop a machine learning system that, given a YouTube video’s metadata (title, tags, description, posting time, length, etc.), will:
- Predict the probability of success.
- Explain the main factors influencing that prediction.
- Recommend improvements to maximize performance.

# CLENING THE DATA 
To prepare the dataset for analysis, I performed the following preprocessing steps:
I began by merging the three datasets into a single DataFrame to create a unified structure. After merging, I applied several cleaning transformations to ensure consistency and completeness:
- The column default_language was dropped, as it was not essential for the analysis.
- Missing values in the description column were filled with the placeholder "No description".
- The default_audio_language column was standardized by replacing missing or null entries with "Unknown".
- Missing or null values in the channel_keyword column were replaced with "None".
- These steps ensured that the dataset had no critical gaps and was ready for further exploration and modeling.
## Handling the datatypes
Duration column:
- Converted from ISO 8601 format (PT17M14S) to numeric seconds for easier analysis.
- Old string format was replaced with numeric values in Full_data["duration"].
Channel creation date (channel_created_at):
- Converted from string to datetime with automatic format inference.
- Extracted year, month, day, month name, weekday name, and a clean date for readability and analysis.
Video publish date (published_at):
- Converted from string to datetime, handling fractional seconds.
- Extracted year, month, day, month name, weekday name, and a clean date similar to channel creation date.
- columns converted include video category are definition quality, audio language, region restrictions, license type, and live broadcast status.

# ANALYSIS
1. Descriptive Analysis (Summary Statistics & Exploration)
a) Video-level metrics
Views, likes, comments, duration
- Mean, median, max, min, std
- Distribution plots (histogram, log-scaled for skewed metrics)
- Correlations between views, likes, comments
Tags & categories
- Count of tags per video (tags_count)
- Most common tags
- Distribution across category_id, definition, region_restriction, license
Publication patterns
- Number of videos published per year/month/weekday
- Videos made for kids vs not
- Videos with captions or licensed content
b) Channel-level metrics
Channel engagement
- channel_views, channel_subscribers, channel_total_videos
- Correlation with video-level metrics (do channels with more subscribers get more views/likes?)
Channel age
- channel_date → calculate age of channel
- Relation to average video views or engagement
c) Temporal analysis
Publication trends
- Views/likes/comments over time (daily, monthly, yearly)
- Identify viral periods
- Weekday vs weekend publishing effect
Duration vs engagement
- Short vs long videos
- Average views/likes/comments per duration bucket
2. Content Analysis
Title & description
- Word clouds of frequent words
- Sentiment analysis of titles/descriptions
- Length of title/description vs engagement
- Tag diversity vs engagement









