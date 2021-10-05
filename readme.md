# An example of git workflow with rebase

Let's develop a feature locally in a separate branch

> git checkout -b feature_mult

Do some dev on that branch...

And commit it

> git commit -m "Adding a readme on git workflow"

Do some staff...

Commit and push that branch to remote


Now that I am happy with the job, I wanna check if I can rebase my feature branch based on master

==> Requires to pull the master branch first to have the latest contributions of my team

git checkout master

git pull