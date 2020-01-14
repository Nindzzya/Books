ssh-keygen.exe
cat ~/.ssh/id_rsa.pub

git init
git status
git add .
git commit -m "fd"
git push
git push -f


Еor create a new repository on the command line

echo "# Books" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Nindzzya/Books.git
git push -u origin master

Еor push an existing repository from the command line

git remote add origin https://github.com/Nindzzya/Books.git
git push -u origin master

git pull origin master, а потом git push origin master, если всЄ ок.

1