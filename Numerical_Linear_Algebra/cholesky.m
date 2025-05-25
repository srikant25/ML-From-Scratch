A=[5 1 2; 5 4 7; 4 8 2];
[r,c]=size(A);
a=A;
n=r;
if r<=1
	exit;
end
sum=0;
R=zeros(r,c);

R(1,1)=sqrt(a(1,1));
R(1,:)=a(1,:)/R(1,1);
for i=2:n
	sum=0;
	for j=1:i-1
		sum = sum + (R(j,i)*R(j,i));
	end
        R(i,i) = sqrt(a(i,i) - sum);	

	for j=i+1:n
sum=0;
		if i==j
			sum = R(1,i-1)'*R(1,i-1); 
			R(i,j)=sqrt(a(i,j)-sum);
		
		else
			sum=R(1:i-1,i)'*R(1:i-1,j);
			R(i,j)=(a(i,j)-sum);
			R(i,j)=R(i,j)/R(i,i);
		end
	end
end
R
