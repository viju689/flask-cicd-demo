# 🖥️
cat > app.py << 'EOF'
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(status="ok", message="Hello from Flask + Docker + GitHub Actions!")

if __name__ == "__main__":
    # local dev only (prod uses gunicorn)
    app.run(host="0.0.0.0", port=5000)
EOF
