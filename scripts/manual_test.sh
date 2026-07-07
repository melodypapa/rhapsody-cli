#!/bin/bash
# Manual test script for element CLI operations
# Prerequisites: Rhapsody must be running with an open project
# Usage: ./scripts/manual_test.sh

set -e  # Exit on first error

CLI="python -m rhapsody_cli.cli.main"
CLASS_NAME="TestClass_$(date +%s)"  # Use timestamp for uniqueness

echo "========================================"
echo "Element CLI Manual Test"
echo "========================================"
echo ""

# Step 1: List elements before adding
echo "[Step 1] Query existing elements..."
$CLI element query
echo "✓ Query succeeded"
echo ""

# Step 2: Add a new class
echo "[Step 2] Adding new class: $CLASS_NAME..."
$CLI element add --type class --name "$CLASS_NAME"
echo "✓ Class added successfully"
echo ""

# Step 3: Query and verify the class is there
echo "[Step 3] Verifying class exists in project..."
if $CLI element query | grep -q "$CLASS_NAME"; then
    echo "✓ Class '$CLASS_NAME' found in query results"
else
    echo "✗ ERROR: Class '$CLASS_NAME' NOT found in query results"
    exit 1
fi
echo ""

# Step 4: Delete the class
echo "[Step 4] Deleting class: $CLASS_NAME..."
$CLI element delete --path "Root::$CLASS_NAME"
echo "✓ Class deleted successfully"
echo ""

# Step 5: Query and verify the class is gone
echo "[Step 5] Verifying class was deleted..."
if $CLI element query | grep -q "$CLASS_NAME"; then
    echo "✗ ERROR: Class '$CLASS_NAME' STILL found (deletion may have failed)"
    exit 1
else
    echo "✓ Class '$CLASS_NAME' no longer in query results (successfully deleted)"
fi
echo ""

echo "========================================"
echo "✓ All manual tests PASSED!"
echo "========================================"
