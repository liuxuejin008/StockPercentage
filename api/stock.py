from sanic import Sanic
from sanic.response import json
from api.util import Util

app = Sanic("stock")

@app.post('/stock')
async def stock(request):
    start_date = request.form.get("startDate")
    end_data = request.form.get("endDate")
    name = request.form.get("name")
    if not name:
        name = "AAPL"
    nlist = Util.get_percent(start_date, end_data, name)
    return json({"list": nlist})


# if __name__ == "__main__":
# app.run(host="0.0.0.0", port=8088)
