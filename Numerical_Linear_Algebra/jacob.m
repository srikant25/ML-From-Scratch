%function [ xn,count ] = jacob( mat_A,b )
%jacobian method for solving linear equation iteratively
a = dlmread('pos_def')
mat = diagon_zero([mat_A,b])
b = mat(:,end);
mat_A = mat(:,1:end-1);
str=time();
sz = size(mat_A);
dig = (diag((diag(mat_A)).^-1));
mat_M = mat_A-diag(diag(mat_A));
xo = zeros(sz(1),1);
xn = ones(sz(1),1);
mat_C = abs(mat_A);
c_dig = diag(mat_C);
sum_c_col = sum(mat_C,1)';
sum_c_col = sum_c_col - c_dig;
sum_c_row = sum(mat_C,2);
sum_c_row = sum_c_row - c_dig;
count = 0 ;
     for i=1:sz(1)
         temp = 0 ;
        if (c_dig(i) > sum_c_row(i) && c_dig(i) > sum_c_col(i) )
            temp = temp + 1;
        else
            sprintf("Jacobi method may converge")
        end
     end
     if (temp == sz(1))
         sprintf("Jacobi method will definetely converge because satisfying strong conditon")
     elseif (max(abs(eig(mat_A))) > 1)
         sprintf("Jacobi method will not converge")
         return
%      else 
%          sprintf("Jacobi method will not converge")
     end
     while((norm(b-mat_A*xo)/norm(b))>0.00001)
%          xo = xn ;
%          xn=dig*(b-mat_M*xo) ;
%          count =  count+1 ;
% %          xo = xn ;
          for i = 1 : sz(2)
               mat_M(i, :)*xo
              xn(i) = dig(i, i)*(b(i) - mat_M(i, :)*xo ) ;
          end
          xo = xn ;
     end
     xn ; 
     count ;

ett=time();
llo=ett-str;
disp(llo)



