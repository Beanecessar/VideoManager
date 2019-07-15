@echo off
setlocal EnableDelayedExpansion
for %%f in (*.ui) do (
SET n=%%f
pyuic5 -i 0 !n! -o !n:.ui=UI.py!
)