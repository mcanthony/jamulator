# 6502 specs

# flags:	bit 0 - Add 1 to num_cycles if page boundary is crossed
#			bit 1 - Add 2 if branch occurs to different page


# opcode:assembly language form:num_bytes:num_cycles:flag
69:ADC #%i:2:2:00
65:ADC %i:2:3:00
75:ADC %i,X:2:4:00
60:ADC %i:3:4:00
7D:ADC %i,X:3:4:01
79:ADC %i,Y:3:4:01
61:ADC (%i,X):2:6:00
71:ADC (%i),Y:2:5:01
29:AND #%i:2:2:00
25:AND %i:2:3:00
35:AND %i,X:2:4:00
2D:AND %i:3:4:00
3D:AND %i,X:3:4:01
39:AND %i,Y:3:4:01
21:AND (%i,X):2:6:00
31:AND (%i),Y:2:5:00
0A:ASL A:1:2:00
06:ASL %i:2:5:00
16:ASL %i,X:2:6:00
0E:ASL %i:3:6:00
1E:ASL %i,X:3:7:00
90:BCC %i:2:2:03
B0:BCS %i:2:2:03
F0:BEQ %i:2:2:03
24:BIT %i:2:3:00
2C:BIT %i:3:4:00
30:BMI %i:2:2:03
D0:BMI %i:2:2:03
10:BPL %i:2:2:03
00:BRK:1:7:00
50:BVC %i:2:2:03
70:BVS %i:2:2:03
18:CLC:1:2:00
D8:CLD:1:2:00
58:CLI:1:2:00
B8:CLV:1:2:00
C9:CMP #%i:2:2:00
C5:CMP %i:2:3:00
D5:CMP %i,X:2:4:00
CD:CMP %i:3:4:00
DD:CMP %i,X:3:4:01
D9:CMP %i,Y:3:4:01
C1:CMP (%i,X):2:6:00
D1:CMP (%i),Y:2:5:01
E0:CPX #%i:2:2:00
E4:CPX %i:2:3:00
EC:CPX %i:3:4:00
C0:CPY #%i:2:2:00
C4:CPY %i:2:3:00
CC:CPY %i:3:4:00
C6:DEC %i:2:5:00
D6:DEC %i,X:2:6:00
CE:DEC %i:3:6:00
DE:DEC %i,X:3:7:00
CA:DEX:1:2:00
88:DEY:1:2:00
49:EOR #%i:2:2:00
45:EOR %i:2:3:00
55:EOR %i,X:2:4:00
40:EOR %i:3:4:00
5D:EOR %i,X:3:4:01
59:EOR %i,Y:3:4:01
41:EOR (%i,X):2:6:00
51:EOR (%i),Y:2:5:01
E6:INC %i:2:5:00
F6:INC %i,X:2:6:00
EE:INC %i:3:6:00
FE:INC %i,X:3:7:00
E8:INX:1:2:00
C8:INY:1:2:00
4C:JMP %i:3:3:00
6C:JMP (%i):3:5:00
20:JSR %i:3:6:00
A9:LDA #%i:2:2:00
A5:LDA %i:2:3:00
B5:LDA %i,X:2:4:00
AD:LDA %i:3:4:00
BD:LDA %i,X:3:4:01
B9:LDA %i,Y:3:4:01
A1:LDA (%i,X):2:6:00
B1:LDA (%i),Y:2:5:01
A2:LDX #%i:2:2:00
A6:LDX %i:2:3:00
B6:LDX %i,Y:2:4:00
AE:LDX %i:3:4:00
BE:LDX %i,Y:3:4:01
A0:LDY #%i:2:2:00
A4:LDY %i:2:3:00
B4:LDY %i,X:2:4:00
AC:LDY %i:3:4:00
BC:LDY %i,X:3:4:01
4A:LSR A:1:2:00
46:LSR %i:2:5:00
56:LSR %i,X:2:6:00
4E:LSR %i:3:6:00
5E:LSR %i,X:3:7:00
EA:NOP:1:2:00
09:ORA #%i:2:2:00
05:ORA %i:2:3:00
15:ORA %i,X:2:4:00
0D:ORA %i:3:4:00
10:ORA %i,X:3:4:01
19:ORA %i,Y:3:4:01
01:ORA (%i,X):2:6:00
11:ORA (%i),Y:2:5:00
48:PHA:1:3:00
08:PHP:1:3:00
68:PLA:1:4:00
28:PLP:1:4:00
2A:ROL A:1:2:00
26:ROL %i:2:5:00
36:ROL %i,X:2:6:00
2E:ROL %i:3:6:00
3E:ROL %i,X:3:7:00
6A:ROR A:1:2:00
66:ROR %i:2:5:00
76:ROR %i,X:2:6:00
6E:ROR %i:3:6:00
7E:ROR %i,X:3:7:00
4D:RTI:1:6:00
60:RTS:1:6:00
E9:SBC #%i:2:2:00
E5:SBC %i:2:3:00
F5:SBC %i,X:2:4:00
ED:SBC %i:3:4:00
FD:SBC %i,X:3:4:01
F9:SBC %i,Y:3:4:01
E1:SBC (%i,X):2:6:00
F1:SBC (%i),Y:2:5:00
38:SEC:1:2:00
F8:SED:1:2:00
78:SEI:1:2:00
85:STA %i:2:3:00
95:STA %i,X:2:4:00
8D:STA %i:3:4:00
9D:STA %i,X:3:5:00
99:STA %i, Y:3:5:00
81:STA (%i,X):2:6:00
91:STA (%i),Y:2:6:00
86:STX %i:2:3:00
96:STX %i,Y:2:4:00
8E:STX %i:3:4:00
84:STY %i:2:3:00
94:STY %i,X:2:4:00
8C:STY %i:3:4:00
AA:TAX:1:2:00
A8:TAY:1:2:00
BA:TSX:1:2:00
8A:TXA:1:2:00
9A:TXS:1:2:00
98:TYA:1:2:00