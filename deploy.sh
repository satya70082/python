#!/bin/bash

# Stop running app (if any)
pkill -f "python3 app.py"

# Start the application
nohup python3 app.py > app.log 2>&1 &
echo "Application deployed and running!"
