function [ l,u,c ] = lu_nt_pi( a )
%this function returns l u factorization of a matrix a without partial
%pivoting
sz=size(a);
str=time();
for pm = 1:sz(1)-1 % this is the submatrix positon on which we are doing operation  
    for i = pm+1:sz(1)
        a(i,pm) = a(i,pm)/a(pm,pm); %these are enteries of l matrix 
        for j = pm+1:sz(1)
            a(i,j) = -(a(i,pm))*a(pm,j) + a(i,j); %this i'th column is constructing u matrix
        end
    end
end
u = triu(a);
l = tril(a,-1);
l = l + eye(sz(1));
c=l*u;
ett=time();
llo=ett-str;
disp(llo)

end

