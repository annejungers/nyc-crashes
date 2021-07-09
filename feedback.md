It's a good start, and what you did is not wrong, but there needs to be more steps for it to be usable for a ML algo:
1. conversion from categorical string data to numerical data
2. using one hot encoding for categorical data
3. dropping more columns that refer to the same information, or cannot be used by a ML model (zip code, state name, ...)
