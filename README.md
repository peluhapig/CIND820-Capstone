**Read Me File For Initial Results**

We are attempting to predict certain characteristics of a neighborhood based on the cars included inside it. The research question we will attempt to answer is can we predict median income based on the cars in the neighborhood?

https://data.ny.gov/Transportation/Vehicle-Snowmobile-and-Boat-Registrations/w4pv-hbkt/data

*Initial Sampling*

Our DMV registration data which we are utilizing is large, with around 12.2 million observations. 

We utilized stratified sampling, focusing on keeping the zipcode percentages consistent. We initially did 5% of our data, which is around 500 cars per zip code, but after receiving poor results, we increased up to 20% (2,000 cars) and then 40% (4,000 cars). 

**The sampled data included in the github repo is 1%**

*Initial Regression*

The sampled dataset was then cleaned, with the median income added.

Afterward, we made the categorical variables into dummy attributes and attempted to do a regression where our results were abysmal. 

*Pivoting Strategies and Generating New Data*

After seeing the results, we decided to instead count the number of cars of each make in each zip code. We initially did this on a sample set, where we set the "threshold" value to 20 (meaning there had to be at least 20 vehicles of that make registered in NY), but then performed it on the entire set with a threshold of 100,000.

Our MSE for our regression-based off these numbers of cars in zipcode values were initially around 1,000,000 and went down to around 700,000. 

*Further Steps and Plans*

Despite the high MSE, it has potential. Honestly, the ZIP code system is prone to redlining and historically the outliers are OUTLIERS, and it can be hard to do a regression on a dataset with as many as we have. My future steps will be to maybe instead of zip code, group by town and find the town median from the census data. This may be a bit of work and I may have to scrape it myself, however, it would greatly aid in reducing the MSE.


The differences are also in the range of 10,000, which if we're predicting median income is acceptable. The main issue is with those previously mentioned outlier zip codes, where the median income is 200,000 and we predict 80,000. This may also have to do with the pretty high threshold value we chose, we may lower it to 70,000 registered vehicles as we are only considering a few makes, of which there aren't any "high-value brands".

