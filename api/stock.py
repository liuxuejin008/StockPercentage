from sanic import Sanic, json

from api.util import Util

app = Sanic("stock")

@app.get('/stock')
async def index(request):
    start_date = request.form.get("startDate")
    end_data = request.form.get("endDate")
    name = request.form.get("name")
    nlist = Util.get_percent(start_date, end_data, name)
    return json({"list":nlist})