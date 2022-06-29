# Project-Sentiment-analysis-on-producr-review

## Project flow
* Understand business problem
* Data collection
* Text preprocessing & data cleaning
* Data visualization
* Sentiment analysis
* Model building & comparison
* Model deployment

## Business problem
Most of the people are expressing their views by posting it on social platforms about a product. We need to understand the liking or disliking of that product to help the organization to make some decisions about the production and supply of the same in the market. So here consider extracting reviews from any social platform or from ecommerce websites and analyze them to satisfy the object.

## Data includes:
19371 reviews
iPhone 4s product
    We collect this data from different websites like amazon, flipkart,
Gadgets 360, Gsmarena, Influenster etc.
![image](https://user-images.githubusercontent.com/93990320/176368826-223672a9-e0ff-4b4c-a95a-1a0c833f760e.png)

## Data preprocessing and cleaning
* Remove null reviews
* Remove punctuations
* Remove hyperlinks
* Remove stop words
* Convert all review in lower case
* Convert numbers to text
* Lemmatization's

## Data visualization
* Positive word cloud
![image](https://user-images.githubusercontent.com/93990320/176369317-57199b03-9992-49da-ad7c-298e3acfc0c7.png)

* Negative word cloud
![image](https://user-images.githubusercontent.com/93990320/176369425-45180116-0117-43a5-a4a4-6002d87360c7.png)

* Sentiment distribution
![image](https://user-images.githubusercontent.com/93990320/176369561-f478418e-8c85-44c8-b622-c5f3ba7f9937.png)

* Pie chart
![image](https://user-images.githubusercontent.com/93990320/176369611-2cc5b94e-ad0e-40b8-a702-af9eabb2ff60.png)

## Sentiment analysis
* Text Blob :-  It is a lexicon-based sentiment analyzer  it has some predefined rules or we can say word & weight dictionary, where it has some scores that helps to calculate sentence’s polarity. 

* Countvectorizer :- As our data is available in text format, we need to convert it into a set of real numbers (a vector) so here we use countvectorizer.

## Model accuracy
![image](https://user-images.githubusercontent.com/93990320/176369881-7ec076b7-265d-40b7-9e94-332229706d5a.png)
* We finalize the Linear SVC because the accuracy of this model accuracy is greater than other models.

## Deployment
* User interface
![image](https://user-images.githubusercontent.com/93990320/176370067-775b052b-5500-4bec-be67-c8efc4f907fa.png)
![image](https://user-images.githubusercontent.com/93990320/176370073-c4fb6af8-0fd5-4e67-a8b5-51ad9345fd34.png)
![image](https://user-images.githubusercontent.com/93990320/176370086-49cc0ae8-cb3b-409a-b4b2-ee528744b9a0.png)








