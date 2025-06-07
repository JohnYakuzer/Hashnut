#!/bin/bash

INSTALL_DIR="$HOME/.local/bin"
SCRIPT_NAME="hashnut"

PROJECT_DIR="$(pwd)"

mkdir -p "$INSTALL_DIR"

cat > "$INSTALL_DIR/$SCRIPT_NAME" <<EOF
#!/bin/bash
python3 "$PROJECT_DIR/main.py" "\$@"
EOF

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc
    echo "[+] Added $INSTALL_DIR to PATH in ~/.bashrc"
else
    echo "[*] $INSTALL_DIR is already in PATH"
fi

echo "[+] Installation done! Program is ready to use."

