# -*- coding: utf-8 -*-

"""
Copyright (c) 2016 Randal S. Olson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from __future__ import print_function
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import argparse

def autoclean(input_dataframe, copy=False):
    """Performs a series of automated data cleaning transformations on the provided data set

    Parameters
    ----------
    input_dataframe: pandas.DataFrame
        Data set to clean

    copy: bool
        Make a copy of the data set (default: False)

    Returns
    ----------
    output_dataframe: pandas.DataFrame
        Cleaned data set

    """
    if copy:
        input_dataframe = input_dataframe.copy()

    for column in input_dataframe.columns.values:
        if str(input_dataframe[column].values.dtype) == 'object':
            input_dataframe[column] = LabelEncoder().fit_transform(input_dataframe[column].values)

        # Replace NaNs with the median value of the column
        input_dataframe[column].fillna(input_dataframe[column].median())

    return input_dataframe

def autoclean_cv(training_dataframe, testing_dataframe, copy=False):
    """Performs a series of automated data cleaning transformations on the provided training and testing data sets

    Unlike `autoclean()`, this function takes cross-validation into account by learning the data transformations from only the training set, then
    applying those transformations to both the training and testing set. By doing so, this function will prevent information leak from the
    training set into the testing set.

    Parameters
    ----------
    training_dataframe: pandas.DataFrame
        Training data set

    testing_dataframe: pandas.DataFrame
        Testing data set

    copy: bool
        Make a copy of the data set (default: False)

    Returns
    ----------
    output_training_dataframe: pandas.DataFrame
        Cleaned training data set

    output_testing_dataframe: pandas.DataFrame
        Cleaned testing data set

    """
    return

def main():
    """Main function that is called when datacleaner is run on the command line"""
    from _version import __version__

    parser = argparse.ArgumentParser(description='A Python tool that automatically cleans data sets and readies them for analysis')

    parser.add_argument('INPUT_FILENAME', type=str, help='Data file to clean')

    parser.add_argument('-o', action='store', dest='OUTPUT_FILENAME', default=None,
                        type=str, help='Data file to output to')

    parser.add_argument('-is', action='store', dest='INPUT_SEPARATOR', default='\t',
                        type=str, help='Column separator for the input file (default: \\t)')
                    
    parser.add_argument('-os', action='store', dest='OUTPUT_SEPARATOR', default='\t',
                        type=str, help='Column separator for the output file (default: \\t)')

    parser.add_argument('--version', action='version',
                        version='datacleaner v{version}'.format(version=__version__))

    args = parser.parse_args()

    

if __name__ == '__main__':
    main()
