
# Iris Data Project
Programming and Scripting module - Project on the Iris dataset

*By: Mohamed Noor - 2018*

## Introduction
This project related to the Fisher's Iris dataset, as obtained from the UCI Machine Learning Repository [webpage snapshot](UCI Machine Learning Repository_ Iris Data Set.pdf).

To analyze the dataset (in statistics term: exploratory data analysis), a script was written in Python 3.6.3 with Visual Studio Community 2017. The main and other well-known libraries were utilized to read the Iris dataset and output the analysis results.
(see the following section below).

An extensive search was made on [stackoverflow](https://stackoverflow.com/), [Python documentation](https://docs.python.org/3/) and Google in general to determine the best strategy for writing a relatively flexible, OS-independent script.

Briefly, in terms of the Iris dataset itself, the dataset captures the measurements of *Iris* flowers (sepal and petal lengths and widths, all in cm) and the respective *Iris* species (*I. setosa*, *I. versicolor* and *I. virginica*), and was used by Ronald Fisher in his [paper (R.A. Fisher (1936) 'The use of multiple measurements in taxonomic problems', Annals of Eugenics, 7: 179-188. doi:10.1111/j.1469-1809.1936.tb02137.x](https://doi.org/10.1111%2Fj.1469-1809.1936.tb02137.x). Interestingly, note that the journal's name was changed to Annals of Human Genetics for bad connotations of the eugenics field. There is also more information on [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set).

In the machine learning field, this dataset can be used to train different statistical algorithms and perform a prediction on which species a set of flower measurements belong to.

Some images to give a background are in the table below - all images were taken from/linked to the [Wikipedia page](https://en.wikipedia.org/wiki/Iris_flower_data_set), and are confirmed to be freely shareable.


|R. A. Fisher <br>  ![R. A. Fisher](https://upload.wikimedia.org/wikipedia/commons/4/46/R._A._Fischer.jpg)  | *Iris setosa* <br> ![Iris setosa](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/180px-Kosaciec_szczecinkowaty_Iris_setosa.jpg) |
|:---:|:---:|
|***Iris versicolor*** <br> ![Iris versicolor](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/320px-Iris_versicolor_3.jpg)  | ***Iris virginica*** <br> ![Iris virginica](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/295px-Iris_virginica.jpg)|

For those of us not well-versed in flowers, the image below shows the sepal and petal, as linked to [University of Maryland Math Department](https://www.math.umd.edu/~petersd/666/html/iris_pca.html):


<p align="center">
<img src="https://www.math.umd.edu/~petersd/666/html/iris_with_labels.jpg">
</p>


## Methods

### Rationale for chosen method
Among the options considered for designing the project solution was:
1. a graphical user interface whereby users can load their desired dataset and the plots will be displayed within the window. Not pursued because of requirements of installation of wxPython library and time to run.
2. a web-based interface with Plotly. Not pursued due to the relative complexity in writing the code in MVC model, and the code in Python is converted to HTML/JavaScript anyway. If there is no language restriction, writing the code in JavaScript would be the most straightforward option
3. a simple, commandline interface with no user options except for letting users to choose the specific dataset. All outputs are automatically saved to the user's root drive under a subfolder named according to the current time. This was the approach taken in this project.

Imported libraries are:
1. pandas - provides easy manipulation of datasets (dataframes) and obtain descriptive statistical information
2. matplotlib.pyplot - generate graphical plots. Note that pandas already call matplotlib implicitly for plotting
3. tkinter - provides access to OS open file dialog box
4. os, sys, pathlib - to obtain root drive and perform directory operations in an OS-independent way
5. datetime - to allow reading current date and time. Only used to generate a name for folder to save outputs to

### Description of script execution
The script performs certain tasks in a logical way as detailed below:
1. Ask user for the location of the Iris dataset using tkinter dialog. In case the user clicks 'Cancel' in the dialog, the script exits without running the rest of the code.
2. The actual reading of the csv file is done by pandas into a dataframe (df). Following this, multiple statistics can be conveniently obtained including the mean, standard deviation and overall data distribution. The correlation between each of the *Iris* flower measurements are also performed. Information on the various methods to calculate pairwise correlation was obtained from [Statistics Solutions](https://www.statisticssolutions.com/correlation-pearson-kendall-spearman/) and [Minitab Support](http://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/supporting-topics/basics/a-comparison-of-the-pearson-and-spearman-correlation-methods/).

In general:
* Pearson (default): assumes linearity, normal distribution and homoscedasticity (data equally distributed about the regression line
* Kendall: does not seem to be apply here because there is no ranking
* Spearman: non-parametric, no assumption about data distribution. Indicates monotonic relationship (i.e.  rate of change that is not necessarily constant.
* S > P values indicate monotonic, non-linear relationship


## Results and Discussion

...

## Conclusion




<outputs..>

<rationale for approach taken...>
