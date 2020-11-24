#!/bin/bash

cp xwaf.clean xwaf.php
python3 regras.py $1 >> xwaf.php
cat tail.txt >> xwaf.php
