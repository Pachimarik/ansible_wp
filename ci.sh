#!/bin/bash
export $(cat  variables | xargs)

python3 entrypoint.py