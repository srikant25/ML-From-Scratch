function tridigonal(a,b,c)
u(1)=b(1)
for i=1:n-1 
  l(i)=a(i)/u(i);
  u(i+1) = b(i+1)-l(i)*c(i);
    
end

