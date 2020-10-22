#!/usr/bin/env bash
rm -f outputs/sample_output
rm -f outputs/output
cat inputs/sample_input | python3 app.py > outputs/sample_output
cat inputs/input | python3 app.py > outputs/output