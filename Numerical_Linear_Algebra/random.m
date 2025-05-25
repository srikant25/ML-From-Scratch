f = @(x,m,n) reshape(randperm(x),m,n);
a=f(100,10,10);
%frob(a)
choles(a);
