import pandas
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog
from sklearn import svm

# %matplotlib inline # not needed unless in Jupyter Notebook

#root = tk.Tk()
#Tk().withdraw() # otherwise, the tk window is kept open.  Need to comment this
#so that program exits gracefully after closing matplotlib and other windows
file_open_path = filedialog.askopenfilename()



if file_open_path == '':
    raise SystemExit # no file to open = exit program
else:
    df = pandas.read_csv(file_open_path)
    print(round(df.describe(),2)) # round mean, stdev etc to 2 decimal places
    
    df.boxplot(by=df.columns[4],grid=False, layout=(1,4)), plt.show() #matplotlib/panda. layout control columnxrow arrangement, just for display
    #Tk().withdraw()
    
    file_saveas_path = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    print(file_saveas_path)

    try:
        if file_saveas_path == '':
            pass
            #Tk().withdraw()
            #Tk().destroy()
                    # it's ok if the user does not want to save the output
        else:
            text_to_save= str(df.describe())
            file_saveas_path.write(text_to_save)
            file_saveas_path.close()
    
    except AttributeError:
        pass


# pandas.tools.plotting.scatter_matrix(df) - deprecated; use pandas.plotting.scatter_matrix - this doesn't show anything useful
# pandas.plotting.scatter_matrix(df,color=['black','yellow','blue'], diagonal='kde', alpha=1) - better

# # Calculating Correlations for Multivariate Data
# http://python-for-multivariate-analysis.readthedocs.io/a_little_book_of_python_for_multivariate_analysis.html#calculating-correlations-for-multivariate-data

# http://adataanalyst.com/data-analysis-resources/exploratory-data-analysis-pandas-2/
#from pandas.tools.plotting import parallel_coordinates
#iris_df['groups'] = [iris.target_names[k] for k in groups]
#pll = parallel_coordinates(iris_df,'groups')


# predict species from a given set of measurements




do_prediction = str(input('would you like to predict...? Y for Yes, N for No: '))

if do_prediction == 'Y':
    print('yes, predict')
    
    # svm with sklearn


else:
    print('no prediction, exiting')
    raise SystemExit
