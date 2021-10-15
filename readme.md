# An example of git workflow with rebase

Let's develop a feature locally in a separate branch

> git checkout -b feature_mult

Do some dev on that branch...

And commit it

> git commit -m "Adding a readme on git workflow"

Do some staff...

Commit and push that branch to remote

> git push


Now that I am happy with the job, I wanna check if I can rebase my feature branch based on main

==> Requires to pull the main branch first to have the latest contributions of my team

> git checkout main

> git pull  (with a rebase)

My main can be one or more commits ahead (my feature branch one or more commits behind)

> git checkout feature_mult

> git rebase main

before pushing, update the feature branch

git pull (with a rebase)

If everything is OK, push the feature branch to remote repo

git push