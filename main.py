import os
import time

class basicUtility():
    def cmd(self, command):
        os.system(command)
    def wait(self, seconds):
        time.sleep(seconds)

basic = basicUtility()

class gitAndGhCommand():
    def gitInit(self):
        basic.cmd("git init")
        basic.cmd("cls")
        print("Successfully initialized the git project")
    def commitAll(self, msg):
        basic.cmd(f'git commit -a -m "{msg}"')
        basic.cmd("cls")
        basic.cmd(f"git status")
        print("Successfully committed to local repository")
    def stage(self, fileOrFolderName):
        basic.cmd(f"git add {fileOrFolderName}")
        basic.cmd("cls")
        basic.cmd("status")
        print(f"Successfully stages {fileOrFolderName}")
    def commit(self, msg):
        basic.cmd("cls")
        basic.cmd(f"git commit -m {msg}")
        basic.cmd("cls")
        basic.cmd(f"git status")
        print("Successfully committed to local repository")
    def addRemoteRepo(self, url):
        basic.cmd("cls")
        basic.cmd(f"git remote add origin {url}")
        basic.cmd("cls")
        basic.cmd(f"git status")
        basic.cmd(f"Successfully set the remote repository to {url}")
    def setRemoteBranch(self, branchName):
        basic.cmd("cls")
        basic.cmd(f"git branch -M {branchName}")
        basic.cmd("cls")
        basic.cmd("git status")
        basic.cmd(f"Successfully set the remote branch to {branchName}")
    def commitInRemoteRepository(self):
        basic.cmd("cls")
        basic.cmd(f"git push -u origin")
        basic.cmd("cls")
        basic.cmd("git status")
        basic.cmd(f"Successfully committed the remote repository")

gitAndGhCommand().commitAll("Initial commit")