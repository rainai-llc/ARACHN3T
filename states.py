#!/usr/bin/env python3
#
# Scientist: Jeremiah Jackson-Williams
#
# Copy Right: Rainai Inc 2025

class nState:
    def __init__(self) -> float|int:
        self.sState=-1.00
        self.kState=self.sState
    def stateSelf(self) -> float | int:
        return self.kState

class stateZero:
    def __init__(self) -> float|int:
        self.sState=0.00
        self.kState=self.sState
    def stateSelf(self) -> float | int:
        return self.kState

class stateOne:
    def __init__(self) -> float | int:
        self.sState=1.00
        self.kState=self.sState
    def stateSelf(self) -> float | int:
        return self.nState
