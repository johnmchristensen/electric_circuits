function str = display_phasor(complex_num)
    % FROM_PHASOR Converts a complex number to a "Mag @ Deg" string
    
    mag = abs(complex_num);
    phase_deg = rad2deg(angle(complex_num));
    
    % Format the string to 2 decimal places
    str = sprintf('%.3f @ %.3f degrees', mag, phase_deg);
end