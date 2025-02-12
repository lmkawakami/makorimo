import marimo

__generated_with = "0.11.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
async def _():
    import micropip
    await micropip.install('influxdb-client')
    await micropip.install('ssl')
    return (micropip,)


@app.cell
def _():
    import influxdb_client, os, time
    from influxdb_client import InfluxDBClient, Point, WritePrecision
    from influxdb_client.client.write_api import SYNCHRONOUS

    token="bRsS5n3qyCV7ZX7gxsPn15YR7OlW__Ak-bl1fpaxaz0arL_pPMaskYCt8czqOlC2xD-JdqmaUKgq_XnRb3Fb4Q=="
    org = "danko_corp"
    url = "http://192.168.0.3:8086"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    return (
        InfluxDBClient,
        Point,
        SYNCHRONOUS,
        WritePrecision,
        client,
        influxdb_client,
        org,
        os,
        time,
        token,
        url,
    )


@app.cell
def _(Point, SYNCHRONOUS, client, time):
    bucket="danko_bucket"

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for value in range(5):
      point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
      )
      write_api.write(bucket=bucket, org="danko_corp", record=point)
      time.sleep(1) # separate points by 1 second
    return bucket, point, value, write_api


@app.cell
def _(client):
    query_api = client.query_api()

    query = """from(bucket: "danko_bucket")
     |> range(start: -15m)
     |> filter(fn: (r) => r["_measurement"] == "kilns")
     |> aggregateWindow(every: 5s, fn: mean, createEmpty: false)
    """
    tables = query_api.query(query, org="danko_corp")

    data = []
    for table in tables:
      for record in table.records:
        data.append({
            "time": record["_time"],
            "measurement": record["_measurement"],
            "field": record["_field"],
            "value": record["_value"],
            "kiln": record["kiln"],
            "location": record["location"],
            "serial": record["serial"],
            "start_date": record["start_date"],
            "type": record["type"]
        })
    return data, query, query_api, record, table, tables


@app.cell
def _(data):
    import pandas as pd
    df= pd.DataFrame(data)
    df = pd.pivot_table(df, values="value", index="time", columns="field")
    df.index = df.index.tz_convert("America/Sao_Paulo")
    df
    return df, pd


if __name__ == "__main__":
    app.run()
