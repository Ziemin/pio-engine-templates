![alt text](https://github.com/apache/incubator-predictionio/blob/develop/docs/manual/source/images/logos/logo.png)

# Engine Templates

* [Classification](#classification)
* [Regression](#regression)
* [Unsupervised Learning](#unsupervised-learning)
* [Recommender Systems](#recommenders)
* [Natural Language Processing](#nlp)

<div id='classification'/>

## Classification
#### ***[Classification](https://github.com/PredictionIO/template-scala-parallel-classification)***<iframe src="https://ghbtns.com/github-btn.html?user=PredictionIO&repo=template-scala-parallel-classification&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


An engine template is an almost-complete implementation of an engine. PredictionIO's Classification Engine Template has integrated Apache Spark MLlib's Naive Bayes algorithm by default.

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Scala | Apache Licence 2.0 | stable | 0.9.2


<div id='regression'/>

## Regression
#### ***[MLLib-LinearRegression](https://github.com/RAditi/PredictionIO-MLLib-LinReg-Template)***<iframe src="https://ghbtns.com/github-btn.html?user=RAditi&repo=PredictionIO-MLLib-LinReg-Template&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


This template uses the linear regression with stochastic gradient descent algorithm from MLLib to make predictions on real-valued data based on features (explanatory variables)

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Scala | Apache Licence 2.0 | alpha | 0.9.1


<div id='unsupervised-learning'/>

## Unsupervised Learning
#### ***[MLlibKMeansClustering](https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate)***<iframe src="https://ghbtns.com/github-btn.html?user=sahiliitm&repo=predictionio-MLlibKMeansClusteringTemplate&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


This is a template which demonstrates the use of K-Means clustering algorithm which can be deployed on a spark-cluster using prediction.io.

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Scala | Apache Licence 2.0 | alpha | -


<div id='recommenders'/>

## Recommender Systems
#### ***[E-Commerce Recommendation](https://github.com/PredictionIO/template-java-parallel-ecommercerecommendation)***<iframe src="https://ghbtns.com/github-btn.html?user=PredictionIO&repo=template-java-parallel-ecommercerecommendation&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


This engine template provides personalized recommendation for e-commerce applications with the following features by default:
* Exclude out-of-stock items
* Provide recommendation to new users who sign up after the model is trained
* Recommend unseen items only (configurable)
* Recommend popular items if no information about the user is available

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Java | Apache Licence 2.0 | alpha | 0.9.3

#### ***[Similar Product](https://github.com/PredictionIO/template-scala-parallel-similarproduct)***<iframe src="https://ghbtns.com/github-btn.html?user=PredictionIO&repo=template-scala-parallel-similarproduct&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


This engine template recommends products that are "similar" to the input product(s). Similarity is not defined by user or item attributes but by users' previous actions. By default, it uses 'view' action such that product A and B are considered similar if most users who view A also view B. The template can be customized to support other action types such as buy, rate, like..etc

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Scala | Apache Licence 2.0 | stable | 0.9.2


<div id='nlp'/>

## Natural Language Processing
#### ***[Text Classification](https://github.com/PredictionIO/template-scala-parallel-textclassification)***<iframe src="https://ghbtns.com/github-btn.html?user=PredictionIO&repo=template-scala-parallel-textclassification&type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>


Use this engine for general text classification purposes. Uses OpenNLP library for text vectorization, includes t.f.-i.d.f.-based feature transformation and reduction, and uses Spark MLLib's Multinomial Naive Bayes implementation for classification.

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
Parallel | Scala | Apache Licence 2.0 | alpha | 0.9.2

