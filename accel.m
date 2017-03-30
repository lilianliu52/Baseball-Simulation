%PHYS350

% function to compute acceleration given velocity

function accel = accel(v,Cd,rho,A,m,g,Dm,w)

vel = [v(1) v(2) v(3)];
vmag  = norm(vel);

magnus = m*Dm*cross(w,v);

force = [-0.5*Cd*rho*A*vmag*v(1) + magnus(1), -0.5*Cd*rho*A*vmag*v(2) + magnus(2), -0.5*Cd*rho*A*vmag*v(3) - m*g + magnus(3)];

accel = force/m;

return
