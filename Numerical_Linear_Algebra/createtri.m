function A = createtri(a,b,c)
% Construct tridiagonal matrix from three vectors
 
A1 = diag(a,1);
A2 = diag(b);
A3 = diag(c,-1);
A = A1+A2+A3;
 
 
 
end