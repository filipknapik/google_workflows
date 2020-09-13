# Open Exchange Rates connector for Google Workflows
Open source connector for OpenExchangeRates API. 

<h3>Overview</h3>

It supports the following methods
- [Latest Exchange Rates- latestOpenExchangeRates](#latestOpenExchangeRates)
- [Time Series Exchange Rates - timeSeriesOpenExchangeRates](#timeSeriesOpenExchangeRates)
- [Historical Exchange Rates for a date - historicalOpenExchangeRates](#historicalOpenExchangeRates)
- [Open, High, Low, Close exchange rates - ohlcOpenExchangeRates](#ohlcOpenExchangeRates)
- [Convert amount from one currency to another - convertOpenExchangeRates](#convertOpenExchangeRates)


<br>
<h3>Usage</h3>

**OpenExchangeRates**

1. Register at OpenExchangeRates and obtain an App ID key.

**Google Cloud**

1. Create new or edit Service Account that you will use when deploying your workflow. Assign it a "Secret Manager Secret Accessor" role.
2. Create a new Secret in Secret Manager to store the appid you got in OpenExchangeRates preparation step
3. Copy and paste one of the subworkflows (corresponding to the method you need) from openexchangerates.yaml at the end of your workflow source code
4. Make a call to it according to the spec of a given method. See next section for details. 

<h3>Methods</h3>

# latestOpenExchangeRates

This method returns the latest echange rates for a given Base currency according to https://docs.openexchangerates.org/docs/latest-json

Parameters
- secret: name of the secret storing OpenExchangeRates appid in Secret Manager 
- base: OPTIONAL. Change base currency (3-letter code, default: USD)
- prettyprint: OPTINAL. Set to false to reduce response size (removes whitespace)
- show_alternative: OPTIONAL. Extend returned values with alternative, black market and digital currency rates.(Bool)
- symbols: OPTIONAL. Limit results to specific currencies (comma-separated list of 3-letter codes)

```yaml
main:
    steps:
      - getExchangeRate:
          call: latestOpenExchangeRates
          args:
              secret: "myOpenExchangeRates"
          result: myEchangeRates
      - theEnd:
          return: ${myEchangeRates.body}

latestOpenExchangeRates:
    # the rest of the subworkflow source code from this repo goes here...
```

# timeSeriesOpenExchangeRates

This method returns the time series echange rates for a given Base currency according to https://docs.openexchangerates.org/docs/time-series-json

Parameters
- secret: name of the secret storing OpenExchangeRates appid in Secret Manager 
- start: The time series start date in YYYY-MM-DD format
- end: The time series end date in YYYY-MM-DD format
- base: OPTIONAL. Change base currency (3-letter code, default: USD)
- prettyprint: OPTINAL. Set to false to reduce response size (removes whitespace)
- show_alternative: OPTIONAL. Extend returned values with alternative, black market and digital currency rates.(Bool)
- symbols: OPTIONAL. Limit results to specific currencies (comma-separated list of 3-letter codes)

```yaml
main:
    steps:
      - getExchangeRate:
          call: timeSeriesOpenExchangeRates
          args:
              secret: "myOpenExchangeRates"
              start: "2020-04-01"
              end: "2020-04-10"
          result: myEchangeRates
      - theEnd:
          return: ${myEchangeRates.body}

timeSeriesOpenExchangeRates:
    # the rest of the subworkflow source code from this repo goes here...
```

# historicalOpenExchangeRates

Get historical exchange rates for any date available from the Open Exchange Rates API, currently going back to 1st January 1999. It covers a call to https://docs.openexchangerates.org/docs/historical-json

Parameters
- secret: name of the secret storing OpenExchangeRates appid in Secret Manager 
- date: The requested date in YYYY-MM-DD format
- base: OPTIONAL. Change base currency (3-letter code, default: USD)
- prettyprint: OPTINAL. Set to false to reduce response size (removes whitespace)
- show_alternative: OPTIONAL. Extend returned values with alternative, black market and digital currency rates.(Bool)
- symbols: OPTIONAL. Limit results to specific currencies (comma-separated list of 3-letter codes)

```yaml
main:
    steps:
      - getExchangeRate:
          call: historicalOpenExchangeRates
          args:
              secret: "myOpenExchangeRates"
              date: "2020-06-13"
          result: myEchangeRates
      - theEnd:
          return: ${myEchangeRates.body}

historicalOpenExchangeRates:
    # the rest of the subworkflow source code from this repo goes here...
```

# ohlcOpenExchangeRates

This method returns Open, High, Low, Close exchange rates for a specific period per https://docs.openexchangerates.org/docs/ohlc-json

Parameters
- secret: name of the secret storing OpenExchangeRates appid in Secret Manager 
- start_time: The start time for the requested OHLC period (ISO-8601 format, UTC only). Restrictions apply.
- period: OPTIONAL. The requested period (starting on the start_time), e.g. "1m", "30m", "1d". Please see API spec for supported periods. Defaults to 1 day (1d).
- prettyprint: OPTINAL. Set to false to reduce response size (removes whitespace)
- base: OPTIONAL. Change base currency (3-letter code, default: USD)
- show_alternative: OPTIONAL. Extend returned values with alternative, black market and digital currency rates.(Bool)
- symbols: Limit results to specific currencies (comma-separated list of 3-letter codes)

```yaml
main:
    steps:
      - getExchangeRate:
          call: ohlcOpenExchangeRates
          args:
              secret: "myOpenExchangeRates"
              start_time: "2020-05-21"
          result: myEchangeRates
      - theEnd:
          return: ${myEchangeRates.body}

ohlcOpenExchangeRates:
    # the rest of the subworkflow source code from this repo goes here...
```

# convertOpenExchangeRates

This method returns the latest echange rates for a given Base currency according to https://docs.openexchangerates.org/docs/convert

Parameters
- secret: name of the secret storing OpenExchangeRates appid in Secret Manager 
- from: The currency code for conversion - from (e.g. USD)
- to: The currency code for conversion - to (e.g. PLN)
- value: The value that needs to be converted, e.g. 9.99
- prettyprint: OPTINAL. Set to false to reduce response size (removes whitespace)

```yaml
main:
    steps:
      - getExchangeRate:
          call: convertOpenExchangeRates
          args:
              secret: "myOpenExchangeRates"
          result: myEchangeRates
      - theEnd:
          return: ${myEchangeRates.body}

convertOpenExchangeRates:
    # the rest of the subworkflow source code from this repo goes here...
```
