
# Grafana Logger

An HTTP based library that can post logs to grafana with tags. This allows you to use
grafana's powerfull LogQL system to query logs in the dashboard and set up alerts.



## Logging
To avoid configuring additional log forwarding services. GLogger use the http API to directly 
post logs to grafana cloud in a syntax that is similar to Python's inbuilt logger. 

Along with posting logs to grafana, it also prints out the logs in console to enable fast debugging without having to go the cloud.

### Initializing the logger class

```python
  from Glogger import Loki
  logger = Loki()
  logger = Loki(url='api_url')
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_url` | `string` | **Required**. Your API url |

#### Post Info

```python
  logger.info(message, **tags)
  logger.info(message, id='xyx', cloudProvider='aws', env='test')
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tags`      | `key value pairs` | **Required**. At least on tag required to query in Cloud. |

#### Post Warning

```python
  logger.warning(message, **tags)
  logger.warning(message, id='xyx', cloudProvider='aws', env='test')
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tags`      | `key value pairs` | **Required**. At least on tag required to query in Cloud. |

#### Post Error

```python
  logger.error(message, **tags)
  logger.error(message, id='xyx', cloudProvider='aws', env='test')
```
Error method automatically appends the stack trace and the exception of the current exception that has occured.

This method can only be inside an except clause.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tags`      | `key value pairs` | **Required**. At least on tag required to query in Cloud. |
