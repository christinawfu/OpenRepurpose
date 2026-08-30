#!/bin/bash

echo "=========================================="
echo "       OpenRepurpose Evidence Demo"
echo "=========================================="

echo ""
echo "Target:   PCSK9"
echo "Drug:     Evolocumab"
echo "Disease:  Hypercholesterolemia"
echo ""

echo "Running evidence-generation workflow..."
echo ""

python3 -m dossier_generator.agent \
    --target PCSK9 \
    --drug evolocumab \
    --disease hypercholesterolemia \
    --output demo/output

echo ""
echo "=========================================="
echo "Demo complete."
echo "=========================================="

echo ""
echo "Generated files:"
echo ""

ls -lh demo/output/