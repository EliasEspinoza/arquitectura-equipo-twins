`timescale 1ns/1ns

module chocorrol (
	input[19:0] in,
	output[31:0] resultadoF,
	output zflow
);

wire[31:0] op1, op2, re;

memoria1 m1(
	.dirLec1(in[17:13]),
	.dirLec2(in[9:5]),
	.we(in[19]),
	.datosOut1(op1),
	.datosOut2(op2));


ALU a1(
	.operand1(op1),
	.operand2(op2),
	.sel(in[12:10]),
	.resultado(re),
	.zf(zflow));
	

memoria2 m2(
	.datos(re),
	.dirEsc(in[4:0]),
	.dirLec1(in[4:0]),
	.we(in[18]),
	.datosOut1(resultadoF));


endmodule
