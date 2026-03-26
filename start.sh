#!/bin/bash
cd /opt/render/project/src
python -m streamlit run streamlit_app.py \
  --server.port=8501 \
  --server.address=0.0.0.0
