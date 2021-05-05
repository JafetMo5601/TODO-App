from app import createApp
import os

app = createApp()
app.run(port=5000, threaded=True, debug=(os.environ.get("DEBUG") == "True"))