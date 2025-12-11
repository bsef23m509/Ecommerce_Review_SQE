#!/usr/bin/env bash

# Activate virtual environment
source .venv/bin/activate

# Create timestamped report folder
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_DIR="performance_reports/$TIMESTAMP"
mkdir -p "$REPORT_DIR"

# Start the FastAPI app
uvicorn app.main:app --port 8000 --host 127.0.0.1 &
APP_PID=$!
sleep 1

echo "--------------------------------------"
echo " Running Performance Tests "
echo "--------------------------------------"

BASE_URL="http://localhost:8000"

# Markdown report header
echo "# Performance Test Report" > "$REPORT_DIR/report.md"
echo "" >> "$REPORT_DIR/report.md"
echo "**Generated:** $(date)" >> "$REPORT_DIR/report.md"
echo "" >> "$REPORT_DIR/report.md"
echo "---" >> "$REPORT_DIR/report.md"
echo "" >> "$REPORT_DIR/report.md"

# Function to run AB and save output + inject into markdown
run_test() {
    NAME=$1
    DISPLAY_NAME=$2
    CMD=$3

    RAW_FILE="$REPORT_DIR/${NAME}.txt"

    echo "Running test: $DISPLAY_NAME"

    # Add test title in markdown
    echo "## $DISPLAY_NAME" >> "$REPORT_DIR/report.md"
    echo "" >> "$REPORT_DIR/report.md"
    echo "Command:" >> "$REPORT_DIR/report.md"
    echo "\`$CMD\`" >> "$REPORT_DIR/report.md"
    echo "" >> "$REPORT_DIR/report.md"
    echo "### Results" >> "$REPORT_DIR/report.md"
    echo '```' >> "$REPORT_DIR/report.md"

    # Run the ab command
    eval "$CMD" 2>&1 | tee "$RAW_FILE" | tee -a "$REPORT_DIR/report.md"

    echo '```' >> "$REPORT_DIR/report.md"
    echo "" >> "$REPORT_DIR/report.md"
    echo "---" >> "$REPORT_DIR/report.md"
    echo "" >> "$REPORT_DIR/report.md"
}

# Test 1: GET /api/products
run_test "GET_all_products" \
    "GET /api/products" \
    "ab -n 100 -c 10 $BASE_URL/api/products"

# Test 2: GET /api/products/1
run_test "GET_product_1" \
    "GET /api/products/1" \
    "ab -n 100 -c 10 $BASE_URL/api/products/1"

# Test 3: POST /product/1/reviews
POSTDATA=$(mktemp)
echo "review=performance+test&rating=5" > $POSTDATA

run_test "POST_review" \
    "POST /product/1/reviews" \
    "ab -n 50 -c 5 -p $POSTDATA -T 'application/x-www-form-urlencoded' $BASE_URL/product/1/reviews"

rm $POSTDATA

echo "--------------------------------------"
echo " Performance Tests Completed "
echo "--------------------------------------"

# Stop FastAPI server
kill $APP_PID

# Final report footer
echo "" >> "$REPORT_DIR/report.md"
echo "---" >> "$REPORT_DIR/report.md"
echo "**End of Report**" >> "$REPORT_DIR/report.md"

echo ""
echo "Markdown report created at:"
echo "$REPORT_DIR/report.md"
echo ""
