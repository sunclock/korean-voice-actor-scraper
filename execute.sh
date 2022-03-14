#!/bin/bash
echo "start scraping" && python3 actors.py && python3 dramas_aco.py &&python3 dramas_yahe.py && python3 dramas_haeming.py &&python3 match.py && echo "end scraping"
