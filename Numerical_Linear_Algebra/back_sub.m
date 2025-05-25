function [ x ] = back_sub( mat,y )
%this gives backward substitution result
sz=size(mat);
x=zeros(sz(1),1);
k=sz(1);
str=time();
for n=k:-1:1
    temp=0;
    if (n~=sz(2))
    for i= n+1:sz(2)
        temp=temp+mat(n,i)*x(i);
    end
    end
    x(n)=(y(n)-temp)/mat(n,n);
end

ett=time();
llo=ett-str;
disp(llo)

end

