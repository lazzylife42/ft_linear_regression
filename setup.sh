#!/bin/bash

# Check et install pip3
if command -v pip3 &> /dev/null; then
    echo "pip3 OK"
else
    echo "pip3 manquant, installation..."
    curl -s https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
    python3 /tmp/get-pip.py --user
    rm /tmp/get-pip.py
    export PATH="$HOME/.local/bin:$PATH"
fi

# Check et cree venv
if [ -d "venv" ]; then
    echo "venv OK"
else
    echo "Creation du venv..."
    python3 -m venv venv
fi

# Active le venv
source venv/bin/activate

# Check et install requirements
if [ -f "requirements.txt" ]; then
    echo "Installation des requirements..."
    pip install -r requirements.txt
else
    echo "Pas de requirements.txt, installation des packages de base..."
    pip install jupyter matplotlib pandas numpy
fi

echo "Setup termine. Venv active."
echo "Pour lancer jupyter: jupyter notebook"

python3