# setup.sh
#!/usr/bin/env bash
set -e
echo "📦 Installing project in editable mode..."
uv pip install -e .
echo "✅ Done!"