function [ x ] = ford_sub( mat,y )
%this gives backward substitution result
str=time();
sz=size(mat);
x=zeros(sz(1),1);
for n=1:sz(2)
    temp=0;
    if (n~=1)
    for i=1:n-1
        temp=temp+mat(n,i)*x(i);
    end
    end
    x(n)=(y(n)-temp)/mat(n,n);
end

ett=time();
llo=ett-str;
disp(llo)

end

