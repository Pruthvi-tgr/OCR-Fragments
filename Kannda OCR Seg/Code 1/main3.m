% Clear all
clc, close all, clear all
% Read image
[file,path]=uigetfile('*.bmp;*.jpg','select test image');
imagen=imread([path,file]);
% Show image
figure,imshow(imagen),title('INPUT IMAGE')
%  imagen=imcrop(imagen);
% Convert to gray scale
if size(imagen,3)==3 %RGB image
    imagen=rgb2gray(imagen);
    figure,imshow(imagen),title('Gray Scale Image')
end
% Convert to BW
threshold = graythresh(imagen);
imagen =~im2bw(imagen,threshold);
figure,imshow(imagen),title('Black and White image')
% Remove all object containing fewer than 30 pixels
imagen = bwareaopen(imagen,300);
%Storage matrix word from image
SE = strel('disk', 5);
imagen=imdilate(imagen,SE);
figure,imshow(imagen),title('Dilated Image')
re=imagen;
rt=0;
figure,imshow(imagen),title('Segmented line')

% Compute the number of letters in template file
while 1
    %Fcn 'lines' separate lines in text
    [fl,re,r]=lines(re);
    imgn=fl;
    rt=rt+r;
    
    hold on
    rectangle('position',[1 rt size(imagen,2) 1],'EdgeColor','g')
    %*When the sentences finish, breaks the loop
    if isempty(re)  %See variable 're' in Fcn 'lines'
        break
    end    
end
