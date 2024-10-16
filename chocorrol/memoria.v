`timescale 1ns/1ns

module memoria1 (
	input[4:0] dirLec1,
	input[4:0] dirLec2,
	input we,
	output reg[31:0] datosOut1,
	output reg[31:0] datosOut2
);

reg[31:0] Men[0:31];

initial begin
	$readmemh("datos.txt",Men);
	#10;
end

always@(*)
begin
	if(!we) begin
	//Leer
	datosOut1 = Men[dirLec1];
	datosOut2 = Men[dirLec2];
	end
end 

endmodule

module memoria2 (
	input[31:0] datos,
	input[4:0] dirEsc,
	input[4:0] dirLec1,
	input we,
	output reg[31:0] datosOut1
);

reg[31:0] Men[0:31];

always@(*)
begin
	if(we) begin
	//Escribir
	Men[dirEsc] = datos;
	end else begin
	//Leer
	datosOut1 = Men[dirLec1];
	end
end 

endmodule
