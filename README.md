# EC46-statistical-analysis

## Running Script
- Open up a terminal and cd into this directory
- cd into main `cd main`
- run the script `python3 start.py`

## Result
Minimum forecasted temperature is -300.0 degrees
This temperature is forecasted to be at 2018-02-17 00:00:00

Maximum forecasted temperature is 10.4 degrees
This temperature is forecasted to be at 2018-01-28 00:00:00

4.0685082872928175 is the mean temperature of the forecast.

5.5 is the median temperature of the forecast.

Warmest monday of the forecast will be on 2018-01-28 00:00:00
with the temperature of 10.4


## Further Work
- All the functions require unit tests. I would use pytest to do these.
- There are lost of locations where Exception handling needs to be included.
- Would be cool to show what the warmest weekend is.
- All the statistical work currently includes the outlying values. For example the -300 value is obviously an outlier.
