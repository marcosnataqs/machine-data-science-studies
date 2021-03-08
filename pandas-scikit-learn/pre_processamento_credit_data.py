#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:15:15 2021

@author: marcosnqs
"""

import pandas as pd
base = pd.read_csv('credit_data.csv')
base.describe()