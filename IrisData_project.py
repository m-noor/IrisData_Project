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
import pathlib

# %matplotlib inline # not needed unless in Jupyter Notebook

#root = tk.Tk()
Tk().withdraw() # otherwise, the tk window is kept open.  Need to comment this
#so that program exits gracefully after closing matplotlib and other windows
file_open_path = filedialog.askopenfilename()

####################################################
# start by reading dataset and do exploratory analysis
####################################################
if file_open_path == '':
    raise SystemExit # no file to open --> exit program
else:
    df = pandas.read_csv(file_open_path)
    
    ######################################
    # summary descriptions
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

       
    ############################################################################
    # save the results to the user's root folder as this is the most
    # OS-independent way
    # don't use string concatenation etc.  as this might introduce problems on
    # specific OSes
    # doing things the Python way :)
    ############################################################################

    # 1.  make a string to save all the information to a file, mirroring what
    # is displayed on outputs above
    text_to_save = '********************* Dataset description *********************' + \
                        '\n\n' + str(df.describe()) + '\n\n' + \
                        '***************** Pearson product moment correlation ***************' + \
                        '\n\n' + str(df.corr()) + '\n\n' + \
                        '********************* Spearman rank correlation *********************' + \
                        '\n\n' + str(df.corr('spearman'))

    # 2.  get path to save file to. we use the current time as this guarantees
    # a unique folder name
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
    
    folder_path = os.path.join(os.path.abspath(os.sep), datetime.datetime.now().strftime('%Y%m%d_%H%M'))
    filename = os.path.join(folder_path, 'iris_data_summary.txt')

    pathlib.Path(folder_path).mkdir(exist_ok=True) # we don't need to create parent directories (parent) as we're writing to root folder, and it's ok if we overwrite the folder although this is unlikey as we're use datetime.now
   
    # 3.  actual file IO operation to write the content
    with open(filename, 'w') as f:
        f.write(text_to_save)
    #   f.close() # not really needed as 'with' takes care of this
  
    ######################################


    ################################################################################
    # make plots for data visualization.
    # panda provides easy interface to matplotlib, the actual engine for
    # plotting
    ################################################################################

    #Tk().withdraw()

    # layout keyword controls column x row boxplot arrangement - just for
    # display
    # we want plots to be grouped by species for clearer visualization of the
    # distribution of the Iris dataset
    
    df.boxplot(by=df.columns[4],grid=False, layout=(1,4), rot=90) # can use fontsize=X to control font
    plt.savefig('fig1_600.png',dpi=600, bbox_inches='tight')

    # alternative method to control font sizes
    # https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
    #SMALL_SIZE = 0.8
    #MEDIUM_SIZE = 0.10
    #BIGGER_SIZE = 0.12

    #plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    #plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    #plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
    #plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    #plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    #plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    #plt.rc('figure', titlesize=SMALL_SIZE)  # fontsize of the figure title

    
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig

    # scatterplots for pairwise multivariate analysis to determine relationship
    # between each of the measurements
    # plt.figure() - no need to add this because the previous plot by pandas
    # exists on its own.  need for the rest of plots to avoid drawing on top of
    # each other
    # kernel density estimation (kde) is clearer than histogram (hist)
    #figure2 = plt.figure()
    pandas.plotting.scatter_matrix(df,color=['black','yellow','blue'], diagonal='kde', alpha=1)
    plt.suptitle('Scatter matrix of flower measurements with kernel density estimation')
    plt.savefig('fig2.png', dpi=600, bbox_inches='tight')
    
    # parallel coordinates as an orthogonal method for multivariate analysis,
    # grouped by species
    figure3 = plt.figure()
    pandas.plotting.parallel_coordinates(df, df.columns[4])
    figure3.suptitle('Parallel coordinates of flower measurements, grouped by species')
    figure3.savefig('fig3.png', dpi=600, bbox_inches='tight')

    # lag plots - if the measurements are truly by nature (not genetics), then
    # the Iris dataset should be random. is this the case?
    # let's see if there is any structure to the data.
    # the standard Iris dataset has 5 columns with the last (species) being
    # text, so just plot the first 4 numeric columns separately
    figure4= plt.figure()

    for i in range(len(df.columns) - 1):
        plt.subplot(2,2,i + 1, title=df.columns[i])
        pandas.plotting.lag_plot(df[df.columns[i]])

    plt.suptitle('Lag plots of flower measurements')
    figure4.savefig('fig4.png', dpi=600, bbox_inches='tight')
    ###########################
    # show all plots at once
    # plt.show()
    ###########################

    #import matplotlib
    #from matplotlib.backends.backend_pdf import PdfPages
    #matplotlib.use('cairo')

    #pp = PdfPages(os.path.join(folder_path, 'multipage.pdf'))

    #figs = [plt.figure(n) for n in plt.get_fignums()]
    #for fig in figs:
    #    fig.savefig(pp)

    #plt.savefig(pp, format='pdf')

    # or:

    #pp.savefig()
    #pp.close()



# 1. save automatically all plots/tables to root folder_date_time
# 2. plot for multivariate analysis + correlation
# 3. https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
# 4. https://www.kaggleusercontent.com/kf/734137/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..QI3UhhnbF6VVJ3Y76Ao37w.2jBaA-73Kfg-RfnokXRh60Yih-HW2B-qO8hsPtoemUzti9GDRUktRrHtfqxJ0HIEQa1_4Y9jUdNKbAxHiHAcZfLcKSKuL4-uj8mAE6KZLnxDvSfDwCAQnJNVc6EvJPyUdwsiawCmKzF1x3satQRR8w.ZWtvVdjVUtyOw8zb-V8XYQ/__results__.html#Feature-to-feature-relationship



############################################################
## bin section
############################################################

# # Calculating Correlations for Multivariate Data (done)
# http://python-for-multivariate-analysis.readthedocs.io/a_little_book_of_python_for_multivariate_analysis.html#calculating-correlations-for-multivariate-data


# predict species from a given set of measurements

#do_prediction = str(input('would you like to predict...? Y for Yes, N for No: '))

#if do_prediction == 'Y':
#    print('yes, predict')
    
#    # svm with sklearn


#else:
#    print('no prediction, exiting')
#    raise SystemExit


# saving matplotlib figs:
# https://stackoverflow.com/questions/26368876/saving-all-open-matplotlib-figures-in-one-file-at-once?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib?rq=1

############################################################
