import os.path

from invoke import task

@task
def lint(c):
    "run all the lints"
    js_lint(c)

@task
def js_lint(c):
    "eslint the things"
    if not os.path.exists("node_modules"):
        c.run("npm i")
    files = ""
    for x in ["password", "tagger", "complaint", "incidentAddButtons"]:
        files = files  + " " + "OpenOversight/app/static/js/{}.js".format(x)
    c.run("node_modules/.bin/eslint {}".format(files))

@task
def jinja_lint(c):
    c.run("jinjalint OpenOversight/app/templates")