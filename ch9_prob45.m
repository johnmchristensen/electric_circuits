zc = 0 -2i
zl = 4i;
zr = 2;
i = 35;

syms v1 v2;
node1 = i == v1/zc + (v1 - v2) / zl;
node2 = ((v2 - v1) / zl) == v2/zc + v2/zr;

sol = solve([node1, node2], [v1, v2])

i0 = sol.v2 / zr
fprintf("i0 = %s\n", display_phasor(i0))
