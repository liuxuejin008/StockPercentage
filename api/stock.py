from sanic import Sanic
from api.util import Util

app = Sanic()

@app.post('/stock')
async def index(request, path=""):
    start_date = request.form.get("startDate")
    end_data = request.form.get("endDate")
    name = request.form.get("name")
    nlist = Util.get_percent(start_date, end_data, name)
    return nlist
