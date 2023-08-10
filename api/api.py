from flask import render_template, Blueprint, redirect, request, url_for, flash
import imp


def sterm_loader():
    return 0