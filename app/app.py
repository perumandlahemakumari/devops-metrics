from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    conn = psycopg2.connect("dbname=devops user=admin password=pass host=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 10;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

