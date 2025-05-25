function[an]=one_norm(a)
str=time();
a=abs(a)
sz=size(a);
sum_row=sum(a,1);
max_row=max(sum_row);
an=max_row;
an
ett=time();
llo=ett-str;
disp(llo)

end