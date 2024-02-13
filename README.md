# Cornoavirus Twitter Analysis

In this project, I made many different visualizations of Twitter datasets that were filtered using a plethora of hashtags relating to COVID-19 during 2020. From this project, I was able to demonstrate my skills in working with large-scale datasets, working with multilingual text, and using the MapReduce divide-and-conquer technique to create parallel code.

## Background
This project uses a dataset that contains around 1.1 billion geotagged tweets that were sent in 2020. Geotagged tweets only account for 2% of the total tweets that are sent. Therefore, the visualizations made from this project are all under the sample of geotagged tweets only and not a general representation of all tweets.

I went about this project by using the MapReduce divide and conquer strategy to analyze and visualize the dataset. This procedure includes mapping the data into various smaller datasets and then reducing them into one single file that is used to do analysis. In this case, the data was already partitioned beforehand into tweets for every hour for a single day.

### Mapping
I used two different mapping procedures for this project. One was to find the number of mentions for a specific hashtag sorted by language and the other was the number of mentions for a hashtag sorted by country.

### Reducing
I then reduced each of these two different maps by combining each of them into one file. So, one file was created for all the data for countries and the other was all the data for languages in 2020.

### Visualize
Finally, I created visualizations for the data I created by making bar charts. These charts give the top 10 countries or the top 10 languages for two different hashtags: #coronavirus and #코로나바이러스. 

These are the bar graphs for #coronavirus:

<img src=coronaviruscountry.png />
<img src=coronaviruslang.png />

And these are the bar graphs for #코로나바이러스:

<img src=코로나바이러스country.png />
<img src=코로나바이러스lang.png />

## Alternative Reduce
I also created another method for reducing and visualizing this data. In this method, we can compare the different hashtags by the number of tweets during 2020 with a line plot. This alternative-reduce file can take in numerous hashtags as parameters and graph them together in order to compare and visualize. 

Some examples of this can be seen here:

<img src=covid-19_corona.png />
<img src=flu_doctor_sick_virus.png />
