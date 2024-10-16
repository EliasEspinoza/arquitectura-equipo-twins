`timescale 1ns/1ns

module chocorrolTB ();

reg[19:0] inTB;
wire[31:0] r;
wire zf;

chocorrol ch1(
	.in(inTB),
	.resultadoF(r),
	.zflow(zf));

reg[31:0] Mem[19:0];
integer i;

initial begin
	$readmemb("datosBinario.txt",Mem);
	#10;
end

initial
begin
	for(i=0; i<10; i=i+1) begin
		inTB = Mem[i];
		#100;
	end
end



endmodule
