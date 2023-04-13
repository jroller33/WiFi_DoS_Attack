# this is running on kali linux

# subprocess module for running commands on kali
import subprocess

import re
import csv
import os
import time
from datetime import datetime

import shutil

active_wifi_networks = []


