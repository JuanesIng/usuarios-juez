echo "Waiting for PostgreSQL to be available..."
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL is ready. Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
