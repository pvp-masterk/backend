from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="your_host",
    port="5432"
)

@app.route("/api/verify", methods=["GET"])
def verify():
    code = request.args.get("code", "")
    cur = conn.cursor()

    cur.execute("SELECT username FROM discord_links WHERE code = %s", (code,))
    row = cur.fetchone()

    if row:
        return jsonify({"success": True, "username": row[0]})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run()
