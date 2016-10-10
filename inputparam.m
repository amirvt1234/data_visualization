function [fid,fid1,fid2] = inputparam(efield_data,st_data)

	global X Y XC YC VX VY TAG V P CO MAG N CURV ST mag co data data1 


	fid= fopen('NOFZONES.log');
	data=textscan(fid,'%*s%n%*s%*s%f32%*s%*s%f32');
	zn=data{1};
	frame_t=data{3};
	fid  = fopen('param_pc.log');
	data = textscan(fid,'%*s%n%n');
	param_input=cell2mat(data);
	mesh(1,:)=param_input(1,:);
	mesh(1,3)=mesh(1,1)*mesh(1*2);

	answer = lower(input(['The number of available frames are equal to : ',int2str(zn(length(frame_t)))  '\n'  ...
		              'The final time is equal to : ', num2str(frame_t(length(frame_t)))            '\n'   ...
		              'Inter the approximate time of the frame you want to plot your data?','\n'           ...
		               ],'s'));

	plot_time=str2double(answer);

	if  (str2double(answer)>frame_t(length(frame_t))) || (str2double(answer)<0)
	    error('You have entered the wrong value')
	end

	[err, i]=min(abs(frame_t-plot_time));

	header=mesh(1,3)*(i-1);
	fid  = fopen('SPH.dat');
	data=textscan(fid,'%f64%f64%f64%f64%f64%n',mesh(1,3),'HeaderLines',header);
	XC=data{:,1};
	YC=data{:,2};
	VX=data{:,3};
	VY=data{:,4};
	p=data{:,5};
	TAG=data{:,6};
	v=sqrt(VX.^2+VY.^2);


	if st_data==1
	    fid1  = fopen('ST.dat');
	    data1=textscan(fid1,'%f64%f64%f64%f64%f64%f64%f64',mesh(1,3),'HeaderLines',header);
	    NX=data1{:,1};
	    NY=data1{:,2};
	    mag=data1{:,3};
	    STX=data1{:,4};
	    STY=data1{:,5};
	    curv=data1{:,6};
	    co=data1{:,7};
	    st=sqrt(STX.^2+STY.^2);
	    n=sqrt(NX.^2+NY.^2);
	end
	if efield_data==1
	    fid2  = fopen('SPH.dat');
	    data2=textscan(fid,'%f64%f64%f64%f64%f64%f64%f64',mesh(1,3),'HeaderLines',header);
	end


	 clear data data1 answer delta_t error   header i rangeX rangeY  

	fclose('all')

	rangeX=floor(min(XC)):.01:ceil(max(XC)/2);
	rangeY=floor(min(YC)):.01:ceil(max(YC));
	[X,Y]=meshgrid(rangeX,rangeY);

	V=griddata(XC,YC,v,X,Y);
	P=griddata(XC,YC,p,X,Y);
	CO=griddata(XC,YC,co,X,Y);
	MAG=griddata(XC,YC,mag,X,Y);
	N=griddata(XC,YC,n,X,Y);
	CURV=griddata(XC,YC,curv,X,Y);
	ST=griddata(XC,YC,st,X,Y);


	return
