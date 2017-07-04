# pickler
IPython Notebook magic to make and load pickle dumps of all assignments in a cell or a line

*PyPI package*: pickler-magic

## Description

pickler provides `dumpit` magic function that allows to save cell computation results, and later load them instead of recomputing.
The function finds every assignment in a cell, and saves/loads all affected variables. The dump filename is chosen to be a hash of cell code, so if the cell code changes, it will be recomputed. 

Note that `dumpit` only finds assignments in the cell, so if some function called from the cell changes global variables, these changes won't be preserved or loaded.

## Usage

```{python}
%%dumpit
transformed_train = computationally_hard_transform(train)
transformed_test = computationally_hard_transform(test)
call_some_function()
a, b = function_that_returns_tuple()
```

```{python}
%dumpit data = pandas.load_csv('a_large_dataset.csv')
```

By default, dumps are stored in `pickler_dumps/` folder, to change it set `pickler.FOLDER` variable.
