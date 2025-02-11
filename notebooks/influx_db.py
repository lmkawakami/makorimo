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
    return (micropip,)


@app.cell
def _():
    import influxdb_client, os, time
    from influxdb_client import InfluxDBClient, Point, WritePrecision
    from influxdb_client.client.write_api import SYNCHRONOUS

    token="bRsS5n3qyCV7ZX7gxsPn15YR7OlW__Ak-bl1fpaxaz0arL_pPMaskYCt8czqOlC2xD-JdqmaUKgq_XnRb3Fb4Q=="
    org = "danko_corp"
    url = "http://192.168.0.3:8086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    return (
        InfluxDBClient,
        Point,
        SYNCHRONOUS,
        WritePrecision,
        influxdb_client,
        org,
        os,
        time,
        token,
        url,
        write_client,
    )


@app.cell
def _():
    # from influxdb_client import InfluxDBClient, Point
    # from influxdb_client.client.write_api import SYNCHRONOUS

    # INFLUXDB_TOKEN="bRsS5n3qyCV7ZX7gxsPn15YR7OlW__Ak-bl1fpaxaz0arL_pPMaskYCt8czqOlC2xD-JdqmaUKgq_XnRb3Fb4Q=="
    # org = "danko_corp"
    # url = "http://192.168.0.3:8086"

    # client = InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org")

    # write_api = client.write_api(write_options=SYNCHRONOUS)
    # query_api = client.query_api()

    # p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

    # write_api.write(bucket=bucket, record=p)

    # ## using Table structure
    # tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

    # for table in tables:
    #     print(table)
    #     for row in table.records:
    #         print (row.values)


    # ## using csv library
    # csv_result = query_api.query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
    # val_count = 0
    # for row in csv_result:
    #     for cell in row:
    #         val_count += 1
    return


if __name__ == "__main__":
    app.run()
