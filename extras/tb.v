
`timescale 1ns/1ns
module tb;
				
	reg			clk;
	reg 			rst;
	
	
	reg	[31:0] input_theta
	reg	[31:0] input_x;
	reg   input_theta_stb;
	reg   input_x_stb;
	reg  output_activation_ack;
	
	wire  bringInNextSetofInput; 
	wire  [31:0] activation;
	wire  output_activation_stb;
	
	Activation DUT(		//inputs
			input_theta, //input_a
			input_x,//input_b
			input_theta_stb, //input_a_stb,
			input_x_stb, //input_b_stb,
			output_activation_ack, //output_z_ack
			clk,
			rst, // active high reset
			//outputs
			activation, //Θ10.Xo+ Θ11.X1 + Θ12.X2
			output_activation_stb, // output_z_stb
			bringInNextSetofInput//
			);
	integer i;
	reg [31:0] a[0:2];
	reg [31:0] theta[0:2];
initial
	begin
			
		i = 0;
		rst = 1;
		output_activation_ack<=0;
		//output_SOP = 32'd0;
		//output_z_ack = 1;
		a[0]=32'b00111111001010101010101010101011;//.6666667 //0x3f2aaaab
		a[1]=32'b00111110100000000000000000000000;//.25//0x3e800000
		a[2]=32'b00111110100110011001100110011010;//.3//0x3e99999a
		
		theta[0]=32'b00111111000000000000000000000000;//.5 //0x3f000000
		theta[1]=32'b00111110110111000010100011110110;//.43 //0x3edc28f6
		theta[2]=32'b00111111001101100100010110100010;//.712 //0x3f3645a2
		
		//SOLUTIONS VERIFICATION
		//product1 =.6666667 *.5 =>.33333335 (0x3eaaaaab)
		//product2 =.25*.43      => 0.1075  (0x3ddc28f6)
		//product3 =.3*.712      => 0.2136  (0x3e5ab9f5)
		
		//sumOfProd=.6544335 (0x3f2788f4)
		//Sigmoid (C)=1/(1+abs(x)) where x is sum
		//C= (.6544335/1.6544335)=.395563496
		//=(C+1)/2 =>.697781748 (0x3f32a1d3)
		#2 rst = 0;	i=i+1; input_x<=a[0];input_theta<=theta[0];input_x_stb <= 1;input_theta_stb <=1;
		
		
		#1000 $stop;
	end
always @ (posedge clk) begin
		
		if(bringInNextSetofInput==1)
		begin
		input_x <= a[i];//{a_1,a_2,a_3};
		
		
		input_theta <= theta[i];//{theta_1,theta_2,theta_3};
		
		input_x_stb <= 1;
		input_theta_stb <=1;// both stay for atleast
		i <= i+1;
		end
		
		
	end
	

	
initial
	begin
		clk=0;
		forever #1 clk=~clk;
	end


endmodule
	