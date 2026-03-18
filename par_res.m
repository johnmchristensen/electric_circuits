function R_total = par_res(R_vector)
    % PAR_RES Calculates the total resistance of resistors in parallel.
    % Input: R_vector - A vector or matrix of resistance values (Ohms).
    % Output: R_total - The equivalent resistance (Ohms).

    % 1. Filter out zeros to avoid 'Division by Zero' warnings
    % (Physically, a 0-ohm resistor in parallel results in 0 ohms total)
    if any(R_vector == 0)
        R_total = 0;
        return;
    end

    % 2. The core calculation: 1 / sum(1/R1 + 1/R2 + ... + 1/Rn)
    % We use ./ for element-wise division
    R_total = 1 / sum(1 ./ R_vector);
end