@echo off
title Mahouo-Analytics
call env\scripts\activate
call cd sever
call python manager.py
cmd/k