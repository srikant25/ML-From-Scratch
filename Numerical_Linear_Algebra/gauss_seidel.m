function[X]=gauss_seidel(A,b,numiter)
n=1;
[r,c]=size(A);
a=A;
x=zeros(c,1);
x1=zeros(c,1);
d=1;
str=time();
while(n<=numiter & d >= 10^(-4))
	for i=1:c
		x1;
		sum1=a(i,:)*x(:,1);
		sum1=sum1-a(i,i)*x(i,1);
		sum1;
		x1(i,1)=b(i,1)-sum1;
		x1(i,1)=x1(i,1)./(a(i,i));
		x=x1
		d=abs(x1-x);
	end
	n=n+1;
end	
X=x;
ett=time();
llo=ett-str;
disp(llo)

end
