######################################
# A script to analyze Fisher's Iris dataset
######################################
import pandas
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog
import os
import sys
import datetime

# %matplotlib inline # not needed unless in Jupyter Notebook

#root = tk.Tk()
#Tk().withdraw() # otherwise, the tk window is kept open.  Need to comment this
#so that program exits gracefully after closing matplotlib and other windows
file_open_path = filedialog.askopenfilename()

######################################
# start by reading dataset and do analysis
######################################
if file_open_path == '':
    raise SystemExit # no file to open -> exit program
else:
    df = pandas.read_csv(file_open_path)
    
    ######################################
    # exploratory data analysis
    ######################################
    
    print('Dataset description')
    print(round(df.describe(),2)) # round mean, stdev etc to 2 decimal places
    print('\n')
    
    # calculate correlation between variables
    # https://www.statisticssolutions.com/correlation-pearson-kendall-spearman/
    # http://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/supporting-topics/basics/a-comparison-of-the-pearson-and-spearman-correlation-methods/
    # Pearson (default): assumes linearity, normal distribution and
    # homoscedasticity (data equally distributed about the regression line
    # Kendall: does not seem to be apply here because there is no ranking
    # Spearman: non-parametric, no assumption about data distribution.
    # Indicates monotonic relationship (i.e.  rate of change that is not
    # necessarily constant.
    # S > P values indicate monotonic, non-linear relationship
    print('Pearson product moment correlation')
    print(df.corr())
    print('\n')
    print('Spearman rank correlation')
    print(df.corr('spearman'))
    
    # matplotlib/panda.  layout keyword controls column x row boxplot
    # arrangement - just for display
    # we want plots to be grouped by species for clearer visualization of the
    # distribution of the Iris dataset
    df.boxplot(by=df.columns[4],grid=False, layout=(1,4))

    # scatterplots for pairwise multivariate analysis to determine relationship
    # between each of the measurements
    # plt.figure() - no need to add this because the previous plot by pandas
    # exists on its own.  need for the rest of plots to avoid drawing on top of
    # each other
    # kernel density estimation (kde) is clearer than histogram (hist)
    pandas.plotting.scatter_matrix(df,color=['black','yellow','blue'], diagonal='kde', alpha=1,)
    plt.suptitle('Scatter matrix of flower measurements with kernel density estimation')
    
    # parallel coordinates as an orthogonal method for multivariate analysis,
    # grouped by species
    plt.figure()
    pandas.plotting.parallel_coordinates(df, df.columns[4])
    plt.suptitle('Parallel coordinates of flower measurements, grouped by species')

    # lag plots - if the measurements are truly by nature (not genetics), then
    # the Iris
    # dataset should be random.  is this the case?  let's see if there is any
    # structure to the data
    # the standard Iris dataset has 5 columns with the last (species) being
    # text, so just plot the first 4 numeric columns separately
    plt.figure()

    for i in range(len(df.columns) - 1):
        plt.subplot(2,2,i + 1, title=df.columns[i])
        pandas.plotting.lag_plot(df[df.columns[i]])

    plt.suptitle('Lag plots of flower measurements')
    
    ###########################
    # show all plots at once
    plt.show()
    ###########################


    ######################################
    # save the results to the user's root folder as this is the most OS-independent way
    ######################################

    #Tk().withdraw()
    
    #file_saveas_path = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    
    folder_path = os.path.abspath(os.sep) + datetime.datetime.now().strftime('%Y%m%d_%H%M')
    filename = os.path.join(folder_path, 'iris_data_summary.txt') # doing things the Python way :)

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write("FOOBAR")
        f.close()


    try:
        if file_saveas_path == '':
            pass
            #Tk().withdraw()
            #Tk().destroy()
                    # it's ok if the user does not want to save the output
        else:
            text_to_save = '*********************Dataset description*********************' + \
                        '\n\n' + str(df.describe()) + '\n\n' + \
                        '*****************Pearson product moment correlation***************' + \
                        '\n\n' + str(df.corr()) + '\n\n' + \
                        '*********************Spearman rank correlation*********************' + \
                        '\n\n' + str(df.corr('spearman'))

            file_saveas_path.write(text_to_save)
            file_saveas_path.close()
    
    except:
        pass

  

# # Calculating Correlations for Multivariate Data (done)
# http://python-for-multivariate-analysis.readthedocs.io/a_little_book_of_python_for_multivariate_analysis.html#calculating-correlations-for-multivariate-data


# 1. save automatically all plots/tables to root folder_date_time
# 2. plot for multivariate analysis + correlation
# 3. https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
# 4. https://www.kaggleusercontent.com/kf/734137/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..QI3UhhnbF6VVJ3Y76Ao37w.2jBaA-73Kfg-RfnokXRh60Yih-HW2B-qO8hsPtoemUzti9GDRUktRrHtfqxJ0HIEQa1_4Y9jUdNKbAxHiHAcZfLcKSKuL4-uj8mAE6KZLnxDvSfDwCAQnJNVc6EvJPyUdwsiawCmKzF1x3satQRR8w.ZWtvVdjVUtyOw8zb-V8XYQ/__results__.html#Feature-to-feature-relationship


# predict species from a given set of measurements

#do_prediction = str(input('would you like to predict...? Y for Yes, N for No: '))

#if do_prediction == 'Y':
#    print('yes, predict')
    
#    # svm with sklearn


#else:
#    print('no prediction, exiting')
#    raise SystemExit
