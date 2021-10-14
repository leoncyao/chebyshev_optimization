\ Model chebyshev
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  c_pow_2 + [ 2 a ^2 + 4 a * b + 4 a * c + 0.125 a_inv_pow_2 * b_pow_4
   + 2 b ^2 + 4 b * c - b_pow_2 * c_over_a + 4 c ^2 ] / 2 
Subject To
 a_inv_constr: [ a * a_inv ] = 1
 a_pow_constr: - a_pow_2 + [ a ^2 ] = 0
 a_inv_constr: [ a_pow_2 * a_inv_pow_2 ] = 1
 b_pow_2_constr: - b_pow_2 + [ b ^2 ] = 0
 b_pow_3_constr: - b_pow_3 + [ b * b_pow_2 ] = 0
 b_pow_4_constr: - b_pow_4 + [ b_pow_2 ^2 ] = 0
 c_pow_2_constr: - c_pow_2 + [ c ^2 ] = 0
 c_over_a_constr: - c_over_a + [ a_inv * c ] = 0
Bounds
 -100 <= a <= 100
 -100 <= a_pow_2 <= 100
 -100 <= a_inv <= 100
 -100 <= a_inv_pow_2 <= 100
 -100 <= b <= 100
 -100 <= b_pow_2 <= 100
 -100 <= b_pow_3 <= 100
 -100 <= b_pow_4 <= 100
 -100 <= c <= 100
 -100 <= c_pow_2 <= 100
 -100 <= c_over_a <= 100
Generals
 a a_pow_2 b b_pow_2 b_pow_3 b_pow_4 c c_pow_2
End
