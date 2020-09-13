# Open Weather Map connector for Google Workflows
Open source connector for OpenWeatherMap API. 

<h3>Overview</h3>

It supports the following methods
- [Current Weather Data - openWeatherMapCurrent](#openWeatherMapCurrent)
- [Hourly Forecast 4 days - openWeatherMapHourlyForecast](#openWeatherMapHourlyForecast)
- [Daily Forecast 16 days - openWeatherMapDailyForecast](#openWeatherMapDailyForecast)
- [Climatic Forecast 30 days - openWeatherMapClimaticForecast](#openWeatherMapClimaticForecast)
- [5 Day / 3 Hour Forecast - openWeatherMap5DayForecast](#openWeatherMap5DayForecast)


<br>
<h3>Usage</h3>

**OpenWeathMap**

1. Register at OpenWeatherMap and obtain an appid key.

**Google Cloud**

1. Create new or edit Service Account that you will use when deploying your workflow. Assign it a "Secret Manager Secret Accessor" role.
2. Create a new Secret in Secret Manager to store the appid you got in OpenWeatherMap preparation step
3. Copy and paste one of the subworkflows (corresponding to the method you need) from openweathermap.yaml at the end of your workflow source code
4. Make a call to it according to the spec of a given method. See next section for details. 

<h3>Methods</h3>

# openWeatherMapCurrent

This method returns the current weather data for a given location according to https://openweathermap.org/current

Parameters
- secret: name of the secret storing OpenWeatherMap appid in Secret Manager 
- location: location for which the weather data is to be retrieved

```yaml
main:
    steps:
      - getWeather:
          call: openWeatherMapCurrent
          args:
              location: "Warsaw,Poland"
              secret: "MyOpenWeatherAppId"
          result: currentWeather
      - theEnd:
          return: ${currentWeather.body}

openWeatherMapCurrent:
    # the rest of the subworkflow source code from this repo goes here...
```

# openWeatherMapHourlyForecast

This method returns hourly forecast weather data for a given location according to https://openweathermap.org/api/hourly-forecast

Parameters
- secret: name of the secret storing OpenWeatherMap appid in Secret Manager 
- location: location for which the weather data is to be retrieved

```yaml
main:
    steps:
      - getWeather:
          call: openWeatherMapHourlyForecast
          args:
              location: "Warsaw,Poland"
              secret: "MyOpenWeatherAppId"
          result: currentWeather
      - theEnd:
          return: ${currentWeather.body}

openWeatherMapHourlyForecast:
    # the rest of the subworkflow source code from this repo goes here...
```

# openWeatherMapDailyForecast

This method returns daily forecast weather data for up to 16 days for a given location according to https://openweathermap.org/forecast16

Parameters
- secret: name of the secret storing OpenWeatherMap appid in Secret Manager 
- location: location for which the weather data is to be retrieved
- count: number of days for which the forecast is to be retrieved (1 to 16, at the time of writing this doc)

```yaml
main:
    steps:
      - getWeather:
          call: openWeatherMapDailyForecast
          args:
              location: "Warsaw,Poland"
              secret: "MyOpenWeatherAppId"
              count: 16
          result: currentWeather
      - theEnd:
          return: ${currentWeather.body}

openWeatherMapDailyForecast:
    # the rest of the subworkflow source code from this repo goes here...
```

# openWeatherMapClimaticForecast

This method returns 30 day climatic forecast for a given location according to https://openweathermap.org/api/forecast30

Parameters
- secret: name of the secret storing OpenWeatherMap appid in Secret Manager 
- location: location for which the weather data is to be retrieved

```yaml
main:
    steps:
      - getWeather:
          call: openWeatherMapClimaticForecast
          args:
              location: "Warsaw,Poland"
              secret: "MyOpenWeatherAppId"
          result: currentWeather
      - theEnd:
          return: ${currentWeather.body}

openWeatherMapClimaticForecast:
    # the rest of the subworkflow source code from this repo goes here...
```


# openWeatherMap5DayForecast

This method returns 5 day/3 hour forecast for a given location according to https://openweathermap.org/forecast5

Parameters
- secret: name of the secret storing OpenWeatherMap appid in Secret Manager 
- location: location for which the weather data is to be retrieved

```yaml
main:
    steps:
      - getWeather:
          call: openWeatherMap5DayForecast
          args:
              location: "Warsaw,Poland"
              secret: "MyOpenWeatherAppId"
          result: currentWeather
      - theEnd:
          return: ${currentWeather.body}

openWeatherMap5DayForecast:
    # the rest of the subworkflow source code from this repo goes here...
```