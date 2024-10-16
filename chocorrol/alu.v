`timescale 1ns/1ns

module mod_and (
	input[31:0] A,
	input[31:0] B,
	output[31:0] S1
);
assign S1 = A & B;
endmodule


module mod_or (
	input[31:0] A,
	input[31:0] B,
	output[31:0] S2
);
assign S2 = A | B;
endmodule


module mod_add (
	input[31:0] A,
	input[31:0] B,
	output[31:0] S3
);
assign S3 = A + B;
endmodule


module mod_sub (
	input[31:0] C,
	input[31:0] D,
	output[31:0] S4
);
assign S4 = C - D;
endmodule


module setOnLessThan (
	input[31:0] D,
	input[31:0] E,
	output reg[31:0] S5
);
always@(*)begin
	if(D < E) begin
		S5 = 32'b1;
	end else begin
		S5 = 32'b0;
	end
end
endmodule


module mod_nor (
	input[31:0] B,
	input[31:0] C,
	output[31:0] S6
);
assign S6 = ~(B | C);
endmodule


module ALU (
	input[31:0] operand1,
	input[31:0] operand2,
	input[2:0] sel,
	output reg[31:0] resultado,
	output reg zf
);

wire[31:0] w1, w2, w3, w4, w5, w6;

mod_and I1(.A(operand1),.B(operand2),.S1(w1));
mod_or I2(.A(operand1),.B(operand2),.S2(w2));
mod_add I3(.A(operand1),.B(operand2),.S3(w3));
mod_sub I4(.C(operand1),.D(operand2),.S4(w4));
setOnLessThan I5(.D(operand1),.E(operand2),.S5(w5));
mod_nor I6(.B(operand1),.C(operand2),.S6(w6));

always@(*) begin
	case (sel)
	3'b000: resultado = w1;
	3'b001: resultado = w2;
	3'b010: resultado = w3;
	3'b110: resultado = w4;
	3'b111: resultado = w5;
	3'b100: resultado = w6;
	default: resultado = 32'd0;
	endcase
end
	
always@(*) begin
	if(resultado == 0) begin
		zf = 1'b1;
	end
end

always@(*) begin
	if(resultado != 0) begin
		zf = 1'b0;
	end
end

endmodule
