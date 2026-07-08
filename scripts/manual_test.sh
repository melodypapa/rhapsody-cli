#!/bin/bash
# Manual test script for element CLI operations
# Prerequisites: Rhapsody must be running with an open project
# Usage: ./scripts/manual_test.sh

CLI="python -m rhapsody_cli.cli.main"
CLASS_NAME="TestClass_$(date +%s)"  # Use timestamp for uniqueness

echo "========================================"
echo "Element CLI Manual Test"
echo "========================================"
echo ""

# Step 1: Check if CLI is available
echo "[Step 0] Checking Rhapsody connection..."
if ! $CLI element query 2>/dev/null; then
    echo "❌ ERROR: Rhapsody is not running or no project is open"
    echo ""
    echo "Prerequisites:"
    echo "  1. Start IBM Rhapsody"
    echo "  2. Open a project file"
    echo "  3. Run this script again"
    echo ""
    echo "To run unit tests instead (without Rhapsody):"
    echo "  pytest tests/cli/test_element_commands.py -v"
    exit 1
fi
echo "✓ Rhapsody connection verified"
echo ""

# Step 1: List elements before adding
echo "[Step 1] Query existing elements..."
if ! $CLI element query; then
    echo "❌ ERROR: Query failed"
    exit 1
fi
echo "✓ Query succeeded"
echo ""

# Step 2: Add a new class
echo "[Step 2] Adding new class: $CLASS_NAME..."
if ! $CLI element add --type class --name "$CLASS_NAME"; then
    echo "❌ ERROR: Failed to add class"
    exit 1
fi
echo "✓ Class added successfully"
echo ""

# Step 3: Query and verify the class is there
echo "[Step 3] Verifying class exists in project..."
if $CLI element query | grep -q "$CLASS_NAME"; then
    echo "✓ Class '$CLASS_NAME' found in query results"
else
    echo "❌ ERROR: Class '$CLASS_NAME' NOT found in query results"
    exit 1
fi
echo ""

# Step 4: Delete the class
echo "[Step 4] Deleting class: $CLASS_NAME..."
if ! $CLI element delete --path "Root::$CLASS_NAME"; then
    echo "❌ ERROR: Failed to delete class"
    exit 1
fi
echo "✓ Class deleted successfully"
echo ""

# Step 5: Query and verify the class is gone
echo "[Step 5] Verifying class was deleted..."
if $CLI element query | grep -q "$CLASS_NAME"; then
    echo "❌ ERROR: Class '$CLASS_NAME' STILL found (deletion may have failed)"
    exit 1
else
    echo "✓ Class '$CLASS_NAME' no longer in query results (successfully deleted)"
fi
echo ""

echo "========================================"
echo "✓ All manual tests PASSED!"
echo "========================================"
