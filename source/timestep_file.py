def timestep_(dx,cfl,EqFLAG,cx=None,nu=None):
    dt=0
    if EqFLAG == 'DAdvection':
        dt = cfl*dx/cx
    elif EqFLAG == 'DDiffusion':
        dt = cfl*dx*dx/nu
    elif ((EqFLAG == 'DAD') or (EqFLAG == 'DBurgers')):
        dt=min(cfl*dx/cx,cfl*dx*dx/nu)
    return dt

