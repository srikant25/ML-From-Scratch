function [ a ] = diagon_zero( a )
%this is the function to remove non zero entery from diagonal of matix by
%row exchange
sz=size(a)
i=1;
if(sz(1)+1==sz(2))
    while(i~=sz(1))
    if(a(i,i)~=0)
        i=i+1;
    else
        c=0;
        for j=1:sz(1)
            c=c+1;
            if(a(i,j)~=0 && a(j,i)~=0)
                temp = a(i,:) ;
                a(i,:) = a(j,:) ;
                a(j,:) = temp ;
                i=i+1;
                break
            end            
        end
        if(c==sz(1))
            sprintf("the matrix is not good");     
            
        end          
    end
    end
else
    sprintf("the matrix dimension are not correct");
end
end
            
        
        




