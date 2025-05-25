function[an]=inf_narm(a)
str=time();
sz=size(a);
a=abs(a);
sum_row=sum(a,2);
max_row=max(sum_row);
an=max_row;

ett=time();
llo=ett-str;
disp(llo);






end