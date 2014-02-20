import copy
import re 
import CMGTools.RootTools.fwlite.Config as cfg

Radion300 = cfg.MCComponent(
    name = 'Radion300',
    files = [],
    xSection = None, 
    nGenEvents = 200000, ## problem with publish.py
    triggers = [],
    effCorrFactor = 1 )

Radion500 = cfg.MCComponent(
    name = 'Radion500',
    files = [],
    xSection = None, 
    nGenEvents = 200000, ## problem with publish.py
    triggers = [],
    effCorrFactor = 1 )

Radion700 = cfg.MCComponent(
    name = 'Radion700',
    files = [],
    xSection = None, 
    nGenEvents = 200000, ## problem with publish.py
    triggers = [],
    effCorrFactor = 1 )

#############

mc_radion = [
    Radion300,
    Radion500,
    Radion700,
    ]
