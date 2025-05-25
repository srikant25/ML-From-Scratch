function [x,iter,relresid] = sors(A,b,x0,w,tol,iterm)
[m,n] = size(A);
k = 1;
x = x0;
str=time();
for k = 1:iterm
	x(1) = w*(1.0/A(1,1))*(b(1) - A(1,2:n)*x(2:n)) + (1-w)*x(1);
	for i = 2:n-1
		x(i) = w*(1.0/A(i,i))*(b(i)-A(i,1:i-1)*x(1:i-1)-A(i,i+1:n)*x(i+1:n)) + (1-w)*x(i);
	end
	x(n) = w*(1.0/A(n,n))*(b(n) - A(n,1:n-1)*x(1:n-1)) + (1-w)*x(n);
   relresid = norm(b - A*x)/norm(b);
	if relresid < tol
		iter = k
		return;
	end

iter = -1;

ett=time();
llo=ett-str;
disp(llo)

end