function x = thomasa(a,b,temp,rhs)


n = length(b);
x = zeros(n,1);

temp(1) = temp(1)/b(1);
rhs(1) = rhs(1)/b(1);
str=time()
for i = 2:n-1
    temp(i) = temp(i)/(b(i)-a(i-1)*temp(i-1));
    rhs(i)=(rhs(i)-a(i-1)*rhs(i-1))/(b(i)-a(i-1)*temp(i-1));
end
rhs(n)=(rhs(n)-a(n-1)*rhs(n-1))/(b(n)-a(n-1)*temp(n-1));

x(n) = rhs(n);
for i = n-1:-1:1
    x(i) = rhs(i)-temp(i)*x(i+1);
end

ett=time();
llo=ett-str;
disp(llo)

end