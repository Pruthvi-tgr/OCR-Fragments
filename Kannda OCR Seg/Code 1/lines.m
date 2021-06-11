function [fl,re,row]=lines(im_text)
[im_texto,r]=clip_r(im_text);
num_filas=size(im_texto,1);
for s=1:num_filas
    if sum(im_texto(s,:))==0
        nm=im_texto(1:s-1, :); % First line matrix
        re=im_texto(s:end, :);% Remain line matrix
%        [fl,r1,r2,c1,c2] = clip(nm);
%        [re]=clip(rm);
        break
    else
        fl=im_texto;%Only one line.
        re=[ ];
    end
end
row=r+s;


function [img_out,r]=clip_r(img_in)
[f,c]=find(img_in);
r=min(f);
img_out=img_in(min(f):max(f),min(c):max(c));%Crops image

function [img_out]=clip(img_in)
[f,c]=find(img_in);
img_out=img_in(min(f):max(f),min(c):max(c));%Crops image