from app import create_app

app = create_app()
app.testing = True
app.config["PROPAGATE_EXCEPTIONS"] = True

with app.test_client() as client:
    try:
        resp = client.get("/auth/login")
        print("Status:", resp.status_code)
        print(resp.data.decode("utf-8")[:1000])
    except Exception as exc:
        import traceback
        print("EXCEPTION RAISED:\n", exc)
        traceback.print_exc()