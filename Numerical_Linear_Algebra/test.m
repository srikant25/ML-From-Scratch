% f = @(x,m,n) reshape(randperm(x),m,n);
% a=f(100,10,10);
 %frob(a)
 %chole(a);
 
%n=500; 
%A = rand(n,n);

%A = 0.5*(A+A'); 



%A = A + n*eye(n);
%choles(A);

S = load('gre_1107.mat');


s=S.Problem;
A=s.A;
inf_narm(A);


%n = 100;
%a = rand(n-1,1);
%b =rand(n,1);
%c = rand(n-1,1);
%y=rand(n,1);
%thomasa(a,b,c,y);
%A = createtri(a,b,c);
%y=rand(n,1);
%x0=zeros(n,1);
%luwopivot(A);
%ludecompvt(A);
%fbb(A);
%jacobi(A,y,x0,0.001,5000);
