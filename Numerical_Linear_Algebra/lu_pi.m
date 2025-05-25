function [ l,u,c,r_inch ] = lu_pi( a )
%this is the function to solve linear equation using gaussian elimination
%with partial pivoting
sz=size(a) ;
r_inch = [1:sz(1)]' ; %  to keep track of row exchange
str=time();
   for pm=1:sz(1)
       int_ind = pm;
       temp = a(pm,pm);
       for k=pm+1:sz(1)
           if(abs(temp)<abs(a(k,pm)))
               int_ind = k ;
               temp = a(k,pm);
           end
       end
       if(temp==0)
           sprintf("matrix is singular")
       elseif(int_ind ~= pm)
           v_temp = a(pm,:);
           a(pm,:) = a(int_ind,:);
           a(int_ind,:) = v_temp ;
           r_inch(pm) = int_ind ;
       end
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
c=l*u
ett=time();
llo=ett-str;
disp(llo)

end

