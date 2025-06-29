curl -X PUT \
  -u admin:root \
  http://localhost:5984/notes_db/_design/app \
  --data-binary @app_design.json \
  -H "Content-Type: application/json"